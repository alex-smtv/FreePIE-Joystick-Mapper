#: vJoy 1 to 1
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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(0)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(0)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(0)

        )

    )

    # ~~[ STICK / BTN 14 ]~~>>    BUTTONS / STICK --- Index Second Stage TRIGGER
    x52_pro.button(14).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(14)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(14)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(14)

        )

    )

    # ~~[ STICK / BTN 1  ]~~>>    BUTTONS / STICK --- Thumb TOP CENTER
    x52_pro.button(1).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(1)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(1)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(1)

        )

    )

    # ~~[ STICK / BTN 2  ]~~>>    BUTTONS / STICK --- Thumb TOP RIGHT
    x52_pro.button(2).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(2)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(2)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(2)

        )

    )

    # ~~[ STICK / BTN 3  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM RIGHT
    x52_pro.button(3).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(3)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(3)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(3)

        )

    )

    # ~~[ STICK / BTN 4  ]~~>>    BUTTONS / STICK --- Thumb BOTTOM LEFT
    x52_pro.button(4).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(4)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(4)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(4)

        )

    )

    # ~~[ STICK / BTN 5  ]~~>>    BUTTONS / STICK --- Pinkie
    x52_pro.button(5).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(5)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(5)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(5)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / BTN 7  ]~~>>    BUTTONS / THROTTLE --- TOP
    x52_pro.button(7).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(7)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(7)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(7)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(18)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(18)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(18)

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 16 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL FWD
    x52_pro.button(16).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(16)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(16)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(16)

        )

    )

    # ~~[ THROTTLE / WHEEL BTN 17 ]~~>>    BUTTONS / THROTTLE MOUSE WHEEL --- SCROLL AFT
    x52_pro.button(17).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(17)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(17)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(17)

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   BUTTONS / THROTTLE MFD
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / MFD BTN 31 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel DOWN
    x52_pro.button(31).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(31)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(31)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(31)

        )

    )

    # ~~[ THROTTLE / MFD BTN 34 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL FWD
    x52_pro.button(34).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(34)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(34)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(34)

        )

    )

    # ~~[ THROTTLE / MFD BTN 35 ]~~>>    BUTTONS / THROTTLE MFD --- Left Wheel SCROLL AFT
    x52_pro.button(35).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(35)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(35)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(35)

        )

    )

    # ~~[ THROTTLE / MFD BTN 32 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER TOP
    x52_pro.button(32).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(32)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(32)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(32)

        )

    )

    # ~~[ THROTTLE / MFD BTN 33 ]~~>>    BUTTONS / THROTTLE MFD --- CENTER BOTTOM
    x52_pro.button(33).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(33)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(33)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(33)

        )

    )

    # ~~[ THROTTLE / MFD BTN 38 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel DOWN
    x52_pro.button(38).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(38)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(38)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(38)

        )

    )

    # ~~[ THROTTLE / MFD BTN 36 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel FWD
    x52_pro.button(36).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(36)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(36)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(36)

        )

    )

    # ~~[ THROTTLE / MFD BTN 37 ]~~>>    BUTTONS / THROTTLE MFD --- Right Wheel AFT
    x52_pro.button(37).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(37)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(37)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(37)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(8)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(8)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(8)

        )

    )

    # ~~[ STICK / SWITCH BTN 9  ]~~>>    SWITCHES / STICK --- LEFT AFT
    x52_pro.button(9).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(9)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(9)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(9)

        )

    )

    # ~~[ STICK / SWITCH BTN 10 ]~~>>    SWITCHES / STICK --- CENTER FWD
    x52_pro.button(10).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(10)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(10)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(10)

        )

    )

    # ~~[ STICK / SWITCH BTN 11 ]~~>>    SWITCHES / STICK --- CENTER AFT
    x52_pro.button(11).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(11)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(11)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(11)

        )

    )

    # ~~[ STICK / SWITCH BTN 12 ]~~>>    SWITCHES / STICK --- RIGHT FWD
    x52_pro.button(12).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(12)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(12)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(12)

        )

    )

    # ~~[ STICK / SWITCH BTN 13 ]~~>>    SWITCHES / STICK --- RIGHT AFT
    x52_pro.button(13).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(13)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(13)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(13)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(19)

        ),
        
        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(19)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(20)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(20)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(21)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(21)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(22)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(22)

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

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('N')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('N')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('N')

        )

    )

    # ~~[ STICK / POV 0 | NE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northeast
    x52_pro.pov(0).cardinal('NE').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('NE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('NE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('NE')

        )

    )

    # ~~[ STICK / POV 0 | E  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- East
    x52_pro.pov(0).cardinal('E').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('E')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('E')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('E')

        )

    )

    # ~~[ STICK / POV 0 | SE ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southeast
    x52_pro.pov(0).cardinal('SE').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('SE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('SE')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('SE')

        )

    )

    # ~~[ STICK / POV 0 | S  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- South
    x52_pro.pov(0).cardinal('S').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('S')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('S')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('S')

        )

    )

    # ~~[ STICK / POV 0 | SW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Southwest
    x52_pro.pov(0).cardinal('SW').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('SW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('SW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('SW')

        )

    )

    # ~~[ STICK / POV 0 | W  ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- West
    x52_pro.pov(0).cardinal('W').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('W')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('W')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('W')

        )

    )

    # ~~[ STICK / POV 0 | NW ]~~    POV / STICK   [BOTTOM CENTER - 8-Way] --- Northwest
    x52_pro.pov(0).cardinal('NW').map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).pov(0).cardinal('NW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(0).pov(1).cardinal('NW')

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(0).pov(2).cardinal('NW')

        )

    )


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # > > > >   POV / THROTTLE   [TOP | 4-Way]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~[ THROTTLE / POV BTN 25 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat FWD
    x52_pro.button(25).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(25)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(25)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(25)

        )

    )

    # ~~[ THROTTLE / POV BTN 24 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat RIGHT
    x52_pro.button(24).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(24)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(24)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(24)

        )

    )

    # ~~[ THROTTLE / POV BTN 23 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat AFT
    x52_pro.button(23).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(23)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(23)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(23)

        )

    )

    # ~~[ THROTTLE / POV BTN 26 ]~~>>    POV / THROTTLE   [TOP | 4-Way] --- Hat LEFT
    x52_pro.button(26).map_to(

        action(

            label = "",

            joy_modifiers = (),
            command = vjoy(0).button(26)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_pinkie),
            command = vjoy(1).button(26)

        ),

        action(

            label = "",

            joy_modifiers = (modifier_clutch),
            command = vjoy(2).button(26)

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
