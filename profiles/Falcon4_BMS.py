#: Falcon 4 BMS
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

            label = "STICK: FIRST TRIGGER DETENT", # Fire weapon

            joy_modifiers = (),
            command = 'Left Control + /'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    x52_pro.button(14).map_to(

        action(

            label = "STICK: SECOND TRIGGER DETENT", # Fire weapon

            joy_modifiers = (),
            command = 'Left Alt + /'

        )

    )

    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    x52_pro.button(1).map_to(

        action(

            label = "STICK: WEAPON RELEASE (Pickle)", # Fire weapon

            joy_modifiers = (),
            command = 'Space'

        )

    )

    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "STICK: NWS A/R DISC MSL STEP SWITCH", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Left Shift + /'

        )

    )

    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "CKPIT: Wheel Brakes - Hold",

            joy_modifiers = (),
            command       = 'K'

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

            label = "CKPIT: Nightvision - Toggle", # NVG

            joy_modifiers = (),
            command       = 'N'

        ),

        action(

            label = "CKPIT: Visor - Toggle",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Alt + V'

        ),

        action(

            label = "CKPIT: Spotlight - Toggle",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Shift + S'

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL AFT


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MFD
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    # ~~[ THROTTLE / MFD BTN 32 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER TOP
    # ~~[ THROTTLE / MFD BTN 33 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER BOTTOM
    x52_pro.button(33).map_to(

        action(

            label = "GEAR: LG Handle - Toggle", speech_text="Landing Gear",

            joy_modifiers = (),
            command       = 'G'

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 36 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel FWD
    # ~~[ THROTTLE / MFD BTN 37 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel AFT


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

            label = "MISC: MASTER ARM Switch - Cycle",

            joy_modifiers = (),
            command       = 'Left Shift + M'

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
    x52_pro.button(12).map_to(

        action(

            label = "SIM: Togle Pilot Model",

            joy_modifiers = (),
            command = sequence.rotate(False).create(
                'Left Alt + C',
                'P'
            )

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

            label = "STICK: TRIM Down - Nose Up", # Elevator Trim UP

            joy_modifiers = (),
            command       = 'Left Control + Down ARROW'

        ),

        action(

            label = "CKPIT: FLAPS - Increase",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + F12'

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

            label = "TRIM: YAW TRIM Knob - R", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Left Control + Left Alt + F10'

        ),

        action(

            label = "STICK: TRIM Right - Roll Right", # Ailreon Trim RIGHT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + Right Arrow'

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

            label = "STICK: Trim Up - Nose Down", # Elevator Trim DOWN

            joy_modifiers = (),
            command       = 'Left Control + Up Arrow'

        ),

        action(

            label = "CKPIT: FLAPS - Decrease",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + F11'

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

            label = "TRIM: YAW TRIM Knob - L", # Rudder Trim LEFT

            joy_modifiers = (),
            command       = 'Left Control + Left Alt + F9'

        ),

        action(

            label = "STICK: TRIM Left - Roll Left", # Ailreon Trim LEFT WING DOWN

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + Left Arrow'

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

            label = "TQS: SPD BRAKE Switch Close",

            joy_modifiers = (),
            command       = 'Left Control + B'

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "TQS: SPD BRAKE Switch Open",

            joy_modifiers = (),
            command       = 'Left Shift + B'

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
