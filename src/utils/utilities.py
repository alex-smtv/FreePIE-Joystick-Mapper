from collections import Iterable

def is_iterable(obj):
    return isinstance(obj, Iterable)

# https://stackoverflow.com/a/1123026
# Simulate anonymous class: basically use a dict like it's an Object
class Bunch(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

# def guarantee_to_be_tuple(maybe_tuple):
#     return (maybe_tuple,) if type(maybe_tuple) is not tuple else maybe_tuple

def tuple_it_if_needed(maybe_tuple):
    if type(maybe_tuple) is list:
        return tuple(maybe_tuple)
    else:
        return maybe_tuple if type(maybe_tuple) is tuple else (maybe_tuple,)

def sort_keep_unique_tuple_list(given_tuple_list):
    if not isinstance(given_tuple_list, (tuple, list)):
        raise ValueError("'sort_keep_unique_tuple' got called with a parameter that is not a tuple or a list (specified: {}).".format(type(given_tuple_list)))

    return tuple(
        sorted(
            set(given_tuple_list),
            reverse = False
        )
    )

# The range of values from a joystick axis  is not the same as in a vjoy
def convert_val_joy_to_vjoy(value, joy_max_axis, vjoy_max_axis):
    return (value * vjoy_max_axis)/joy_max_axis

# Taken from FreePie, more info on:
# https://stackoverflow.com/a/5295202
# [xMin, xMax] --> [yMin, yMax]
# x = the number
def scale_val(x, xMin, xMax, yMin, yMax):
    return yMin + 1.0 *(yMax - yMin)*(x - xMin)/(xMax - xMin)