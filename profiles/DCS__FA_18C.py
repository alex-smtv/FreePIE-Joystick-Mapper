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

            label = "Gun Trigger - SECOND DETENT (Press to shoot)",

            joy_modifiers = (),
            command = 'Space'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    x52_pro.button(1).map_to(

        action(

            label = "Weapon Release",

            joy_modifiers = (),
            command       = 'Right Alt + Space'

        )

    )

    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    x52_pro.button(3).map_to(

        action(

            label = "Cage/Uncage",

            joy_modifiers = (),
            command       = 'C'

        ),

        action(

            label = "Sensor Control Switch - Depress",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + Enter' # not a default shortcut!

        )

    )

    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "Undesignate/Nose Wheel Steer Switch",

            joy_modifiers = (),
            command       = 'S'

        ),

        action(

            label = "Autopilot/Nosewheel Steering Disengage (Paddle) Switch",

            joy_modifiers = (modifier_pinkie),
            command       = 'A'

        )

    )

    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "Throttle Designator Controller - Depress",

            joy_modifiers = (),
            command       = 'Enter'

        ),

        action(

            label = "RAID/FLIR FOV Select Button",

            joy_modifiers = (modifier_clutch),
            command       = 'i'

        )

    )

    # ~~[ THROTTLE / BTN 6  ]~~>>    BUTTONS / THROTTLE --- MIDDLE
    x52_pro.button(6).map_to(

        action(

            label = "VKB T-Rudder T-Link", # Differential brakes

            joy_modifiers = (),
            command       = vjoy(4).button(0)

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
            command       = 'Right Shift + H'

        ),

        action(

            label = "Exterior Light Switch - ON/OFF",

            joy_modifiers = (modifier_pinkie),
            command       = 'L'

        ),

        action(

            label = "RECCE Event Mark Switch", # Turn ON/OFF HMD

            joy_modifiers = (modifier_pinkie, modifier_clutch),
            command       = 'R'

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    x52_pro.button(16).map_to(

        action(

            label = "Gain goggles up", # NVG

            joy_modifiers = (),
            command       = 'Right Control + Right Shift + H'

        )

    )

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
    x52_pro.button(31).map_to(

        action(

            label = "Flaps Down",

            joy_modifiers = (),
            command       = 'Left Alt + Left Control + F'

        )

    )

    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    x52_pro.button(34).map_to(

        action(

            label = "Throttle (Left) - IDLE", speech_text="Throttle Left IDLE",

            joy_modifiers = (),
            command       = 'Right Alt + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    x52_pro.button(35).map_to(

        action(

            label = "Throttle (Left) - OFF", speech_text="Throttle Left OFF",

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
    x52_pro.button(38).map_to(

        action(

            label = "Flaps Up",

            joy_modifiers = (),
            command       = 'Left Alt + Left Shift + F'

        )

    )

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel FWD
    x52_pro.button(36).map_to(

        action(

            label = "Throttle (Right) - IDLE", speech_text="Throttle Right IDLE",

            joy_modifiers = (),
            command       = 'Right Shift + Home'

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel AFT
    x52_pro.button(37).map_to(

        action(

            label = "Throttle (Right) - OFF", speech_text="Throttle Right OFF",

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

            label = "Master Arm Switch: Arm/Safe",

            joy_modifiers = (),
            command       = 'M'

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    x52_pro.button(9).map_to(

        action(

            label = "MASTER CAUTION Reset Button",

            joy_modifiers = (),
            command       = 'N'

        )

    )

    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    x52_pro.button(10).map_to(

        action(

            label = "Master Mode: A/A",

            joy_modifiers = (),
            command       = '1'

        )

    )

    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    x52_pro.button(11).map_to(

        action(

            label = "Master Mode: A/G",

            joy_modifiers = (),
            command       = '2'

        )

    )

    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
    x52_pro.button(12).map_to(

        action(

            label = "Show pilot body",

            joy_modifiers = (),
            command       = 'Right Shift + P'

        ),
        
        action(

            label = "Control Stick - HIDE/SHOW",

            joy_modifiers = (modifier_pinkie),
            command       = 'Backspace'

        ),
        
        action(

            label = "Show controls indicator",

            joy_modifiers = (modifier_clutch),
            command       = 'Right Control + Enter'

        )

    )

    # ~~[ STICK / SWITCH BTN 13 ]~~>>    SWITCHES / STICK --- RIGHT AFT
    x52_pro.button(13).map_to(

        action(

            label = "Flashlight",

            joy_modifiers = (),
            command       = 'Left Alt + L'

        )

    )


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

            label = "Trimmer Switch - PULL (CLIMB)", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Right Control + .'

        ),

        action(

            label = "Dispense Switch - Forward(CHAFF)/Center(OFF)",

            joy_modifiers = (modifier_pinkie),
            command       = 'E'

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

            label = "Trimmer Switch - RIGHT WING DOWN", # Ailreon Trim RIGHT WING DOWN

            joy_modifiers = (),
            command       = 'Right Control + /'

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

            label = "Trimmer Switch - PUSH(DESCEND)", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Right Control + ;'

        ),

        action(

            label = "Dispense Switch - Aft(FLARE)/Center(OFF)",

            joy_modifiers = (modifier_pinkie),
            command       = 'D'

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

            label = "Trimmer Switch - LEFT WING DOWN", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (),
            command       = 'Right Control + ,'

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

            label = "Select Sparrow", speech_text="FOX 1 AIM-7",

            joy_modifiers = (),
            command       = 'Left Shift + W'

        ),

        action(

            label = "Sensor Control Switch - Fwd",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + ;'

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northeast
    # ~~[ STICK / POV 0 | E  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- East
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "Select AMRAAM", speech_text="FOX 3 AIM-120",

            joy_modifiers = (),
            command       = 'Left Shift + D'

        ),

        action(

            label = "Sensor Control Switch - Right",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + /'

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southeast
    # ~~[ STICK / POV 0 | S  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- South
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "Select Sidewinder", speech_text="FOX 2 AIM-9",

            joy_modifiers = (),
            command       = 'Left Shift + S'

        ),

        action(

            label = "Sensor Control Switch - Aft",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + .'

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southwest
    # ~~[ STICK / POV 0 | W  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- West
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "Select Gun", speech_text="Gun",

            joy_modifiers = (),
            command       = 'Left Shift + X'

        ),

        action(

            label = "Sensor Control Switch - Left",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + ,'

        )

    )

    # ~~[ STICK / POV 0 | NW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northwest


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / THROTTLE   [TOP | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / POV BTN 25 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat FWD
    x52_pro.button(25).map_to(

        action(

            label = "Throttle Designator Controller - Up",

            joy_modifiers = (),
            command       = ';'

        ),

        action(

            label = "Radar Elevation Control - Up",

            joy_modifiers = (modifier_clutch),
            command       = '='

        ),

        action(

            label = "Speed Brake Retract",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + B'

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "Throttle Designator Controller - Right",

            joy_modifiers = (),
            command       = '/'

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "Throttle Designator Controller - Down",

            joy_modifiers = (),
            command       = '.'

        ),

        action(

            label = "Radar Elevation Control - Down",

            joy_modifiers = (modifier_clutch),
            command       = '-'

        ),

        action(

            label = "Speed Brake Extend",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Shift + B'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "Throttle Designator Controller - Left",

            joy_modifiers = (),
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

                Filter.MinMax(-1 * joy_axis_max, 0 * joy_axis_max)

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
