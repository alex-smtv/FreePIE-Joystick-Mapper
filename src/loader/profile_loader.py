from src.helpers.freepie_vars   import FreePieVars
from src.utils.utilities        import tuple_it_if_needed

import gc, sys, os, threading, time

class ProfileFileWatcher(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(ProfileFileWatcher, self).__init__(group=group, target=target, name=name, verbose=verbose)
        self.args           = args
        self.kwargs         = kwargs
        self._is_keep_alive = True

        self._profile_selection_path = FreePieVars.root_script_path + "\profile_selected.txt"
        self._cached_profile_selection_stamp = 0
        self._cached_selected_profile_stamp  = 0

        self._is_profile_selection_changed   = False
        self._is_active_profile_changed      = False

        self._active_profile      = None
        self._active_profile_path = None

        self._pretty_profile_print = None
        self._raw_profile_print    = None

        if not os.path.isfile(self._profile_selection_path):
            message = 'The following file is missing: ' + self._profile_selection_path
            FreePieVars.diagnostics.debug(message)
            raise Exception(message)

    # Terminate the work of the thread
    def terminate(self):
        self._is_keep_alive = False

    # Check if a new profile is selected or if the selected profile was modified
    def is_new_state(self):
        return self._is_profile_selection_changed or self._is_active_profile_changed

    # Reset internal flags and return a tuple of the last known selected profile and 
    # its pretty format for printing
    def consume_state(self):
        self._is_profile_selection_changed = False
        self._is_active_profile_changed    = False
        return (self._active_profile, self._pretty_profile_print)

    # Check if the profile selectin has been changed. If not then check if the active file has been modified.
    def _watch_profile(self):
        stamp = os.stat(self._profile_selection_path).st_mtime

        # If profile selection file has been changed
        if stamp != self._cached_profile_selection_stamp:
            self._cached_profile_selection_stamp = stamp

            potential_profile = None

            # First we open the profile selection file and read its last line
            with open(self._profile_selection_path, 'r') as f:
                for line in f:
                    pass
                potential_profile = line.strip().replace("/", "\\")

            if potential_profile[-3:] == ".py":
                potential_profile = potential_profile[:-3]

            profiles_folder_separator = "\profiles\\"
            potential_selected_file = FreePieVars.root_script_path + profiles_folder_separator + potential_profile + ".py"
            
            # If last line is not a valid profile file, no profile can be loaded so its an error
            if potential_profile is None or not os.path.isfile(potential_selected_file):
                message = 'The following profile is selected, but could not be found: ' + potential_selected_file
                raise Exception(message)
            
            # If the selected profile file is the same as the current active profile, then nothing to do
            elif potential_selected_file == self._active_profile_path:
                return

            # The selected profile is a valid file and is a new one, treatment must be done before acknowledging the new state
            else:
                # Handle the case where the selected profile lies in subfolder(s):
                #   Make sure __init__.py exists on each subfolder (if not then create the file), including root /profiles/
                #   Remark: the file path correctness has already been checked previously
                i = potential_selected_file.rfind(profiles_folder_separator) + len(profiles_folder_separator)
                lenpf = len(potential_selected_file)
                
                # While we find a folder separator with find() in the profile path, we check each folder for the file __init__.py
                # We check 0 instead of -1, because we add +1 to find() to ommit the current separator found for the next loop
                while i != 0:
                    # Create file if it doesn't exist at the current folder
                    open(potential_selected_file[:i] + "__init__.py", "a+").close()

                    # Compute new index for the next folder
                    i = potential_selected_file.find("\\", i, lenpf) + 1

                # Go back to profile selection
                FreePieVars.diagnostics.debug("Profile Selection Watcher >> Profile selected: " + potential_selected_file)
                
                self._raw_profile_print            = potential_profile
                self._active_profile               = potential_profile.replace("\\", ".") # prepare correct format for later module loading
                self._active_profile_path          = potential_selected_file
                self._is_profile_selection_changed = True

                self._generate_pretty_profile_print()

                # Already store the stamp to prevent the next cycle to trigger a second load of the new profile selected
                self._cached_selected_profile_stamp = os.stat(potential_selected_file).st_mtime
        
        # If profile selection has not changed, then check whether the active selected profile has changed
        else:
            stamp = os.stat(self._active_profile_path).st_mtime
            if stamp != self._cached_selected_profile_stamp:
                self._generate_pretty_profile_print()

                FreePieVars.diagnostics.debug("Profile Selection Watcher >> Current profile has been modified: " + self._active_profile_path)
                self._cached_selected_profile_stamp = stamp
                self._is_active_profile_changed = True

    # Read currently stored active profile path to construct a pretty format
    def _generate_pretty_profile_print(self):
        # Read profile file to see if a pretty text has been set for its profile name
        print_format = None
        with open(self._active_profile_path, 'r') as f:
            line = f.readline().strip()
            if line.startswith("#:"):
                print_format = line[2:].strip()

        # Now we determine if the raw print contains any separator
        if self._raw_profile_print.find("\\") != -1:
                # If pretty text is not set, handle only \, if it is set handle \ until the one separating
                # the profile filename and replace the rest with the pretty text
                print_format = \
                    self._raw_profile_print.replace("\\", " -> ") if print_format is None else \
                    self._raw_profile_print[:self._raw_profile_print.rfind("\\")].replace("\\", " -> ") + " -> " + print_format
        else:
            # If no pretty text has been set for its profile name, then the original filename is used
            if print_format is None:
                print_format = self._raw_profile_print

        self._pretty_profile_print = print_format

    def run(self):
        try:
            while self._is_keep_alive:

                # If profile selection was changed, do not check again until the flag is turned off
                if not self._is_profile_selection_changed:
                    self._watch_profile()

                time.sleep(1)

        except Exception as e:
            FreePieVars.diagnostics.debug("Profile Selection Watcher Thread has encountered an error: " + str(e))
            raise e

class ProfileLoader:

    def __init__(self):
        self._thread_idstr = "profilewatcher"

        # Check for any residual running threads from multiple (previous) run to avoid any side effects
        for thread in threading.enumerate():
            if self._thread_idstr in thread.name:
                thread.terminate()
                thread.join()

        self._profile_watcher_thread = ProfileFileWatcher(
            name = self._thread_idstr
        )

        self._profile_watcher_thread.start()
        self.joys_mappings = []

    def _profile_load(self, profile_file_name, pretty_profile_print = None):
        # TODO: Check FreePieVars is correctly setup, this handle the case where the user is modifying a line he shouldn't

        profile_module = 'profiles.' + profile_file_name

        # Reload a profile already loaded in FreePie so we can account for any change made
        # in the profile.
        # WARNING: be mindful of reload subtlety https://stackoverflow.com/a/7274356
        # From all the registered modules, if the module is related to the profile we need then reload it.
        for key, value in sys.modules.items():
            if value is not None and profile_module in str(value):
                reload(sys.modules[key])

        exec 'import ' + profile_module

        candidates_func = []

        for member in dir(eval(profile_module)):
            member_access = eval(profile_module + '.' + member)

            if member.endswith('_mapping') and callable(member_access):
                candidates_func.append(member_access)

        joys_mappings = []

        for mapping_func in candidates_func:
            joys_mappings.append(
                mapping_func().build(
                    FreePieVars.joysticks, 
                    FreePieVars.vjoys, 
                    FreePieVars.keyboard, 
                    FreePieVars.speech
                )
            )

        self.joys_mappings = tuple_it_if_needed(joys_mappings)

        profile_print = profile_file_name if pretty_profile_print is None else pretty_profile_print
        message = 'Profile ' + profile_print + ' loaded.'

        FreePieVars.diagnostics.notify(message)
        FreePieVars.diagnostics.debug(message)

        # At end free up the memory
        gc.collect()

    def reload_check(self):
        if self._profile_watcher_thread.is_new_state():
            self._profile_load(
                # Tuple unpacking
                *self._profile_watcher_thread.consume_state()
            )

    def loop_apply_mappings(self):
        self.reload_check()

        for joy_mappings in self.joys_mappings:
            joy_mappings.map_in_loop()
