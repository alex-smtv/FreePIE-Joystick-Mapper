# encoding: utf-8
from src.helpers.freepie_helper import KeyExtended

# Cette classe va servir de pivot pour avoir accès aux variables keyboard etc. sans devoir transférer les instances à chaque fois à toutes les functions!
class FreePieVars(object):
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
    def feed_with(joysticks, vjoys, keyboard, Key, diagnostics, speech):
        FreePieVars.joysticks   = joysticks
        FreePieVars.vjoys       = vjoys
        FreePieVars.keyboard    = keyboard
        FreePieVars.Key         = Key
        FreePieVars.KeyE        = KeyExtended
        FreePieVars.diagnostics = diagnostics
        FreePieVars.speech      = speech

        _is_all_set = True

    @staticmethod
    def check_vars():
        # check vars are corecctly set and not None
        pass