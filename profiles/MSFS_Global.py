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
    x52_pro.button(0).map_to(

        action(

            label = "Cockpit View Upper",

            joy_modifiers = (),
            command       = 'Space'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>  | Second Trigger | Index | Second CLICK |
    # ~~[ STICK / BTN 1 ]~~>>   | Fire   | Thumb | Middle TOP |
    # ~~[ STICK / BTN 2 ]~~>>   | Fire A | Thumb | Right TOP |

    # ~~[ STICK / BTN 3 ]~~>>   | Fire B | Thumb | Right BOTTOM |
    x52_pro.button(3).map_to(

        action(

            label = "Reset View",

            joy_modifiers = (),
            command       = 'Left Control + Space'

        )

    )

    # ~~[ STICK / BTN 4 ]~~>>   | Fire C | Thumb | Left BOTTOM |
    x52_pro.button(4).map_to(

        action(

            label = "Toggle Tail Wheel Lock",

            joy_modifiers = (),
            command       = 'Left Shift + G'

        )

    )

    # ~~[ STICK / POV BTN 19 ]~~>>  | Pov 2  | Thumb | Hat UP |
    x52_pro.button(19).map_to(

        action(

            label = "Elevator Trim UP", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Num 1'

        ),

        action(

            label = "Decrease Flaps",

            joy_modifiers = (pinkie_modifier1),
            command       = 'F6'

        )

    )

    # ~~[ STICK / POV BTN 20 ]~~>>  | Pov 2  | Thumb | Hat RIGHT |
    x52_pro.button(20).map_to(

        action(

            label = "Rudder Trim Right", # Rudder Trim RIGHT

            joy_modifiers = (),
            command       = 'Left Control + Enter' # not a default shortcut!

        ),

        action(

            label = "Aileron Trim Right", # Ailreon Trim RIGHT WING DOWN

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Control + Num 6'

        )

    )

    # ~~[ STICK / POV BTN 21 ]~~>>  | Pov 2  | Thumb | Hat DOWN |
    x52_pro.button(21).map_to(

        action(

            label = "Elevator Trim DOWN", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Num 7'

        ),

        action(

            label = "Increase Flaps",

            joy_modifiers = (pinkie_modifier1),
            command       = 'F7'

        )

    )

    # ~~[ STICK / POV BTN 22 ]~~>>  | Pov 2  | Thumb | Hat LEFT |
    x52_pro.button(22).map_to(

        action(

            label = "Rudder Trim Left", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Left Control + Num 0' # not a default shortcut!

        ),

        action(

            label = "Aileron Trim Left", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Control + Num 4'

        )

    )

    # ~~[ STICK / BTN 5 ]~~>>   | Pinkie | Pinkie | Rest |



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  STICK SWITCHES - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / SWITCH BTN 8 ]~~>>   | Toggle 1 | Left   | UP   |
    x52_pro.button(8).map_to(

        action(

            label = "Display ATC",

            joy_modifiers = (),
            command       = 'Scroll Lock'

        )

    )

    # ~~[ STICK / SWITCH BTN 9 ]~~>>   | Toggle 2 | Left   | DOWN |
    x52_pro.button(9).map_to(

        action(

            label = "Display NavLog",

            joy_modifiers = (),
            command       = 'N'

        )

    )

    # ~~[ STICK / SWITCH BTN 10 ]~~>>  | Toggle 3 | Middle | UP   |
    # ~~[ STICK / SWITCH BTN 11 ]~~>>  | Toggle 4 | Middle | DOWN |
    # ~~[ STICK / SWITCH BTN 12 ]~~>>  | Toggle 5 | Right  | UP   |
    # ~~[ STICK / SWITCH BTN 13 ]~~>>  | Toggle 6 | Right  | DOWN |



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  HAND ON THROTTLE - BUTTONS < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # ~~[ THROTTLE / WHEEL BTN 18 ]~~>>  | Right Mouse Button | Middle | Wheel CLICK       |

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>  | Scroll Up          | Middle | Wheel Scroll UP   |
    x52_pro.button(16).map_to(

        action(

            label = "Zoom",

            joy_modifiers = (),
            command       = sequence.rotate(False).create(
                '='
            )

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>  | Scroll Down        | Middle | Wheel Scroll DOWN |
    x52_pro.button(17).map_to(

        action(

            label = "Dezoom",

            joy_modifiers = (),
            command       = sequence.rotate(False).create(
                '-'
            )

        )

    )

    # ~~[ THROTTLE / POV BTN 25 ]~~>>  | Throttle Hat | Index | Hat UP
    x52_pro.button(25).map_to(

        action(

            label = "Zoom",

            joy_modifiers = (),
            command       = '='

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>  | Throttle Hat | Index | Hat RIGHT

    # ~~[ THROTTLE / POV BTN 23 ]~~>>  | Throttle Hat | Index | Hat DOWN
    x52_pro.button(23).map_to(

        action(

            label = "Dezoom",

            joy_modifiers = (),
            command       = '-'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>  | Throttle Hat | Index | Hat LEFT

    # ~~[ THROTTLE / BTN 7 ]~~>>   | Fire E | Thumb  | Right TOP
    x52_pro.button(7).map_to(

        action(

            label = "Brakes",

            joy_modifiers = (),
            command       = 'Num .'

        ),

        action(

            label = "Left Brake",

            joy_modifiers = (clutch_modifier2),
            command       = 'Num *'

        ),

        action(

            label = "Right Brake",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Num -'

        )

    )

    # ~~[ THROTTLE / BTN 6 ]~~>>   | Fire D | Thumb  | Right MIDDLE
    x52_pro.button(6).map_to(

        action(

            label = "Toggle Throttle Reverse Thrust",

            joy_modifiers = (),
            command       = 'I' # NOT A DEFAULT BIND

        ),

        action(

            label = "Toggle Propeller Reverse Thrust",

            joy_modifiers = (pinkie_modifier1),
            command       = 'U' # NOT A DEFAULT BIND

        )

    )

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
        ),

        action(

            label = "Discord Mute",

            joy_modifiers = (clutch_modifier2),
            command = 'Right Control + Right Shift + End'
        )

    )



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >    THROTTLE - MFD BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>   | Left Wheel  | CLICK
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>   | Left Wheel  | Scroll UP
    # ~~[ THROTTLE / MFD BTN 35 ]~~>>   | Left Wheel  | Scroll DOWN

    # ~~[ THROTTLE / MFD BTN 32 ]~~>>   | Middle      | Button ABOVE
    x52_pro.button(32).map_to(

        action(

            label = "Toggle Spoilers",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Num /'

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>   | Middle      | Button BELOW
    x52_pro.button(33).map_to(

        action(

            label = "Toggle Landing Gear", speech_text="Landing Gear",

            joy_modifiers = (),
            command       = 'G'

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>   | Right Wheel | CLICK
    x52_pro.button(38).map_to(

        action(

            label = "Toggle Parking Brakes",

            joy_modifiers = (),
            command       = 'Left Control + Num .'

        )

    )

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>   | Right Wheel | Scroll UP
    x52_pro.button(36).map_to(

        action(

            label = "Auto Start Engine",

            joy_modifiers = (),
            command       = 'Left Control + E'

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>   | Right Wheel | Scroll DOWN
    x52_pro.button(37).map_to(

        action(

            label = "Engine Autostop",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Shift + Left Control + E'

        )

    )



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

        vjoy(0).axis('rx').filtered_with(

            invert = True

        )

    )

    # ~~[ THROTTLE / AXIS RY ]~~
    x52_pro.axis('ry').map_to(

        vjoy(0).axis('ry').filtered_with(

            invert = True

        )

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