from src.helpers.axis_type import AxisType
from src.utils.utilities   import tuple_it_if_needed

import src.client.models.vjoy
from src.helpers.freepie_vars import FreePieVars

class JoyAxisData(object):
    def __init__(self, axis):
        if not AxisType.is_value_allowed(axis):
            raise ValueError("The axis specified for joy could not be validated (specified: type={}, val={}).".format(type(axis), axis))

        self.__axis          = AxisType.retrieve_value_from(axis)
        self.vjoys_axes_refs = None

    @property
    def axis(self):
        return self.__axis

    def __eq__(self, other):
        return  self.__class__ == other.__class__ and self.axis == other.axis

    def __hash__(self):
        return hash((self.axis,))

    def map_to(self, *vjoys_axes_refs):
        if vjoys_axes_refs is None:
            raise ValueError("The joystick axis '{}' was mapped to None!.")

        if self.vjoys_axes_refs is not None:
            raise RuntimeError("The joystick axis '{}' can only be mapped once.".format(self.axis))

        if len(vjoys_axes_refs) == 0 :
            raise ValueError("The joystick axis {} was mapped to an empty list.".format(self.axis))

        for vjoy_axis_ref in vjoys_axes_refs:
            if not isinstance(vjoy_axis_ref, src.client.models.vjoy.VJoyAxisRef):
                raise ValueError("The joystick axis {} was mapped to a vjoy axis that is not an VJoyAxisRef (specified: type={}, val={}).".format(self.axis, type(vjoy_axis_ref), vjoy_axis_ref))

        self.vjoys_axes_refs = vjoys_axes_refs

        return self
