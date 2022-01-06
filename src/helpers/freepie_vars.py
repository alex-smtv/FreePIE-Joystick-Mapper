# encoding: utf-8
from src.helpers.freepie_helper import KeyExtended

# This class will serve as a pivotal point to access useful variables provided within FreePie without the need to jungle instances around.
class FreePieVars(object):
    # Last char doesn't contain any / or \
    root_script_path = None

    joysticks   = None
    vjoys       = None
    keyboard    = None
    Key         = None
    KeyE        = None
    diagnostics = None
    speech      = None

    _is_all_set = False

    # TODO: None checking with properties and setter
    @staticmethod
    def feed_with(root_script_path, joysticks, vjoys, keyboard, Key, diagnostics, speech):
        # TODO: handle case of duplicate separator (not very important, but more clean especially for printing)

        # Remove the last separator if it exists in script path
        last_char_index = len(root_script_path)-1
        last_char = root_script_path[last_char_index]
        
        if last_char == "\\" or last_char == "/":
            root_script_path = root_script_path[:last_char_index]

        FreePieVars.root_script_path = root_script_path.replace("/", "\\")
        FreePieVars.joysticks        = joysticks
        FreePieVars.vjoys            = vjoys
        FreePieVars.keyboard         = keyboard
        FreePieVars.Key              = Key
        FreePieVars.KeyE             = KeyExtended
        FreePieVars.diagnostics      = diagnostics
        FreePieVars.speech           = speech

        _is_all_set = True

    @staticmethod
    def check_vars():
        # check vars are corecctly set and not None
        pass