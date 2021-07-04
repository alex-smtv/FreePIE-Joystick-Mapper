from src.utils.utilities import tuple_it_if_needed

class FlaggedAction:
    def __init__(self, label, speech_text, command, speech):
        self.flag  = False

        self.label        = label
        self.speech_text  = speech_text
        self.speech_voice = speech

        # could be a unit or a sequence
        self.command = command

    def speech(self):
        if self.speech_text:
            self.speech_voice.say(self.speech_text)

    def activate(self):
        if not self.flag:
            self.flag = True
            self.speech()

        self.command.hold()

    def deactivate(self):
        self.flag = False
        self.command.release()

class JoyModifiersAction:
    def __init__(self, joy, modifiers, btns_action, povs_action, axes_thresholds_action):
        self.joy                    = joy
        self.modifiers              = tuple_it_if_needed(modifiers)
        self.btns_action            = tuple_it_if_needed(btns_action)
        self.povs_action            = tuple_it_if_needed(povs_action)
        self.axes_thresholds_action = tuple_it_if_needed(axes_thresholds_action)

    def is_down(self):
        for modifier in self.modifiers:
            if not self.joy.getDown(modifier):
                return False

        return True

class JoyBtnAction:
    def __init__(self, joy, btn, flagged_action):
        self.joy            = joy
        self.btn            = btn
        self.flagged_action = flagged_action

    def is_down(self):
        return self.joy.getDown(self.btn)

class JoyPovAction:
    def __init__(self, joy, pov_index, pov_cardinal, flagged_action):
        self.joy            = joy
        self.pov_index      = pov_index
        self.pov_cardinal   = pov_cardinal
        self.flagged_action = flagged_action

    def is_down(self):
        return self.joy.pov[self.pov_index] == self.pov_cardinal

class AxisThresholdAction:
    def __init__(self, vjoy_axis_manager, threshold_percent, threshold_direction, flagged_action):
        self.vjoy_axis_manager = vjoy_axis_manager

        self.threshold_raw  = 1.0 * threshold_percent * self.vjoy_axis_manager.axisMax / 100
        self.is_threshold_direction_up = (threshold_direction.lower() == 'up')

        self.flagged_action = flagged_action

        self.reached_once = False

    def is_threshold_reached(self):
        if self.is_threshold_direction_up:
            is_reached = self.vjoy_axis_manager.get_value() >= self.threshold_raw

        else:
            is_reached = self.vjoy_axis_manager.get_value() <= self.threshold_raw

        if is_reached:
            if self.reached_once:
                is_reached = False
            else:
                self.reached_once = True
        else:
            self.reached_once = False

        return is_reached