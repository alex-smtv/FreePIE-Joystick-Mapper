from src.helpers.axis_type     import AxisType
from src.helpers.cardinal_type import CardinalType
from src.utils.filters         import IFilter
from src.utils.utilities       import Bunch, tuple_it_if_needed

import src.client.models.actions

class VJoyIndexRefManager(object):
    _KNOWN_REF = {}

    @staticmethod
    def get_at_index(index):
        if index not in VJoyIndexRefManager._KNOWN_REF:
            VJoyIndexRefManager._KNOWN_REF[index] = VJoyIndexRef(index)

        return VJoyIndexRefManager._KNOWN_REF[index]

class VJoyIndexRef(object):
    def __init__(self, vjoy_index):
        if type(vjoy_index) is not int:
            raise ValueError("A VJoy's index must be an int (specified: {}).".format(type(vjoy_index)))

        self.vjoy_index = vjoy_index

    def button(self, button):
        if type(button) is not int:
            raise ValueError("A VJoy's button must be an int (specified: {}).".format(type(button)))

        return VJoyBtnRef(self.vjoy_index, button)

    def pov(self, pov_index):
        #return VJoyPovData(self.vjoy_index, pov_index)
        return Bunch(
            cardinal = lambda value: self.pov_cardinal(pov_index, value)
        )

    def pov_cardinal(self, pov_index, cardinal_val):
        if not isinstance(pov_index, int):
            raise ValueError("A VJoy's pov index must be an int (specified: {}).".format(pov_index))

        if not CardinalType.is_value_allowed(cardinal_val):
            raise ValueError("The VJoy's pov cardinal is not allowed (specified: {} with type {}).".format(axis, type(axis)))

        return VJoyPovCardinalRef(self.vjoy_index, pov_index, cardinal_val)

    def axis(self, axis):
        if not AxisType.is_value_allowed(axis):
            raise ValueError("The VJoy's axis is not allowed (specified: {} with type {}).".format(axis, type(axis)))

        return VJoyAxisRef(self.vjoy_index, axis)

class VJoyBtnRef(object):
    def __init__(self, vjoy_index, button):
        self.vjoy_index = vjoy_index
        self.button     = button

# class VJoyPovData(object):
#     def __init__(self, vjoy_index, pov_index):
#         self.vjoy_index = vjoy_index

#         if type(vjoy_index) is not int:
#             raise ValueError("A VJoy's index must be an int (specified: {}).".format(type(vjoy_index)))

#         if type(pov_index) is not int:
#             raise ValueError("A VJoy's pov index must be an int (specified: {}).".format(pov_index))

#         self.pov_index    = pov_index

#     def cardinal(self, value):
#         if not CardinalType.is_value_allowed(value):
#             raise ValueError("The VJoy's pov cardinal is not allowed (specified: {} with type {}).".format(axis, type(axis)))

#         return VJoyPovCardinalRef(self.vjoy_index, self.pov_index, value)

class VJoyPovCardinalRef(object):
    def __init__(self, vjoy_index, pov_index, cardinal):
        self.vjoy_index = vjoy_index
        self.pov_index  = pov_index
        self.cardinal   = cardinal

class VJoyAxisRef(object):
    def __init__(self, vjoy_index, axis):

        if type(vjoy_index) is not int:
            raise ValueError("A vjoy index must be an int (specified: {}).".format(pov_index))

        if not AxisType.is_value_allowed(axis):
            raise ValueError("The axis specified in vjoy could not be validated (specified: type={}, val={}).".format(type(axis), axis))

        self.vjoy_index         = vjoy_index
        self.axis               = AxisType.retrieve_value_from(axis)
        self.transfer_range     = None
        self.invert             = None
        self.curve_filters      = None
        self.threshold_actions  = None

    def filtered_with(
        self,
        range_of_transfer = None,
        invert            = False,
        curve_filters     = None,
        threshold_actions = None
        ):

        if range_of_transfer is not None and not isinstance(range_of_transfer, TransferRange):
            raise ValueError("The vjoy axis ref 'range_of_transfer' was not a 'TransferRange' (specified: {}).".format(type(range_of_transfer)))

        if not isinstance(invert, bool):
            raise ValueError("The vjoy axis ref 'invert' was not a bool (specified: {}).".format(type(invert)))

        if curve_filters is not None:
            curve_filters = tuple_it_if_needed(curve_filters)

            for curve_filter in curve_filters:
                if not isinstance(curve_filter, IFilter):
                    raise ValueError("The vjoy axis ref 'curve_filters' contain a filter which is not a IFilter (specified: {}).".format(type(curve_filter)))

        if threshold_actions is not None:
            threshold_actions = tuple_it_if_needed(threshold_actions)

            for threshold_action in threshold_actions:
                if not isinstance(threshold_action, src.client.models.actions.ThresholdActionData):
                    raise ValueError("The vjoy axis ref 'threshold_actions' contain an action which is not a ThresholdActionData (specified: {}).".format(type(threshold_action)))

        self.transfer_range    = range_of_transfer
        self.invert            = invert
        self.curve_filters     = curve_filters
        self.threshold_actions = threshold_actions

        return self

class TransferRange(object):
    def __init__(self):
        self.joy_min  = None
        self.joy_max  = None

        self.vjoy_min = None
        self.vjoy_max = None

    def from_joy(self, joy_min_percent, joy_max_percent):
        if type(joy_min_percent) is not int and type(joy_min_percent) is not float:
            raise ValueError("The joystick minimum transfer range must be either an int or float.")

        if type(joy_max_percent) is not int and type(joy_max_percent) is not float:
            raise ValueError("The joystick maximum transfer range must be either an int or float.")

        if joy_min_percent < -100:
            raise ValueError("The joystick minimum transfer must not go below -100 (specified: {}).".format(joy_min_percent))

        if joy_max_percent > 100:
            raise ValueError("The joystick maximum transfer must not go above 100 (specified: {}).".format(joy_min_percent))

        if joy_min_percent >= joy_max_percent:
            raise ValueError("The joystick minimum transfer must be lower than the maximum transfer (specified minimum: {}, specified maximum: {}).".format(joy_min_percent, joy_max_percent))

        self.joy_min = joy_min_percent
        self.joy_max = joy_max_percent

        return self

    def to_vjoy(self, vjoy_min_percent, vjoy_max_percent):

        if self.joy_min is None or self.joy_max is None:
            raise RuntimeError("You must set the joystick minimum and maximum range before setting the transfer range for the vjoy.")

        if type(vjoy_min_percent) is not int and type(vjoy_min_percent) is not float:
            raise ValueError("The virtual joystick minimum transfer range must be either an int or float.")

        if type(vjoy_max_percent) is not int and type(vjoy_max_percent) is not float:
            raise ValueError("The virtual joystick maximum transfer range must be either an int or float.")

        if vjoy_min_percent < -100:
            raise ValueError("The virtual joystick minimum transfer must not go below -100 (specified: {}).".format(vjoy_min_percent))

        if vjoy_max_percent > 100:
            raise ValueError("The virtual joystick maximum transfer must not go above 100 (specified: {}).".format(vjoy_max_percent))

        if vjoy_min_percent >= vjoy_max_percent:
            raise ValueError("The virtual joystick minimum transfer must be lower than the maximum transfer (specified minimum: {}, specified maximum: {}).".format(vjoy_min_percent, vjoy_max_percent))

        self.vjoy_min = vjoy_min_percent
        self.vjoy_max = vjoy_max_percent

        return self
