from src.helpers.axis_type import AxisType
from src.utils.utilities   import tuple_it_if_needed, convert_val_joy_to_vjoy, scale_val

class TransferRange:
    def __init__(self,
                 joy_min_percent,
                 joy_max_percent,
                 vjoy_min_percent,
                 vjoy_max_percent,
                 joy_axis_max,
                 vjoy_axis_max
        ):
        self.joy_min_raw = 1.0 * joy_min_percent * joy_axis_max / 100
        self.joy_max_raw = 1.0 * joy_max_percent * joy_axis_max / 100

        self.vjoy_min_raw = 1.0 * vjoy_min_percent * vjoy_axis_max / 100
        self.vjoy_max_raw = 1.0 * vjoy_max_percent * vjoy_axis_max / 100

    def does_joy_value_fit(self, value):
        return value >= self.joy_min_raw and value <= self.joy_max_raw

    def scale_value(self, value):
        return scale_val(value, self.joy_min_raw, self.joy_max_raw, self.vjoy_min_raw, self.vjoy_max_raw)

class AxisFilter:
    def __init__(self, curve_filters = (), invert = False):
        self.curve_filters  = tuple_it_if_needed(curve_filters)
        self.invert         = invert

    def value_filtered(self, val):
        if self.invert:
            val = -val

        for curve_filter in self.curve_filters:
            val = curve_filter.apply_filter(val)

        return val

class JoyAxisTransfer:
    def __init__(self, joy, joy_axis_max, axis_type, vjoy_axis_transfers):
        self.joy                 = joy
        self.joy_axis_max        = joy_axis_max
        self.axis_getter         = AxisType.joy_axis_getter(joy, axis_type)
        self.vjoy_axis_transfers = tuple_it_if_needed(vjoy_axis_transfers)

    def transfer(self):
        joy_val = self.axis_getter()

        for vjoy_axis_transfer in self.vjoy_axis_transfers:
            if vjoy_axis_transfer.has_filter:
                val = vjoy_axis_transfer.filter.value_filtered(joy_val)
            else:
                val = joy_val

            if vjoy_axis_transfer.is_custom_range:
                if not vjoy_axis_transfer.transfer_range.does_joy_value_fit(joy_val):
                    return
                else:
                    val = vjoy_axis_transfer.transfer_range.scale_value(val)

            else:
                val = convert_val_joy_to_vjoy(val, self.joy_axis_max, vjoy_axis_transfer.vjoy_axis_manager.axisMax)

            vjoy_axis_transfer.vjoy_axis_manager.apply_value(val)

class VJoyAxisTransfer:
    def __init__(self, vjoy_axis_manager, axis_filter = None, transfer_range = None):
        self.vjoy_axis_manager = vjoy_axis_manager
        self.filter            = axis_filter
        self.transfer_range    = transfer_range

        self.has_filter        = axis_filter is not None
        self.is_custom_range   = transfer_range is not None

class VJoyAxisManager:
    def __init__(self, vjoy, axis_type):
        self.axis_getter = AxisType.vjoy_axis_getter(vjoy, axis_type)
        self.axis_setter = AxisType.vjoy_axis_setter(vjoy, axis_type)

        self.axisMax = vjoy.axisMax

    def get_value(self):
        return self.axis_getter()

    def apply_value(self, val):
        self.axis_setter(val)