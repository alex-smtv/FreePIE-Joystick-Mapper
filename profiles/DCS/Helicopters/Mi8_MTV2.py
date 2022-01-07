#: Mi-8 MTV2
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

            label = "Release Weapons",

            joy_modifiers = (),
            command = 'Space'

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    x52_pro.button(1).map_to(

        action(

            label = "Release Bomb",

            joy_modifiers = (),
            command = 'B'

        )

    )

    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    x52_pro.button(3).map_to(

        action(

            label = "External Cargo Indicator", speech_text="Cargo Indicator",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Control + Right Shift + P'

        )

    )
    
    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "Pilot Trimmer",

            joy_modifiers = (),
            command       = 'T'

        ),

        action(

            label = "Trimmer reset",

            joy_modifiers = (modifier_pinkie),
            command       = 'Left Control + T'

        )

    )
    
    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "Left Headlight Power Switch - Up | Left Headlight Power Switch - Down",

            joy_modifiers = (modifier_clutch),
            command       = sequence.rotate(True).create('Left Shift + L', 'Left Shift + ;')

        ),

        action(

            label = "Right Headlight Power Switch - Up | Right Headlight Power Switch - Down",

            joy_modifiers = (modifier_pinkie),
            command       = sequence.rotate(True).create('Right Shift + L', 'Right Shift + ;')

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

            label = "Night Vision Goggles",

            joy_modifiers = (),
            command       = 'Right Shift + H'

        ),

        action(

            label = "Taxi Light Power Switch - ON/OFF",

            joy_modifiers = (modifier_clutch),
            command       = 'Right Control + L'
        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    x52_pro.button(16).map_to(

        action(

            label = "Night Vision Goggles Gain Up",

            joy_modifiers = (),
            command       = 'Right Control + Right Shift + H'

        ),
        
        action(

            label = "Sight Intensity Knob - CW/Increase",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Control + O'

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL AFT
    x52_pro.button(17).map_to(

        action(

            label = "Night Vision Goggles Gain Down",

            joy_modifiers = (),
            command       = 'Right Alt + Right Shift + H'

        ),
        
        action(

            label = "Sight Intensity Knob - CW/Decrease",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Alt + O'

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MFD
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel DOWN
    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    # ~~[ THROTTLE / MFD BTN 32 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER TOP
    # ~~[ THROTTLE / MFD BTN 33 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER BOTTOM
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

            label = "Weapon Safe/Armed Switch - ON/OFF",

            joy_modifiers = (),
            command       = 'Left Alt + S'

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
    x52_pro.button(12).map_to(

        action(

            label = "Show pilot body",

            joy_modifiers = (),
            command       = 'Right Shift + P'

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

        ),
        
        action(

            label = "AI Panel Show/Hide",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Win + H'

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

            label = "Autopilot Roll/Pitch Channel ON Button",

            joy_modifiers = (),
            command       = 'Left Win + A'

        ),

        action(

            label = "UV-26 Stop dispensing",

            joy_modifiers = (modifier_pinkie),
            command       = 'Delete'

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

            label = "Autopilot Altitude Channel ON Button | Autopilot Altitude Channel OFF Button",

            joy_modifiers = (),
            command       = sequence.rotate(True).create('Left Alt + A', 'Left Alt + Left Win + A')

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

            label = "Turn Off Autopilot Button",

            joy_modifiers = (),
            command       = 'Left Shift + Left Win + A'

        ),

        action(

            label = "UV-26 Start dispensing",

            joy_modifiers = (modifier_pinkie),
            command       = 'Insert'

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

            label = "Autopilot Heading Channel ON Button | Autopilot Heading Channel OFF Button",

            joy_modifiers = (),
            command       = sequence.rotate(True).create('Left Control + A', 'Left Control + Left Win + A')

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

            label = "Pylon Setup Selector Switch - set to GUN", speech_text="Select GOV", # Custom bind

            joy_modifiers = (),
            command       = 'Left Alt + Left Control + 6'

        ),
        
        action(

            label = "GUV Mode Switch - Increase", speech_text="GOV Mode Increase",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + Right Control + ]'

        ),

        action(

            label = "External Cargo Tactical Hook", speech_text="Hook",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Control + Right Shift + L'

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northeast
    # ~~[ STICK / POV 0 | E  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- East
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "Pylon Setup Selector Switch - CW", speech_text="Select Clockwise", # Custom bind

            joy_modifiers = (),
            command       = ';'

        ),
        
        action(

            label = "Mode UPK/PKT/RS Switch - Up", speech_text="Rocket Switch Up",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Control + ]'

        ),

        action(

            label = "Cargo View",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Left Alt + Left Shift + C'

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southeast
    # ~~[ STICK / POV 0 | S  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- South
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "Pylon Setup Selector Switch - set to I",  speech_text="Select POD 1",# Custom bind

            joy_modifiers = (),
            command       = 'Left Alt + Left Control + 1'

        ),

        action(

            label = "GUV Mode Switch - Decrease", speech_text="GOV Mode Decrease",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Alt + Right Control + ['

        ),

        action(

            label = "External Cargo Tactical Unhook", speech_text="Unhook",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Alt + Right Control + Right Shift + L'

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southwest
    # ~~[ STICK / POV 0 | W  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- West
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "Pylon Setup Selector Switch - CCW", speech_text="Select Counter-clockwise",# Custom bind

            joy_modifiers = (),
            command       = '.'

        ),
        
        action(

            label = "Mode UPK/PKT/RS Switch - Down", speech_text="Rocket Switch Down",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Control + ['

        ),

        action(

            label = "External Cargo Autounhook Switch - ON/OFF", speech_text="Auto Unhook",

            joy_modifiers = (modifier_clutch, modifier_pinkie),
            command       = 'Right Control + Right Shift + K'

        )

    )

    # ~~[ STICK / POV 0 | NW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northwest


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / THROTTLE   [TOP | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / POV BTN 25 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat FWD
    x52_pro.button(25).map_to(

        action(

            label = "Left Headlight - Up",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Shift + 8'

        ),

        action(

            label = "Right Headlight - Up",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Shift + 8'

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "Left Headlight - Right",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Shift + 0'

        ),

        action(

            label = "Right Headlight - Right",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Shift + 0'

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "Left Headlight - Down",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Shift + 7'

        ),

        action(

            label = "Right Headlight - Down",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Shift + 7'

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "Left Headlight - Left",

            joy_modifiers = (modifier_clutch),
            command       = 'Left Shift + 9'

        ),

        action(

            label = "Right Headlight - Left",

            joy_modifiers = (modifier_pinkie),
            command       = 'Right Shift + 9'

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

            invert = False,

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

                Filter.MinMax(-0.5 * joy_axis_max, 1 * joy_axis_max)

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
