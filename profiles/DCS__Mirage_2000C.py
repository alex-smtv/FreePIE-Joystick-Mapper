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

            label = "Weapons FIRE/Bombs Release", # Fire weapon

            joy_modifiers = (),
            command = 'Space'

        )

    )

    #
    # ~~[ STICK / BTN 14 ]~~>>  | Second Trigger | Index | Second CLICK |
    # ~~[ STICK / BTN 1 ]~~>>   | Fire | Thumb | Middle TOP |

    # ~~[ STICK / BTN 2 ]~~>>   | Fire A | Thumb | Right TOP |
    x52_pro.button(2).map_to(

        action(

            label = "STT/TWS Toggle",

            joy_modifiers = (clutch_modifier2),
            command       = 'Enter'

        )

    )

    # ~~[ STICK / BTN 3 ]~~>>   | Fire B | Thumb | Right BOTTOM |
    x52_pro.button(3).map_to(

        action(

            label = "Weapons SystemCMD Depress",

            joy_modifiers = (pinkie_modifier1),
            command       = 'O' # not a default shortcut!

        ),

        action(

            label = "TDC DEPRESS (Lock Target)",

            joy_modifiers = (clutch_modifier2),
            command       = 'L' # not default

        )

    )

    # ~~[ STICK / BTN 4 ]~~>>   | Fire C | Thumb | Left BOTTOM |
    x52_pro.button(4).map_to(

        action(

            label = "Nosewheel Steering/IFF Interrogate",

            joy_modifiers = (),
            command       = 'S'

        ),

        action(

            label = "Autopilot Standby Mode", #disengage trim too on ground

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Alt + A'

        )

    )

    # ~~[ STICK / POV BTN 19 ]~~>>  | Pov 2 | Thumb | Hat UP |
    x52_pro.button(19).map_to(

        action(

            label = "Trim UP", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Right Control + S'

        )

    )

    # ~~[ STICK / POV BTN 20 ]~~>>  | Pov 2 | Thumb | Hat RIGHT |
    x52_pro.button(20).map_to(

        action(

            label = "Trim RUDDER RIGHT", # Rudder Trim RIGHT

            joy_modifiers = (),
            command       = 'Right Control + X' # not a default shortcut!

        ),

        action(

            label = "Trim RIGHT", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (pinkie_modifier1),
            command       = 'Right Control + D'

        )

    )

    # ~~[ STICK / POV BTN 21 ]~~>>  | Pov 2 | Thumb | Hat DOWN |
    x52_pro.button(21).map_to(

        action(

            label = "Trim DOWN", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Right Control + W'

        )

    )

    # ~~[ STICK / POV BTN 22 ]~~>>  | Pov 2 | Thumb | Hat LEFT |
    x52_pro.button(22).map_to(

        action(

            label = "Trim RUDDER LEFT", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Right Control + Z' # not a default shortcut!

        ),

        action(

            label = "Trim LEFT", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (pinkie_modifier1),
            command       = 'Right Control + A'

        )

    )

    # ~~[ STICK / BTN 5 ]~~>>   | Pinkie | Pinkie | Rest |


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  STICK SWITCHES - BUTTONS   < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / SWITCH BTN 8 ]~~>>   | Toggle 1 | Left   | UP   |
    x52_pro.button(8).map_to(

        action(

            label = "Master Arm Toggle",

            joy_modifiers = (),
            command       = '0'

        ),

        action(

            label = "Gun Arm Toggle",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Control + 6'

        )

    )

    # ~~[ STICK / SWITCH BTN 9 ]~~>>   | Toggle 2 | Left   | DOWN |
    # ~~[ STICK / SWITCH BTN 10 ]~~>>  | Toggle 3 | Middle | UP   |
    # ~~[ STICK / SWITCH BTN 11 ]~~>>  | Toggle 4 | Middle | DOWN |
    #

    # ~~[ STICK / SWITCH BTN 12 ]~~>>  | Toggle 5 | Right  | UP   |
    x52_pro.button(12).map_to(

        action(

            label = "Control Stick - HIDE/SHOW",

            joy_modifiers = (),
            command       = 'Backspace'

        ),

        action(

            label = "Show pilot body",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Right Shift + P'

        ),

        action(

            label = "Smoke Device - ON/OFF",

            joy_modifiers = (clutch_modifier2),
            command       = '`' # not a default shortcut!

        )

    )

    #
    # ~~[ STICK / SWITCH BTN 13 ]~~>>  | Toggle 6 | Right  | DOWN |
    #


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >  HAND ON THROTTLE - BUTTONS < < < <
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #
    # ~~[ THROTTLE / WHEEL BTN 18 ]~~>>  | Right Mouse Button | Middle | Wheel CLICK       |
    x52_pro.button(18).map_to(

        action(

            label = "Toggle goggles", # NVG

            joy_modifiers = (),
            command       = 'Left Alt + Home'

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>  | Scroll Up          | Middle | Wheel Scroll UP   |
    x52_pro.button(16).map_to(

        action(

            label = "Gain goggles up", # NVG

            joy_modifiers = (),
            command       = 'Right Control + Right Shift + H'

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>  | Scroll Down        | Middle | Wheel Scroll DOWN |
    x52_pro.button(17).map_to(

        action(

            label = "Gain goggles down", # NVG

            joy_modifiers = (),
            command       = 'Right Alt + Right Shift + H'

        )

    )

    # ~~[ THROTTLE / POV BTN 25 ]~~>>  | Throttle Hat | Index | Hat UP
    x52_pro.button(25).map_to(

        action(

            label = "Air brake off",

            joy_modifiers = (),
            command       = 'Left Control + B'

        ),

        action(

            label = "TDC UP", #Throttle Designator Controller

            joy_modifiers = (clutch_modifier2),
            command       = ';'

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>  | Throttle Hat | Index | Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "TDC RIGHT", #Throttle Designator Controller

            joy_modifiers = (clutch_modifier2),
            command       = '/'

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>  | Throttle Hat | Index | Hat DOWN
    x52_pro.button(23).map_to(

        action(

            label = "Air brake on",

            joy_modifiers = (),
            command       = 'Left Shift + B'

        ),

        action(

            label = "TDC DOWN", #Throttle Designator Controller

            joy_modifiers = (clutch_modifier2),
            command       = '.'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>  | Throttle Hat | Index | Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "TDC LEFT", #Throttle Designator Controller

            joy_modifiers = (clutch_modifier2),
            command       = ','

        )

    )

    # ~~[ THROTTLE / BTN 7 ]~~>>   | Fire E | Thumb | Right TOP
    x52_pro.button(7).map_to(

        action(

            label = "Wheel Brake ON/OFF",

            joy_modifiers = (),
            command       = 'W'

        ),

        action(

            label = "Wheel Brake Left - ON/OFF",

            joy_modifiers = (clutch_modifier2),
            command       = 'Left Control + W'

        ),

        action(

            label = "Wheel Brake Right - ON/OFF",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Left Alt + W'

        )

    )

    # x52_pro.button(7).map_to(

    #     action(

    #         label = "Wheel Brake Left - ON/OFF",

    #         joy_modifiers = (),
    #         command       = 'Left Control + W'

    #     )

    # )

    # ~~[ THROTTLE / BTN 6 ]~~>>   | Fire D | Thumb | Right MIDDLE
    x52_pro.button(6).map_to(

        action(

            label = "Decoy PANIC release",

            joy_modifiers = (),
            command       = 'Insert'

        ),

        action(

            label = "Decoy Program release",

            joy_modifiers = (pinkie_modifier1),
            command       = 'Delete'

        )

    )

    #
    # ~~[ THROTTLE / BTN 30 ]~~>>  | Clutch | Thumb | Right BOTTOM
    #

    # ~~[ THROTTLE / BTN 15 ]~~>>  | Left Mouse Button | Thumb | Deep BOTTOM
    x52_pro.button(15).map_to(

        action(

            label = "OpenTrack Recenter",

            joy_modifiers = (),
            command = (
                #vjoy(4).button(2),
                vjoy(4).button(0)
            )
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

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>  | Left Wheel | CLICK

    # ~~[ THROTTLE / MFD BTN 34 ]~~>>   | Left Wheel | Scroll UP
    x52_pro.button(34).map_to(

        action(

            label = "Throttle (Left) - IDLE", speech_text="Throttle Left - IDLE",

            joy_modifiers = (),
            command       = 'Right Alt + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 35 ]~~>>   | Left Wheel | Scroll DOWN
    x52_pro.button(35).map_to(

        action(

            label = "Throttle (Left) - OFF", speech_text="Throttle Left - OFF",

            joy_modifiers = (),
            command       = 'Right Alt + End'

        )

    )

    # ~~[ THROTTLE / MFD BTN 32 ]~~>>   | Middle     | Button ABOVE
    x52_pro.button(32).map_to(

        action(

            label = "ATC Engage/Disengage Switch", speech_text="ATC",

            joy_modifiers = (),
            command       = 'T'

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>   | Middle     | Button BELOW
    x52_pro.button(33).map_to(

        action(

            label = "Landing Gear Control Handle - UP/DOWN", speech_text="Landing Gear",

            joy_modifiers = (),
            command       = 'G'

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>  | Right Wheel | CLICK

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>   | Right Wheel | Scroll UP
    x52_pro.button(36).map_to(

        action(

            label = "Throttle (Right) - IDLE", speech_text="Throttle Right - IDLE",

            joy_modifiers = (),
            command       = 'Right Shift + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>   | Right Wheel | Scroll DOWN
    x52_pro.button(37).map_to(

        action(

            label = "Throttle (Right) - OFF", speech_text="Throttle Right - OFF",

            joy_modifiers = (),
            command       = 'Right Shift + End'

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

    # ~~[ STICK / POV 0 | N ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('N').map_to(

        action(

            label = "CNM neutral (PCA SELECT)", speech_text="PCA SELECT",

            joy_modifiers = (),
            command       = 'V' # not default

        ),

        action(

            label = "Weapons SystemCMD FWD",

            joy_modifiers = (pinkie_modifier1),
            command       = 'U' # not default

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~   | Pov 1 | Thumb | Middle BOTTOM

    # ~~[ STICK / POV 0 | E ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "CNM MAGIC", speech_text="Magic",

            joy_modifiers = (),
            command       = 'D' # not default

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~   | Pov 1 | Thumb | Middle BOTTOM

    # ~~[ STICK / POV 0 | S ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "PCA Button 2 SELECT", speech_text="Police",

            joy_modifiers = (),
            command       = '2' # not default

        ),

        action(

            label = "Weapons SystemCMD AFT",

            joy_modifiers = (pinkie_modifier1),
            command       = 'I' # not default

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~   | Pov 1 | Thumb | Middle BOTTOM

    # ~~[ STICK / POV 0 | W ]~~   | Pov 1 | Thumb | Middle BOTTOM
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "CNM AA GUN", speech_text="AA Gun",

            joy_modifiers = (),
            command       = 'C'

        )

    )

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

            curve_filters = (
                Filter.Kalman(process_noise = 0.001, sensor_noise = 10000000, estimated_error = 100, radius = 0.04 * joy_axis_max, delay_radius_count = 17)
            )

        )

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