from src.utils.utilities import tuple_it_if_needed, sort_keep_unique_tuple_list

import src.client.models.actions
from src.helpers.freepie_vars import FreePieVars

# TODO: merge JoyBtnData and JoyPovData redundancies
class IBtnPovAction(object):
    def __init__(self):
        self.actions = None

    def get_action_tied_to_modifiers(self, modifiers):
        for action in self.actions:
            if action.joy_modifiers == modifiers:
                return action

        return None

class JoyBtnData(object):
    def __init__(self, button):
        JoyBtnData._check_button(button)

        self.__button  = button
        self.actions = None

    @property
    def button(self):
        return self.__button

    def __eq__(self, other):
        return  self.__class__ == other.__class__ and self.button == other.button

    def __hash__(self):
        return hash((self.button,))

    def map_to(self, *actions):
        if self.actions is not None:
            raise RuntimeError("The button '{}' can only be mapped once.".format(self.button))

        if len(actions) == 0 :
            raise ValueError("The button {} was mapped to an empty actions list.".format(self.button))

        modifiers_found = []

        for action in actions:
            if not isinstance(action, src.client.models.actions.ActionData):
                raise ValueError("The button {} was mapped to an action that is not an ActionData (specified: type={}, val={}).".format(self.button, type(action), action))

            if action.joy_modifiers in modifiers_found:
                raise RuntimeError("The button {} was mapped with at least two actions defined on the same joystick modifiers! ( modifiers: {} )".format(self.button, action.joy_modifiers))

            modifiers_found.append(action.joy_modifiers)

        self.actions = actions

        # TODO: catch duplicate of 2 actions for the same modifiers

        return self

    def get_action_tied_to_modifiers(self, modifiers):
        for action in self.actions:
            if action.joy_modifiers == modifiers:
                return action

        return None

    @staticmethod
    def _check_button(button):
        if type(button) is not int:
            raise ValueError("A button must be an int (specified: {}).".format(button))

    @staticmethod
    def command_of(button, modifiers):
        JoyBtnData._check_button(button)

        if type(modifiers) is not int and type(modifiers) is not tuple:
            raise ValueError("You tried to retrive a joystick button reference for button {} with modifiers that is neither an int or a tuple (specified: {}).".format(button, modifiers))

        if type(modifiers) is tuple:
            for modifier in modifiers:
                if type(modifier) is not int:
                    raise ValueError("You cannot retrieve a joystick button reference for button {} with a modifier that is different than an int (specified: {})".format(button, modifier))

        return JoyBtnRef(button, sort_keep_unique_tuple_list(tuple_it_if_needed(modifiers)))

class JoyBtnRef(object):
    def __init__(self, button, modifiers):
        self.button    = button
        self.modifiers = modifiers