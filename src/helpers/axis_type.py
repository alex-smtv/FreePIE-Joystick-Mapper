class AxisType:
    X       = 0
    Y       = 1
    Z       = 2
    RX      = 3
    RY      = 4
    RZ      = 5
    SLIDER1 = 6
    SLIDER2 = 7

    ALLOWED_VALUES = {
        "X"      : X,
        "Y"      : Y,
        "Z"      : Z,
        "RX"     : RX,
        "RY"     : RY,
        "RZ"     : RZ,
        "SLIDER1": SLIDER1,
        "SLIDER2": SLIDER2,
    }

    @staticmethod
    def is_value_allowed(value):
        if type(value) is not str and type(value) is not int:
            return False

        if type(value) is str:
            value = value.upper()

        found = False

        for allowed_value in AxisType.ALLOWED_VALUES:
            if type(value) is str:
                found = (value == allowed_value)

            elif type(value) is int:
                found = (value == AxisType.ALLOWED_VALUES[allowed_value])

            if found:
                break

        return found

    @staticmethod
    def retrieve_value_from(axis):
        if AxisType.is_value_allowed(axis):

            if type(axis) is str:
                return AxisType.ALLOWED_VALUES[axis.upper()]
            elif type(axis) is int:
                return axis
            else:
                raise RuntimeError("Axis edge case: the value {} could not be retrieved.".format(axis))

        else:
            raise ValueError("The axis {} could not be validated.".format(axis))

    @staticmethod
    def joy_axis_getter(joy, axis_type):
        _JOY_GETTER = [
            lambda: joy.x,
            lambda: joy.y,
            lambda: joy.z,
            lambda: joy.xRotation,
            lambda: joy.yRotation,
            lambda: joy.zRotation,
            lambda: joy.sliders[0],
            lambda: joy.sliders[1]
        ]

        return _JOY_GETTER[axis_type]

    @staticmethod
    def vjoy_axis_getter(vjoy, axis_type):
        _VJOY_GETTER = [
            lambda: vjoy.x     ,
            lambda: vjoy.y     ,
            lambda: vjoy.z     ,
            lambda: vjoy.rx    ,
            lambda: vjoy.ry    ,
            lambda: vjoy.rz    ,
            lambda: vjoy.slider,
            lambda: vjoy.dial
        ]

        return _VJOY_GETTER[axis_type]

    @staticmethod
    def vjoy_axis_setter(vjoy, axis_type):
        _VJOY_SETTER = [
            lambda val: setattr(vjoy, 'x',      val),
            lambda val: setattr(vjoy, 'y',      val),
            lambda val: setattr(vjoy, 'z',      val),
            lambda val: setattr(vjoy, 'rx',     val),
            lambda val: setattr(vjoy, 'ry',     val),
            lambda val: setattr(vjoy, 'rz',     val),
            lambda val: setattr(vjoy, 'slider', val),
            lambda val: setattr(vjoy, 'dial',   val)
        ]

        return _VJOY_SETTER[axis_type]