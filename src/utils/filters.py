from abc import ABCMeta, abstractmethod

# class CurveFilter:

#     # https://forums.x-plane.org/index.php?/forums/topic/126435-joystick-steering-one-solution-to-fix-current-handling-issues/
#     # a: 0 is linear, 1 is max flat at center
#     @staticmethod
#     def center_flattening(x, range, a=0.99):
#         x = (x*1.0)/range
#         return (a*x*x*x + (1.0-a)*x)*range

# class CenterFlatteningFilter:

#     def __init__(self, range, a):
#         self.range = range
#         self.a = a

#     def apply_filter(self, new_value):
#         return CurveFilter.center_flattening(new_value, self.range, self.a)

class IFilter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_filter(self, new_value):
        pass

class CurveFilter(IFilter):

    # value as percent
    def __init__(self, max_value, deadzone, saturation_x, saturation_y, curvature):
        self.max_value    = 1.0*max_value

        self.deadzone_pos = self.max_value * (1.0*deadzone)/100
        self.deadzone_neg = -self.deadzone_pos

        self.saturation_x_pos = self.max_value * (1.0*saturation_x/100)
        self.saturation_x_neg = -self.saturation_x_pos

        self.saturation_y      = self.max_value * (1.0*saturation_y/100)
        self.saturation_y_neg  = -self.saturation_y

        self.curvature     = (1.0*curvature)/100
        self.curvature_abs = -self.curvature if self.curvature < 0 else self.curvature

        self.is_curvature_pos = True if self.curvature >= 0 else False

        self.diff_satx_deadzone   = self.saturation_x_pos - self.deadzone_pos
        self.diff_1_curvature_abs = 1 - self.curvature_abs

    def apply_filter(self, new_value):
        if new_value > 0:
            if new_value <= self.deadzone_pos:
                return 0
            elif new_value >= self.saturation_x_pos:
                return self.saturation_y
            else:
                # func
                if self.is_curvature_pos:
                    # e1
                    x = (new_value - self.deadzone_pos)/self.diff_satx_deadzone

                    return self.saturation_y * (self.curvature * x*x*x + self.diff_1_curvature_abs * x)

                else:
                    # n1
                    x = -1 + (new_value - self.deadzone_pos)/self.diff_satx_deadzone

                    return self.saturation_y * (1 + self.curvature_abs * x*x*x + self.diff_1_curvature_abs * x)

        elif new_value < 0:
            if new_value >= self.deadzone_neg:
                return 0
            elif new_value <= self.saturation_x_neg:
                return self.saturation_y_neg
            else:
                # func
                if self.is_curvature_pos:
                    # e2
                    x = (new_value + self.deadzone_pos)/self.diff_satx_deadzone

                    return self.saturation_y * (self.curvature * x*x*x + self.diff_1_curvature_abs * x)

                else:
                    # n2
                    x = 1 + (new_value + self.deadzone_pos)/self.diff_satx_deadzone

                    return self.saturation_y * (-1 + self.curvature_abs * x*x*x + self.diff_1_curvature_abs * x)

        else:
            return 0

# TODO
# only specify deadzone and saturation
class LinearFilter(IFilter):
    pass

# TODO
class StairsFilter(IFilter):
    pass

class MinMaxFilter(IFilter):

    def __init__(self, max_lower_value, max_upper_value):
        self.max_lower_value = max_lower_value
        self.max_upper_value = max_upper_value

    def apply_filter(self, new_value):
        if new_value < self.max_lower_value:
            return self.max_lower_value

        elif new_value > self.max_upper_value:
            return self.max_upper_value

        else:
            return new_value

# https://helpful.knobs-dials.com/index.php/Low-pass_filter
class LowPassFilter(IFilter):
    def __init__(self, smoothing_factor, radius = None):
        self.a = 1.0 * smoothing_factor
        self.threshold = radius
        self.prev_output = 0

    def apply_filter(self, new_value):

        diff = new_value - self.prev_output

        if self.threshold is not None and abs(diff) > self.threshold:
            self.prev_output = new_value
            return new_value

        else:
            #curr_output = self.a * new_value + (1-self.a) * self.prev_output

            curr_output = self.prev_output + self.a * diff
            self.prev_output = curr_output

            return curr_output

