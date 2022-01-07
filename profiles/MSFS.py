#: Microsoft Flight Simulator 2020
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

            label = "Cockpit View Upper",

            joy_modifiers = (),
            command       = 'Space'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    x52_pro.button(3).map_to(

        action(

            label = "Reset View",

            joy_modifiers = (),
            command       = 'Left Control + Space'

        )

    )

    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "Toggle Tail Wheel Lock",

            joy_modifiers = (),
            command       = 'Left Shift + G'

        )

    )

    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "Brakes",

            joy_modifiers = (),
            command       = 'Num .'

        ),

        action(

            label = "Left Brake",

            joy_modifiers = (modifier_clutch),
            command       = 'Num *'

        ),

        action(

            label = "Right Brake",

            joy_modifiers = (modifier_pinkie),
            command       = 'Num -'

        )

    )

    # ~~[ THROTTLE / BTN 6  ]~~>>    BUTTONS / THROTTLE --- MIDDLE
    x52_pro.button(6).map_to(

        action(

            label = "VKB T-Rudder T-Link", # Differential brakes

            joy_modifiers = (),
            command       = vjoy(4).button(0)

        ),
        
        action(

            label = "Toggle Throttle Reverse Thrust",

            joy_modifiers = (modifier_clutch),
            command       = 'I' # NOT A DEFAULT BIND

        ),

        action(

            label = "Toggle Propeller Reverse Thrust",

            joy_modifiers = (modifier_pinkie),
            command       = 'U' # NOT A DEFAULT BIND

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
    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    x52_pro.button(16).map_to(

        action(

            label = "Zoom",

            joy_modifiers = (),
            command       = sequence.rotate(False).create(
                '='
            )

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL AFT
    x52_pro.button(17).map_to(

        action(

            label = "Dezoom",

            joy_modifiers = (),
            command       = sequence.rotate(False).create(
                '-'
            )

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MFD
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    # ~~[ THROTTLE / MFD BTN 32 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER TOP
    x52_pro.button(32).map_to(

        action(

            label = "Toggle Spoilers",

            joy_modifiers = (modifier_pinkie),
            command       = 'Num /'

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER BOTTOM
    x52_pro.button(33).map_to(

        action(

            label = "Toggle Landing Gear", speech_text="Landing Gear",

            joy_modifiers = (),
            command       = 'G'

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel DOWN
    x52_pro.button(38).map_to(

        action(

            label = "Toggle Parking Brakes",

            joy_modifiers = (),
            command       = 'Left Control + Num .'

        )

    )

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel FWD
    x52_pro.button(36).map_to(

        action(

            label = "Auto Start Engine",

            joy_modifiers = (),
            command       = 'Left Control + E'

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel AFT
    x52_pro.button(37).map_to(

        action(

            label = "Engine Autostop",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Shift + Left Control + E'

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

            label = "Display ATC",

            joy_modifiers = (),
            command       = 'Scroll Lock'

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    x52_pro.button(9).map_to(

        action(

            label = "Display NavLog",

            joy_modifiers = (),
            command       = 'N'

        )

    )

    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
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

            label = "Elevator Trim UP", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Num 1'

        ),

        action(

            label = "Decrease Flaps",

            joy_modifiers = (modifier_pinkie),
            command       = 'F6'

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

            label = "Rudder Trim Right", # Rudder Trim RIGHT

            joy_modifiers = (),
            command       = 'Left Control + Enter' # not a default shortcut!

        ),

        action(

            label = "Aileron Trim Right", # Ailreon Trim RIGHT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + Num 6'

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

            label = "Elevator Trim DOWN", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Num 7'

        ),

        action(

            label = "Increase Flaps",

            joy_modifiers = (modifier_pinkie),
            command       = 'F7'

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

            label = "Rudder Trim Left", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Left Control + Num 0' # not a default shortcut!

        ),

        action(

            label = "Aileron Trim Left", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + Num 4'

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
    # ~~[ STICK / POV 0 | NE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northeast
    # ~~[ STICK / POV 0 | E  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- East
    # ~~[ STICK / POV 0 | SE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southeast
    # ~~[ STICK / POV 0 | S  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- South
    # ~~[ STICK / POV 0 | SW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southwest
    # ~~[ STICK / POV 0 | W  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- West
    # ~~[ STICK / POV 0 | NW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northwest


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / THROTTLE   [TOP | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / POV BTN 25 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat FWD
    x52_pro.button(25).map_to(

        action(

            label = "Zoom",

            joy_modifiers = (),
            command       = '='

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "Dezoom",

            joy_modifiers = (),
            command       = '-'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat LEFT


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

                Filter.MinMax(-1 * joy_axis_max, 1 * joy_axis_max)

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
