import threading
import time
import copy
import types
from src.helpers.freepie_vars import FreePieVars
from src.utils.utilities      import tuple_it_if_needed

class JoyMappingsOrchestrator:
    # the logic of unique ID for hash should be here ?
    def __init__(self, *joy_mappings):
        self.joy_mappings = joy_mappings

    def map_in_loop(self):
        for joy_mapping in self.joy_mappings:
            joy_mapping.map_in_loop()

class AxesThread(threading.Thread):
    def __init__(self, threadID, name, joy_axes_transfer):
        threading.Thread.__init__(self)
        self.threadID      = threadID
        self.name          = name
        self.axes_transfer = joy_axes_transfer
        self._running      = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            for axis_transfer in self.axes_transfer:
                axis_transfer.transfer()

class JoyMapping:

    # joy_btns = (JoyBtn1, JoyBtn2, ...)
    # joy_povs = (JoyPovCardinal1, JoyPovCardinal2, ...)

    # the logic of unique ID for hash should be here ?
    def __init__(self, joy_modifiers_actions, joy_axes_transfer):

        self.axes_transfer = tuple_it_if_needed(joy_axes_transfer)

        temp = tuple(sorted(
            tuple_it_if_needed(joy_modifiers_actions),
            reverse = True,
            key     = lambda joy_modifiers_action: len(joy_modifiers_action.modifiers)
        ))

        i = 0
        while i < len(temp):
            temp[i].modifiers = tuple(sorted(temp[i].modifiers))
            i += 1

        self.joy_modifiers_actions = temp

        # idea: give unique hash ID to all actions, used for sets
        self._old_actions = set()
        self._new_actions = set()

        self._gen_hash()

        # for thread in threading.enumerate():
        #     if thread.name == "Axes Thread":
        #         thread.terminate()
        #         thread.join()
        #         del(thread)

        # self.thread1 = AxesThread(1, "Axes Thread", self.axes_transfer)
        # self.thread1.start()

        self._new_actions_hold  = set()
        self._new_actions_press = set()

        # for joy_modifiers_action in self.joy_modifiers_actions:
        #     FreePieVars.diagnostics.debug(joy_modifiers_action.modifiers)

    ## IDEA: hash value as a tuple index
    def _gen_hash(self):
        h = 0

        for joy_modifiers_action in self.joy_modifiers_actions:

            for btn_action in joy_modifiers_action.btns_action:
                dirty_hash_setter(btn_action.flagged_action, h)
                h += 1

            for pov_action in joy_modifiers_action.povs_action:
                dirty_hash_setter(pov_action.flagged_action, h)
                h += 1

            for axis_threshold_action in joy_modifiers_action.axes_thresholds_action:
                dirty_hash_setter(axis_threshold_action.flagged_action, h)
                h += 1

    # print in debug the mappings registered in a pretty format (ASCII Tree?)
    # Joystick Modifiers - (4, 5)
    # |
    #  ----- Button 4
    # |      |
    # |       ------ Keyboard: Shift + A
    # |
    #  ----- POV 0 | Cardinal 0
    # |
    def _mappings_summary(self):
        pass

    # TODO: Review structure, this class should do something different with models
    # to make blocking modifiers, top-level parent of btn down should be the modifiers
    # if modifier1: if bt1 down: action related to modifier1; same for pov
    #               if bt2 down: ...
    # elif modifier2: if bt1 down: ...
    # else: ... (no modifier)
    # for quick cross-ref with action related to modifiers, investiaate hash/indices
    def map_in_loop(self):
        #
        self._new_actions_hold.clear()
        self._new_actions_press.clear()

        for axis_transfer in self.axes_transfer:
            axis_transfer.transfer()

        #
        for joy_modifiers_action in self.joy_modifiers_actions:
            if joy_modifiers_action.is_down():

                for btn_action in joy_modifiers_action.btns_action:
                    if btn_action.is_down():

                        if btn_action.flagged_action.command.is_press():
                            self._new_actions_press.add(btn_action.flagged_action)
                        else:
                            self._new_actions_hold.add(btn_action.flagged_action)

                for pov_action in joy_modifiers_action.povs_action:
                    if pov_action.is_down():
                        if pov_action.flagged_action.command.is_press():
                            self._new_actions_press.add(pov_action.flagged_action)
                        else:
                            self._new_actions_hold.add(pov_action.flagged_action)

                # BUG: axis threshold creates non-negligeable lag, need to investigate
                # for axis_threshold_action in joy_modifiers_action.axes_thresholds_action:
                #     if axis_threshold_action.is_threshold_reached():
                #         if axis_threshold_action.flagged_action.command.is_press():
                #             self._new_actions_press.add(axis_threshold_action.flagged_action)
                #         else:
                #             self._new_actions_hold.add(axis_threshold_action.flagged_action)

                # because it is sorted by len we can break
                break

        #
        # for old_action in self._old_actions:
        #     if old_action not in self._new_actions:
        #         old_action.flag = False
        #         old_action.command.release()

        # for new_action in self._new_actions:
        #     if new_action.flag == False:
        #         new_action.flag = True
        #         new_action.speech()
        #     new_action.command.hold()

        for old_action in self._old_actions:
            if old_action not in self._new_actions_hold:
                old_action.deactivate()

        for new_action in self._new_actions_press:
            new_action.press()

        for new_action in self._new_actions_hold:
            new_action.activate()

        self._old_actions = self._new_actions_hold.copy()

def dirty_hash_setter(obj, val):
    obj.__hash__  = types.MethodType(lambda self: val, obj)
