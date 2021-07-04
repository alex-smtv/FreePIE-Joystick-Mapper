from src.client.client_interface import joy, vjoy, action, threshold, sequence, transfer, Filter
from src.helpers.freepie_vars    import FreePieVars

def x52_pro_mapping():
    ### Joystick Builder Settings
    joy_name     = "X52 Professional H.O.T.A.S."
    joy_axis_max = 1000

    x52_pro = joy(joy_name, joy_axis_max)

    ### Modifiers Vars
    modifier1 = 30
    modifier2 = 6


    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  INFO: Mapping - Buttons                                                   |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   HAND ON STICK - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / BTN 0 ]~~>>   | Trigger | Index | First CLICK |
    x52_pro.button(0).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(0)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(0)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(0)

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>  | Second Trigger | Index | Second CLICK |
    x52_pro.button(14).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(14)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(14)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(14)

        )

    )

    # ~~[ STICK / BTN 1 ]~~>>   | Fire | Thumb | Middle TOP |
    x52_pro.button(1).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(1)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(1)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(1)

        )

    )

    # ~~[ STICK / BTN 2 ]~~>>   | Fire A | Thumb | Right TOP |
    x52_pro.button(2).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(2)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(2)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(2)

        )

    )

    # ~~[ STICK / BTN 3 ]~~>>   | Fire B | Thumb | Right BOTTOM |
    x52_pro.button(3).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(3)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(3)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(3)

        )

    )

    # ~~[ STICK / BTN 4 ]~~>>   | Fire C | Thumb | Left BOTTOM |
    x52_pro.button(4).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(4)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(4)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(4)

        )

    )

    # ~~[ STICK / POV BTN 19 ]~~>>  | Pov 2 | Thumb | Hat UP |
    x52_pro.button(19).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(19)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(19)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(19)

        )

    )

    # ~~[ STICK / POV BTN 20 ]~~>>  | Pov 2 | Thumb | Hat RIGHT |
    x52_pro.button(20).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(20)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(20)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(20)

        )

    )

    # ~~[ STICK / POV BTN 21 ]~~>>  | Pov 2 | Thumb | Hat DOWN |
    x52_pro.button(21).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(21)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(21)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(21)

        )

    )

    # ~~[ STICK / POV BTN 22 ]~~>>  | Pov 2 | Thumb | Hat LEFT |
    x52_pro.button(22).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(22)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(22)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(22)

        )

    )

    # ~~[ STICK / BTN 5 ]~~>>   | Pinkie | Pinkie | Rest |
    x52_pro.button(5).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(5)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(5)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(5)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  STICK SWITCHES - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / SWITCH BTN 8 ]~~>>   | Toggle 1 | Left   | UP   |
    x52_pro.button(8).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(8)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(8)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(8)

        )

    )

    # ~~[ STICK / SWITCH BTN 9 ]~~>>   | Toggle 2 | Left   | DOWN |
    x52_pro.button(9).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(9)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(9)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(9)

        )

    )

    # ~~[ STICK / SWITCH BTN 10 ]~~>>  | Toggle 3 | Middle | UP   |
    x52_pro.button(10).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(10)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(10)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(10)

        )

    )

    # ~~[ STICK / SWITCH BTN 11 ]~~>>  | Toggle 4 | Middle | DOWN |
    x52_pro.button(11).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(11)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(11)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(11)

        )

    )

    # ~~[ STICK / SWITCH BTN 12 ]~~>>  | Toggle 5 | Right  | UP   |
    x52_pro.button(12).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(12)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(12)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(12)

        )

    )

    # ~~[ STICK / SWITCH BTN 13 ]~~>>  | Toggle 6 | Right  | DOWN |
    x52_pro.button(13).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(13)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(13)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(13)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  HAND ON THROTTLE - BUTTONS < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / WHEEL BTN 18 ]~~>>  | Right Mouse Button | Middle | Wheel CLICK       |
    x52_pro.button(18).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(18)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(18)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(18)

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>  | Scroll Up          | Middle | Wheel Scroll UP   |
    x52_pro.button(16).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(16)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(16)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(16)

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>  | Scroll Down        | Middle | Wheel Scroll DOWN |
    x52_pro.button(17).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(17)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(17)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(17)

        )

    )

    # ~~[ THROTTLE / POV BTN 25 ]~~>>  | Throttle Hat | Index | Hat UP
    x52_pro.button(25).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(25)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(25)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(25)

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>  | Throttle Hat | Index | Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(24)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(24)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(24)

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>  | Throttle Hat | Index | Hat DOWN
    x52_pro.button(23).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(23)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(23)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(23)

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>  | Throttle Hat | Index | Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(26)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(26)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(26)

        )

    )

    # ~~[ THROTTLE / BTN 7 ]~~>>   | Pinkie | Pinkie | Rest |
    x52_pro.button(7).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(7)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(7)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(7)

        )

    )

    # !!! DON'T MAP, IT'S A MODIFIER !!!
    # ~~[ THROTTLE / BTN 6 ]~~>>   | Fire D | Thumb | Right MIDDLE
    # x52_pro.button(6).map_to(

    #     action(

    #         label = "",

    #         joy_modifiers = (),
    #         command = vjoy(0).button(6)

    #     ),

    #     action(

    #         label = "",

    #         joy_modifiers = (modifier1),
    #         command = vjoy(1).button(6)

    #     ),

    #     action(

    #         label = "",

    #         joy_modifiers = (modifier2),
    #         command = vjoy(2).button(6)

    #     )

    # )

    # !!! DON'T MAP, IT'S A MODIFIER !!!
    # ~~[ THROTTLE / BTN 30 ]~~>>  | Clutch | Thumb | Right BOTTOM
    # x52_pro.button(30).map_to(

    #     action(

    #         label = "",

    #         joy_modifiers = (),
    #         command = vjoy(0).button(30)

    #     ),

    #     action(

    #         label = "",

    #         joy_modifiers = (modifier1),
    #         command = vjoy(1).button(30)

    #     ),

    #     action(

    #         label = "",

    #         joy_modifiers = (modifier2),
    #         command = vjoy(2).button(30)

    #     )

    # )

    # ~~[ THROTTLE / BTN 15 ]~~>>  | Left Mouse Button | Thumb | Deep BOTTOM
    x52_pro.button(15).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(15)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(15)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(15)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >    THROTTLE - MFD BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>  | Left Wheel | CLICK
    x52_pro.button(31).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(31)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(31)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(31)

        )

    )

    # ~~[ THROTTLE / MFD BTN 34 ]~~>>   | Left Wheel | Scroll UP
    x52_pro.button(34).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(34)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(34)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(34)

        )

    )

    # ~~[ THROTTLE / MFD BTN 35 ]~~>>   | Left Wheel | Scroll DOWN
    x52_pro.button(35).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(35)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(35)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(35)

        )

    )

    # ~~[ THROTTLE / MFD BTN 32 ]~~>>   | Middle     | Button ABOVE
    x52_pro.button(32).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(32)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(32)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(32)

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>   | Middle     | Button BELOW
    x52_pro.button(33).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(33)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(33)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(33)

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>  | Right Wheel | CLICK
    x52_pro.button(38).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(38)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(38)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(38)

        )

    )

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>   | Right Wheel | Scroll UP
    x52_pro.button(36).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(36)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(36)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(36)

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>   | Right Wheel | Scroll DOWN
    x52_pro.button(37).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(37)

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(1).button(37)

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(2).button(37)

        )

    )



    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  INFO: Mapping - POVs                                                      |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >        STICK - POVS         < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / POV 0 | N ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('N').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('N')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('N')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('N')

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('NE').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('NE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('NE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('NE')

        )

    )

    # ~~[ STICK / POV 0 | E ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('E')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('E')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('E')

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('SE').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('SE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('SE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('SE')

        )

    )

    # ~~[ STICK / POV 0 | S ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('S')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('S')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('S')

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('SW').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('SW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('SW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('SW')

        )

    )

    # ~~[ STICK / POV 0 | W ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('W')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('W')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('W')

        )

    )

    # ~~[ STICK / POV 0 | NW ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('NW').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('NW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier1),
            command = vjoy(0).pov(1).cardinal('NW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier2),
            command = vjoy(0).pov(2).cardinal('NW')

        )

    )



    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
    ###|                                                                            |
    ###|  INFO: Mapping - Axis                                                      |
    ###|                                                                            |
    ###|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

    deadzone_minimum = 2.3

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
                Filter.MinMax(-joy_axis_max, 0 * joy_axis_max)
            )

        )

    )

    return x52_pro

def custom_code_in_loop():
    pass