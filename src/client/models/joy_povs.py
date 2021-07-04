from src.helpers.cardinal_type import CardinalType
from src.utils.utilities       import tuple_it_if_needed, sort_keep_unique_tuple_list

import src.client.models.actions

class JoyPovData(object):
    def __init__(self, pov_index, cardinal):
        JoyPovData._check_pov_index(pov_index)
        JoyPovData._check_cardinal(cardinal)

        self.__pov_index = pov_index
        self.__cardinal  = CardinalType.retrieve_value_from(cardinal)
        self.actions     = None

    @property
    def pov_index(self):
        return self.__pov_index

    @property
    def cardinal(self):
        return self.__cardinal

    def __eq__(self, other):
        return  self.__class__ == other.__class__ and self.pov_index == other.pov_index and self.cardinal == other.cardinal

    def __hash__(self):
        return hash((self.pov_index, self.cardinal))

    def map_to(self, *actions):
        if self.cardinal is None:
            raise RuntimeError("The pov '{}' with cardinal '{}' can only be mapped after specifying a cardinal value.".format(self.pov_index, self.cardinal))

        if self.actions is not None:
            raise RuntimeError("The pov '{}' with cardinal '{}' can only be mapped once.".format(self.pov_index, self.cardinal))

        if len(actions) == 0 :
            raise ValueError("The pov '{}' with cardinal '{}' was mapped to an empty actions list.".format(self.pov_index, self.cardinal))

        modifiers_found = []

        for action in actions:
            if not isinstance(action, src.client.models.actions.ActionData):
                raise ValueError("The pov '{}' with cardinal '{}' was mapped to an action that is not an ActionData (specified: {}).".format(self.pov_index, self.cardinal))

            if action.joy_modifiers in modifiers_found:
                raise RuntimeError("The pov '{}' with cardinal '{}' was mapped with at least two actions defined on the same joystick modifiers! ( modifiers: {} )".format(self.pov_index, self.cardinal, action.joy_modifiers))

            modifiers_found.append(action.joy_modifiers)

        self.actions = actions

        return self

    def get_action_tied_to_modifiers(self, modifiers):
        for action in self.actions:
            if action.joy_modifiers == modifiers:
                return action

        return None

    @staticmethod
    def _check_pov_index(pov_index):
        if type(pov_index) is not int:
            raise ValueError("A pov index must be an int (specified: {}).".format(pov_index))

    @staticmethod
    def _check_cardinal(cardinal):
        if not CardinalType.is_value_allowed(cardinal):
            raise ValueError("The VJoy's pov cardinal is not allowed (specified: {} with type {}).".format(axis, type(axis)))

    @staticmethod
    def command_of(pov_index, cardinal, modifiers):
        JoyPovData._check_pov_index(pov_index)
        JoyPovData._check_cardinal(cardinal)

        if type(modifiers) is not int and type(modifiers) is not tuple:
            raise ValueError("You tried to retrive a joystick action reference for pov '{}' with cardinal '{}' and with modifiers that is neither an int or a tuple (specified: {}).".format(pov_index, cardinal, modifiers))

        if type(modifiers) is tuple:
            for modifier in modifiers:
                if type(modifier) is not int:
                    raise ValueError("You cannot retrieve a joystick pov reference for pov {} and cardinal {} with a modifier that is different than an int (specified: {})".format(pov_index, cardinal, modifier))

        return JoyPovCardinalRef(pov_index, CardinalType.retrieve_value_from(cardinal), sort_keep_unique_tuple_list(tuple_it_if_needed(modifiers)))

class JoyPovCardinalRef(object):
    def __init__(self, pov_index, cardinal, modifiers):
        self.pov_index = pov_index
        self.cardinal  = cardinal
        self.modifiers = modifiers