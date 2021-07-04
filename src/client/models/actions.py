from src.utils.utilities import tuple_it_if_needed, sort_keep_unique_tuple_list

import src.client.models.joy_buttons
import src.client.models.joy_povs
import src.client.models.vjoy

from src.helpers.freepie_vars import FreePieVars

def _is_command_type_valid(command):
    return isinstance(command, (
                    str,
                    src.client.models.vjoy.VJoyBtnRef,
                    src.client.models.vjoy.VJoyPovCardinalRef
                )
            )

def _is_copy_command_type_valid(copy_command):
    return isinstance(copy_command, (
                    src.client.models.joy_buttons.JoyBtnRef,
                    src.client.models.joy_povs.JoyPovCardinalRef
                )
            )

class ActionData(object):
    def __init__(self, label, joy_modifiers, speech_text = None, command = None, copy_commands = None):
        if not isinstance(label, str):
            raise ValueError("An action's label must be a string (specified: {}).".format(type(label)))

        if not isinstance(joy_modifiers, (int, tuple)):
            raise ValueError("An action's modifiers must be an int or a tuple (specified: {}).".format(type(joy_modifiers)))

        if speech_text is not None and not isinstance(speech_text, str):
            raise ValueError("An action's speech text must be a string (specified: {}).".format(type(speech_text)))

        if command is None and copy_commands is None:
            raise ValueError("An action's 'command' and 'copy_commands' cannot be both empty/None. You must specify one or both.")

        if command is not None and \
            not _is_command_type_valid(command) and \
            not isinstance(command, (SequenceCommandData, tuple)):
            raise ValueError("An action's 'command' is of invalid type (specified: {}).".format(type(command)))

            if isinstance(command, tuple):
                if len(command) == 0 :
                    raise ValueError("An action's 'command' cannot be an empty tuple. Are you sure you want to define a 'command'?")

                command = SequenceCommandData().rotate(False).create(command)

        if copy_commands is not None:
            copy_commands = tuple_it_if_needed(copy_commands)

            if len(copy_commands) == 0 :
                raise ValueError("An action's 'copy_commands' cannot be an empty tuple. Are you sure you want to define a 'copy_commands'?")

                for copy_command in copy_commands:
                    if not _is_copy_command_type_valid(copy_command):
                        raise ValueError("An action's 'copy_commands' was a tuple containing an element of invalid type. (specified: {}).".format(type(copy_command)))

        self.label         = label
        self.speech_text   = speech_text
        self.joy_modifiers = sort_keep_unique_tuple_list(tuple_it_if_needed(joy_modifiers))
        self.command       = command
        self.copy_commands = copy_commands

class ThresholdActionData(object):
    def __init__(self, threshold_value_percent):
        if type(threshold_value_percent) is not int and type(threshold_value_percent) is not float:
            raise ValueError("A threshold's value must be either an int or a float (specified: {}).".format(type(threshold_value_percent)))

        self.threshold_value = threshold_value_percent * 1.0
        self.direction_val   = None
        self.actions         = None

    def direction(self, direction):
        if type(direction) is not str:
            raise ValueError("A threshold's direction must be a string (specified: {}).".format(type(direction)))

        direction = direction.lower()

        if direction != 'up' and direction != 'down' and direction != 'both':
            raise ValueError("A threshold's direction must be either 'up', 'down' or 'both'.")

        self.direction_val = direction
        return self

    def map_to(self, *actions):
        if self.direction_val is None:
            raise RuntimeError("A threshold's direction must be set before setting a map.")

        modifiers_found = []

        for action in actions:
            if not isinstance(action, ActionData):
                raise ValueError("A threshold can only be mapped to a valid ActionData (specified: {}).".format(type(action)))

            if action.joy_modifiers in modifiers_found:
                raise RuntimeError("A threshold cannot be mapped with two actions defined on the same joystick modifiers! ( threeshold value: {}, modifiers: {} )".format(self.threshold_value, action.joy_modifiers))

            modifiers_found.append(action.joy_modifiers)

        self.actions = actions

        return self

class SequenceCommandData(object):
    def __init__(self, is_sequence_a_rotation = None):
        self.is_rotate_activated = is_sequence_a_rotation
        self.commands            = None

    def rotate(is_sequence_a_rotation):
        self.is_rotate_activated = is_sequence_a_rotation
        return self

    def create(self, *commands):
        if self.is_rotate_activated is None:
            raise RuntimeError("A sequence must define a rotational state before getting to the creation process.")

        if len(commands) == 0 :
            raise ValueError("An sequence cannot be empty.")

        for command in commands:
            if command is None or not _is_command_type_valid(command):
                raise ValueError("A sequence contains an action of invalid type (specified: {}".format(type(command)))

        self.commands = commands
        return self