# class LowPassFilterOld(IFilter):

#     def __init__(self, jitters_threshold = 0.04 * 1000, filter_smoothing = 2000.0):
#         self.axis_previous_value = None
#         self.jitters_threshold = jitters_threshold
#         self.filter_smoothing = filter_smoothing

#     #http://phrogz.net/js/framerate-independent-low-pass-filter.html
#     #filteredValue = oldValue + (newValue - oldValue) / (smoothing / timeSinceLastUpdate)
#     def apply_filter(self, new_value):

#         # First iterration
#         if self.axis_previous_value is None:
#             self.axis_previous_value = new_value
#             return new_value

#         diff = abs(self.axis_previous_value - new_value)

#         #If we are making greater movement, reset the queue and leave the filter algorithm
#         if diff >= self.jitters_threshold:
#             self.axis_previous_value = new_value
#             return new_value

#         else:

#             #filtered_value = lw_previous_axis_value + (axis_value - lw_previous_axis_value) / self.filter_smoothing.value
#             filtered_value = 1.0 * self.axis_previous_value + (new_value - self.axis_previous_value) / self.filter_smoothing

#             # smoothed += elapsedTime * ( newValue - smoothed ) / smoothing;
#             #filtered_value = elapsedTime * (axis_value - lw_previous_axis_value) / 2.0

#             self.axis_previous_value = filtered_value

#             return filtered_value

# https://web.archive.org/web/20180115165644/http://interactive-matter.eu/blog/2009/12/18/filtering-sensor-data-with-a-kalman-filter/
# https://github.com/bachagas/Kalman
class KalmanFilter(IFilter):
    def __init__(self, process_noise, sensor_noise, estimated_error, radius = None, delay_radius_count = 1):
        """
            The variables are x for the filtered value, q for the process noise,
            r for the sensor noise, p for the estimated error and k for the Kalman Gain.
            The state of the filter is defined by the values of these variables.

            The initial values for p is not very important since it is adjusted
            during the process. It must be just high enough to narrow down.
            The initial value for the readout is also not very important, since
            it is updated during the process.
            But tweaking the values for the process noise and sensor noise
            is essential to get clear readouts.

            For large noise reduction, you can try to start from: (see http://interactive-matter.eu/blog/2009/12/18/filtering-sensor-data-with-a-kalman-filter/ )
            q = 0.125
            r = 32
            p = 1023 //"large enough to narrow down"
            e.g.
            myVar = Kalman(0.125,32,1023,0);

            q; //process noise covariance
            r; //measurement noise covariance
            x; //value
            p; //estimation error covariance
            k; //kalman gain
        """
        self.q = 1.0 * process_noise   # process noise covariance
        self.r = 1.0 * sensor_noise    # measurement noise covariance
        self.p = 1.0 * estimated_error # estimation error covariance
        self.x = None                  # x will hold the iterated filtered value
        self.threshold = radius
        self.delay_count = delay_radius_count
        self.counter = self.delay_count
        self.threshold_reached = False

        if self.threshold is not None:
            # duplicate value to get a reference to initial condition once we move out of the threshold
            self.p_orig = self.p

    def apply_filter(self, new_value):

        if self.x is None:
                self.x = new_value
                return new_value
        else:
            diff = new_value - self.x

            if self.threshold is not None and abs(diff) > self.threshold:
                    self.threshold_reached = True
                    self.p = self.p_orig
                    self.x = new_value
                    return new_value

            else:
                if self.threshold_reached:
                    if self.counter == 0:
                        self.threshold_reached = False
                        self.counter = self.delay_count

                    else:
                        self.counter -= 1
                        self.x = new_value
                        return new_value

                if not self.threshold_reached:
                    # prediction update
                    self.p = self.p + self.q

                    # measurement update
                    k = self.p / (self.p + self.r)
                    self.x = self.x + k * (new_value - self.x)
                    self.p = (1 - k) * self.p

                    return self.x

class Filter(object):
    Curve   = CurveFilter
    MinMax  = MinMaxFilter
    LowPass = LowPassFilter
    Kalman  = KalmanFilter