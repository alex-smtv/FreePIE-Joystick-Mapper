from src.helpers.freepie_vars   import FreePieVars
from src.utils.utilities        import tuple_it_if_needed

import gc, sys

class ProfileLoader:

    def __init__(self, profile_file_name):
        # TODO: Before anything, make sure FreePieVars is correctly setup!

        profile_module = 'profiles.' + profile_file_name

        # Reload a profile already loaded in FreePie (profile switching) so we can account for any change made
        # in the profile.
        # WARNING: be mindful of reload subtlety https://stackoverflow.com/a/7274356
        for key, value in sys.modules.items():
            if value is not None and profile_module in str(value):
                reload(sys.modules[key])
            else:
                exec 'import ' + profile_module

        candidates_func = []

        for member in dir(eval(profile_module)):
            member_access = eval(profile_module + '.' + member)

            if member.endswith('_mapping') and callable(member_access):
                candidates_func.append(member_access)
        # ---

        joys_mappings = []

        for mapping_func in candidates_func:
            joys_mappings.append( mapping_func().build(FreePieVars.joysticks, FreePieVars.vjoys, FreePieVars.keyboard, FreePieVars.speech) )

        self.joys_mappings = tuple_it_if_needed(joys_mappings)

        FreePieVars.diagnostics.notify('Profile - ' + profile_file_name, 'Freepie script is running...')
        FreePieVars.diagnostics.debug('Profile "' + profile_file_name + '" loaded.')

        # TODO: minify "orchestrator" with some call exclusions, create temp file and import that file

        # at end free up memory
        gc.collect()

    def loop_apply_mappings(self):
        for joy_mappings in self.joys_mappings:
            joy_mappings.map_in_loop()
