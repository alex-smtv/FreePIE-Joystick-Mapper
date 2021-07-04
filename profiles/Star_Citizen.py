from src.client.client_interface import joy, vjoy, action, threshold, sequence, transfer, Filter
from src.helpers.freepie_vars    import FreePieVars

def x52_pro_mapping():
    ### Joystick Builder Settings
    joy_name     = "X52 Professional H.O.T.A.S."
    joy_axis_max = 1000

    x52_pro = joy(joy_name, joy_axis_max)

    ### Modifiers Vars
    pinkie_modifier1 = 5
    clutch_modifier2 = 30

    ### For reference only

    # x52_pro.button(0).map_to(

    #     action(

    #         label = "", speech_text = "",

    #         joy_modifiers = (),
    #         command = 'Space',
    #         copy_commands = x52_pro.button(2).command_of(modifiers = ())
    #     )

    # )

    # x52_pro.pov(0).cardinal('S').map_to(...)

    # Commands:
    # vjoy(0).button(0)
    # vjoy(0).pov(0).cardinal('N')
    # sequence.rotate(False).create( vjoy(0).button(29), vjoy(0).button(30))

    # Copy commands:
    # copy_commands  = (
    #     x52_pro.button(2).command_of(modifiers = ()),
    #     x52_pro.pov(0).cardinal('N').command_of(modifiers = modifier1)
    # )



    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  Mapping - Buttons                                                         |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   HAND ON STICK - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / BTN 0 ]~~>>   | Trigger | Index | First CLICK |
    # ~~[ STICK / BTN 14 ]~~>>  | Second Trigger | Index | Second CLICK |
    # ~~[ STICK / BTN 1 ]~~>>   | Fire   | Thumb | Middle TOP |
    # ~~[ STICK / BTN 2 ]~~>>   | Fire A | Thumb | Right TOP |
    # ~~[ STICK / BTN 3 ]~~>>   | Fire B | Thumb | Right BOTTOM |
    # ~~[ STICK / BTN 4 ]~~>>   | Fire C | Thumb | Left BOTTOM |
    # ~~[ STICK / POV BTN 19 ]~~>>  | Pov 2  | Thumb | Hat UP |
    # ~~[ STICK / POV BTN 20 ]~~>>  | Pov 2  | Thumb | Hat RIGHT |
    # ~~[ STICK / POV BTN 21 ]~~>>  | Pov 2  | Thumb | Hat DOWN |
    # ~~[ STICK / POV BTN 22 ]~~>>  | Pov 2  | Thumb | Hat LEFT |
    # ~~[ STICK / BTN 5 ]~~>>   | Pinkie | Pinkie | Rest |



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  STICK SWITCHES - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / SWITCH BTN 8 ]~~>>   | Toggle 1 | Left   | UP   |
    # ~~[ STICK / SWITCH BTN 9 ]~~>>   | Toggle 2 | Left   | DOWN |
    # ~~[ STICK / SWITCH BTN 10 ]~~>>  | Toggle 3 | Middle | UP   |
    # ~~[ STICK / SWITCH BTN 11 ]~~>>  | Toggle 4 | Middle | DOWN |
    # ~~[ STICK / SWITCH BTN 12 ]~~>>  | Toggle 5 | Right  | UP   |
    # ~~[ STICK / SWITCH BTN 13 ]~~>>  | Toggle 6 | Right  | DOWN |



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  HAND ON THROTTLE - BUTTONS < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # ~~[ THROTTLE / WHEEL BTN 18 ]~~>>  | Right Mouse Button | Middle | Wheel CLICK       |
    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>  | Scroll Up          | Middle | Wheel Scroll UP   |
    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>  | Scroll Down        | Middle | Wheel Scroll DOWN |
    # ~~[ THROTTLE / POV BTN 25 ]~~>>  | Throttle Hat | Index | Hat UP
    # ~~[ THROTTLE / POV BTN 24 ]~~>>  | Throttle Hat | Index | Hat RIGHT
    # ~~[ THROTTLE / POV BTN 23 ]~~>>  | Throttle Hat | Index | Hat DOWN
    # ~~[ THROTTLE / POV BTN 26 ]~~>>  | Throttle Hat | Index | Hat LEFT
    # ~~[ THROTTLE / BTN 7 ]~~>>   | Fire E | Thumb  | Right TOP
    # ~~[ THROTTLE / BTN 6 ]~~>>   | Fire D | Thumb  | Right MIDDLE
    # ~~[ THROTTLE / BTN 30 ]~~>>  | Clutch | Thumb  | Right BOTTOM

    # ~~[ THROTTLE / BTN 15 ]~~>>  | Left Mouse Button | Thumb | Deep BOTTOM
    x52_pro.button(15).map_to(

        action(

            label = "OpenTrack Recenter",

            joy_modifiers = (),
            command = vjoy(4).button(0)
        ),

        action(

            label = "OpenTrack Freeze",

            joy_modifiers = (pinkie_modifier1),
            command = vjoy(4).button(1)
        )

    )



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >    THROTTLE - MFD BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>   | Left Wheel  | CLICK
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>   | Left Wheel  | Scroll UP
    # ~~[ THROTTLE / MFD BTN 35 ]~~>>   | Left Wheel  | Scroll DOWN
    # ~~[ THROTTLE / MFD BTN 32 ]~~>>   | Middle      | Button ABOVE
    # ~~[ THROTTLE / MFD BTN 33 ]~~>>   | Middle      | Button BELOW
    # ~~[ THROTTLE / MFD BTN 38 ]~~>>   | Right Wheel | CLICK
    # ~~[ THROTTLE / MFD BTN 36 ]~~>>   | Right Wheel | Scroll UP
    # ~~[ THROTTLE / MFD BTN 37 ]~~>>   | Right Wheel | Scroll DOWN




    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  Mapping - POVs                                                            |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >        STICK - POVS         < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / POV 0 | N ]~~    | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | NE ]~~   | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | E ]~~    | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | SE ]~~   | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | S ]~~    | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | SW ]~~   | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | W ]~~    | Pov 1 | Thumb | Middle BOTTOM
    # ~~[ STICK / POV 0 | NW ]~~   | Pov 1 | Thumb | Middle BOTTOM




    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  Mapping - Axes                                                            |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >           AXES              < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #deadzone_minimum = 2.3
    deadzone_minimum = 0

    linear_curve_dz = Filter.Curve(

        max_value    = joy_axis_max,
        deadzone     = deadzone_minimum,
        saturation_x = 100,
        saturation_y = 100,
        curvature    = 0

    )

    # ~~[ STICK / AXIS X ]~~
    x52_pro.axis('x').map_to(

        vjoy(0).axis('x').filtered_with(

            curve_filters = (
                linear_curve_dz
            )

        )

    )

    # ~~[ STICK / AXIS Y ]~~
    x52_pro.axis('y').map_to(

        vjoy(0).axis('y').filtered_with(

            curve_filters = (
                linear_curve_dz
            )

        )

    )

    # ~~[ STICK / AXIS RZ ]~~
    x52_pro.axis('rz').map_to(

        vjoy(0).axis('rz').filtered_with(

            curve_filters = (
                linear_curve_dz
            )

        )

    )

    # ~~[ THROTTLE / AXIS Z ]~~
    x52_pro.axis('z').map_to(

        vjoy(0).axis('z')

    )

    # ~~[ THROTTLE / AXIS RX ]~~
    x52_pro.axis('rx').map_to(

        vjoy(0).axis('rx')

    )

    # ~~[ THROTTLE / AXIS RY ]~~
    x52_pro.axis('ry').map_to(

        vjoy(0).axis('ry')

    )

    # ~~[ THROTTLE / AXIS SLIDER ]~~
    x52_pro.axis('slider1').map_to(

        vjoy(0).axis('slider1').filtered_with(

            invert = True,

            curve_filters = (
                Filter.Kalman(process_noise = 0.001, sensor_noise = 10000000, estimated_error = 100, radius = 0.04 * joy_axis_max, delay_radius_count = 17),
                #Filter.LowPass(smoothing_factor = 0.000001, radius = 0.035 * joy_axis_max),
                Filter.MinMax(-joy_axis_max, 1 * joy_axis_max)
            )

        )

    )

    return x52_pro

def custom_code_in_loop():
    pass