#: Mirage 2000C
from src.client.client_interface import joy, vjoy, action, threshold, sequence, transfer, Filter
from src.helpers.freepie_vars    import FreePieVars

def x52_pro_mapping():
    ### Joystick Builder Settings
    joy_name     = "X52 Professional H.O.T.A.S."
    joy_axis_max = 1000

    x52_pro = joy(joy_name, joy_axis_max)

    ### Modifiers Vars
    modifier_pinkie = 5
    modifier_clutch = 30

    #* ///////////////////////////////////////////////////////////////////////////////
    #* //                                                                           
    #* // BUTTONS                                                         
    #* //                                                                           
    #* ///////////////////////////////////////////////////////////////////////////////

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / STICK
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / BTN 0  ]~~>>    BUTTONS / STICK --- Index First Stage TRIGGER
    x52_pro.button(0).map_to(

        action(

            label = "Weapons FIRE/Bombs Release", # Fire weapon

            joy_modifiers = (),
            command = 'Space'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    x52_pro.button(2).map_to(

        action(

            label = "STT/TWS Toggle",

            joy_modifiers = (modifier_clutch),
            command       = 'Enter'

        )

    )

    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    x52_pro.button(3).map_to(

        action(

            label = "Weapons SystemCMD Depress",

            joy_modifiers = (modifier_pinkie),
            command       = 'O' # not a default shortcut!

        ),

        action(

            label = "TDC DEPRESS (Lock Target)",

            joy_modifiers = (modifier_clutch),
            command       = 'L' # not default

        )

    )

    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "Nosewheel Steering/IFF Interrogate",

            joy_modifiers = (),
            command       = 'S'

        ),

        action(

            label = "Autopilot Standby Mode", #disengage trim too on ground

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Alt + A'

        )

    )

    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "Wheel Brake ON/OFF",

            joy_modifiers = (),
            command       = 'W'

        ),

        action(

            label = "Wheel Brake Left - ON/OFF",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Control + W'

        ),

        action(

            label = "Wheel Brake Right - ON/OFF",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Alt + W'

        )

    )

    # ~~[ THROTTLE / BTN 6  ]~~>>    BUTTONS / THROTTLE --- MIDDLE
    x52_pro.button(6).map_to(

        action(

            label = "Decoy PANIC release",

            joy_modifiers = (),
            command       = 'Insert'

        ),

        action(

            label = "Decoy Program release",

            joy_modifiers = (modifier_pinkie),
            command       = 'Delete'

        )

    )

    # ~~[ THROTTLE / BTN 30 ]~~>>    BUTTONS / THROTTLE --- BOTTOM
    # ~~[ THROTTLE / BTN 15 ]~~>>    BUTTONS / THROTTLE --- Mouse Click BOTTOM
    x52_pro.button(15).map_to(

        action(

            label = "OpenTrack Recenter",

            joy_modifiers = (),
            command = (
                vjoy(0).button(0)
            )
        ),

        action(

            label = "OpenTrack Freeze",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).button(1)
        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MOUSE WHEEL
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / WHEEL BTN 18 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- DOWN
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

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL AFT
    x52_pro.button(17).map_to(

        action(

            label = "Gain goggles down", # NVG

            joy_modifiers = (),
            command       = 'Right Alt + Right Shift + H'

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MFD
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    x52_pro.button(34).map_to(

        action(

            label = "Throttle (Left) - IDLE", speech_text="Throttle Left - IDLE",

            joy_modifiers = (),
            command       = 'Right Alt + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    x52_pro.button(35).map_to(

        action(

            label = "Throttle (Left) - OFF", speech_text="Throttle Left - OFF",

            joy_modifiers = (),
            command       = 'Right Alt + End'

        )

    )

    # ~~[ THROTTLE / MFD BTN 32 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER TOP
    x52_pro.button(32).map_to(

        action(

            label = "ATC Engage/Disengage Switch", speech_text="ATC",

            joy_modifiers = (),
            command       = 'T'

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER BOTTOM
    x52_pro.button(33).map_to(

        action(

            label = "Landing Gear Control Handle - UP/DOWN", speech_text="Landing Gear",

            joy_modifiers = (),
            command       = 'G'

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 36 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel FWD
    x52_pro.button(36).map_to(

        action(

            label = "Throttle (Right) - IDLE", speech_text="Throttle Right - IDLE",

            joy_modifiers = (),
            command       = 'Right Shift + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel AFT
    x52_pro.button(37).map_to(

        action(

            label = "Throttle (Right) - OFF", speech_text="Throttle Right - OFF",

            joy_modifiers = (),
            command       = 'Right Shift + End'

        )

    )


    #* ///////////////////////////////////////////////////////////////////////////////
    #* //                                                                           
    #* // SWITCHES                                                         
    #* //                                                                           
    #* ///////////////////////////////////////////////////////////////////////////////

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   SWITCHES / STICK
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / SWITCH BTN 8  ]~~>>    SWITCHES / STICK --- LEFT FWD
    x52_pro.button(8).map_to(

        action(

            label = "Master Arm Toggle",

            joy_modifiers = (),
            command       = '0'

        ),

        action(

            label = "Gun Arm Toggle",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + 6'

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
    x52_pro.button(12).map_to(

        action(

            label = "Control Stick - HIDE/SHOW",

            joy_modifiers = (),
            command       = 'Backspace'

        ),

        action(

            label = "Show pilot body",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Shift + P'

        ),

        action(

            label = "Smoke Device - ON/OFF",

            joy_modifiers = (modifier_clutch),
            command       = '`' # not a default shortcut!

        )

    )

    # ~~[ STICK / SWITCH BTN 13 ]~~>>    SWITCHES / STICK --- RIGHT AFT


    #* ///////////////////////////////////////////////////////////////////////////////
    #* //                                                                           
    #* // POVS                                                         
    #* //                                                                           
    #* ///////////////////////////////////////////////////////////////////////////////

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / STICK   [TOP LEFT | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / POV BTN 19 ]~~>>    POV / STICK   [TOP LEFT | 4-Way] --- Hat FWD
    x52_pro.button(19).map_to(

        action(

            label = "Trim UP", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Right Control + S'

        ),
        
        action(

            label = "SRS Radio Bind",

            joy_modifiers = (modifier_clutch),
            command       = vjoy(0).button(11)

        )

    )

    # ~~[ STICK / POV BTN 20 ]~~>>    POV / STICK   [TOP LEFT | 4-Way] --- Hat RIGHT 
    x52_pro.button(20).map_to(

        action(

            label = "Trim RUDDER RIGHT", # Rudder Trim RIGHT

            joy_modifiers = (),
            command       = 'Right Control + X' # not a default shortcut!

        ),

        action(

            label = "Trim RIGHT", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Control + D'

        ),
        
        action(

            label = "SRS Radio Bind",

            joy_modifiers = (modifier_clutch),
            command       = vjoy(0).button(12)

        )

    )

    # ~~[ STICK / POV BTN 21 ]~~>>    POV / STICK   [TOP LEFT | 4-Way] --- Hat AFT
    x52_pro.button(21).map_to(

        action(

            label = "Trim DOWN", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Right Control + W'

        ),
        
        action(

            label = "SRS Radio Bind",

            joy_modifiers = (modifier_clutch),
            command       = vjoy(0).button(13)

        )

    )

    # ~~[ STICK / POV BTN 22 ]~~>>    POV / STICK   [TOP LEFT | 4-Way] --- Hat LEFT 
    x52_pro.button(22).map_to(

        action(

            label = "Trim RUDDER LEFT", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Right Control + Z' # not a default shortcut!

        ),

        action(

            label = "Trim LEFT", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Control + A'

        ),
        
        action(

            label = "SRS Radio Bind",

            joy_modifiers = (modifier_clutch),
            command       = vjoy(0).button(10)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / STICK   [BOTTOM CENTER - 8-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ STICK / POV 0 | N  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- North
    x52_pro.pov(0).cardinal('N').map_to(

        action(

            label = "CNM neutral (PCA SELECT)", speech_text="PCA SELECT",

            joy_modifiers = (),
            command       = 'V' # not default

        ),

        action(

            label = "Weapons SystemCMD FWD",

            joy_modifiers = (modifier_pinkie),
            command       = 'U' # not default

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northeast
    # ~~[ STICK / POV 0 | E  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- East
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "CNM MAGIC", speech_text="Magic",

            joy_modifiers = (),
            command       = 'D' # not default

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southeast
    # ~~[ STICK / POV 0 | S  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- South
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "PCA Button 2 SELECT", speech_text="Police",

            joy_modifiers = (),
            command       = '2' # not default

        ),

        action(

            label = "Weapons SystemCMD AFT",

            joy_modifiers = (modifier_pinkie),
            command       = 'I' # not default

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southwest
    # ~~[ STICK / POV 0 | W  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- West
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "CNM AA GUN", speech_text="AA Gun",

            joy_modifiers = (),
            command       = 'C'

        )

    )

    # ~~[ STICK / POV 0 | NW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northwest


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / THROTTLE   [TOP | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / POV BTN 25 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat FWD
    x52_pro.button(25).map_to(

        action(

            label = "Air brake off",

            joy_modifiers = (),
            command       = 'Left Control + B'

        ),

        action(

            label = "TDC UP", #Throttle Designator Controller

            joy_modifiers = (modifier_clutch),
            command       = ';'

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "TDC RIGHT", #Throttle Designator Controller

            joy_modifiers = (modifier_clutch),
            command       = '/'

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "Air brake on",

            joy_modifiers = (),
            command       = 'Left Shift + B'

        ),

        action(

            label = "TDC DOWN", #Throttle Designator Controller

            joy_modifiers = (modifier_clutch),
            command       = '.'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "TDC LEFT", #Throttle Designator Controller

            joy_modifiers = (modifier_clutch),
            command       = ','

        )

    )


    #* ///////////////////////////////////////////////////////////////////////////////
    #* //                                                                           
    #* // AXES                                                         
    #* //                                                                           
    #* ///////////////////////////////////////////////////////////////////////////////

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   AXES / STICK
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #stick_deadzone = 2.3
    stick_deadzone = 0

    stick_curve = Filter.Curve(

        max_value    = joy_axis_max,
        deadzone     = stick_deadzone,
        saturation_x = 100,
        saturation_y = 100,
        curvature    = 0

    )

    # ~~[ STICK / AXIS X ]~~
    x52_pro.axis('x').map_to(

        vjoy(0).axis('x').filtered_with(

            curve_filters = (
                stick_curve
            )

        )

    )

    # ~~[ STICK / AXIS Y ]~~
    x52_pro.axis('y').map_to(

        vjoy(0).axis('y').filtered_with(

            curve_filters = (
                stick_curve
            )

        )

    )

    # ~~[ STICK / AXIS RZ ]~~
    x52_pro.axis('rz').map_to(

        vjoy(0).axis('rz').filtered_with(

            curve_filters = (
                Filter.MinMax(-1 * joy_axis_max, 1 * joy_axis_max)
            )

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   AXES / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    # ~~[ THROTTLE / AXIS SLIDER1 ]~~
    x52_pro.axis('slider1').map_to(

        vjoy(0).axis('slider1').filtered_with(

            invert = True,

            curve_filters = (

                Filter.Kalman(
                    process_noise = 0.001, 
                    sensor_noise = 10000000, 
                    estimated_error = 100, 
                    radius = 0.04 * joy_axis_max, 
                    delay_radius_count = 17
                ),

                # Filter.LowPass(
                #     smoothing_factor = 0.000001, 
                #     radius = 0.035 * joy_axis_max
                # ),

                Filter.MinMax(-1 * joy_axis_max, 0.5 * joy_axis_max)

            )

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   AXES / REGISTRY HACK
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # The following axis doesn't physically exist on the x52 pro.
    # However a registry hack allows it to virtually exist (e.g. by mapping one mouse mini-stick axis to it).

    # ~~[ REGISTRY HACK / AXIS SLIDER2 ]~~
    x52_pro.axis('slider2').map_to(

        vjoy(0).axis('slider2').filtered_with(

            invert = True,
            
            curve_filters = (
                Filter.MinMax(-1 * joy_axis_max, 1 * joy_axis_max)
            )

        )

    )

    return x52_pro
