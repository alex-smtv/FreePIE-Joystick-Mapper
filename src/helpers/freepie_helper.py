import time
import FreePIE.Core.Plugins.Key as KeyFP

# .NET Core Imports
import System.Runtime.InteropServices.RuntimeInformation

# Note: Make us of CLR = .NET Common Language Runtime (FreePie runs on IronPython)
# Useful module: clr (clr.GetClrType(), etc.)
# With CLR we have access to GetType()
class FreePieTypeCheck:
    is_check_activated = True

    @staticmethod
    def py_str_type_of(var):
        return var.__class__.__name__

    @staticmethod
    def net_type_of(var):
        return var.GetType()

    @staticmethod
    def str_net_type_of(*vars):
        text = ''

        for var in vars:
            text += var.GetType().ToString() + ' | '

        return text[:-3]

    @staticmethod
    def _strict_check(var, expected_type_str):
        if FreePieTypeCheck.is_check_activated:
            if FreePieTypeCheck.py_str_type_of(var) != expected_type_str:
                raise RuntimeError('The strict check failed with expected type str: ' + expected_type_str)

            return True

    @staticmethod
    def check_keyboard(keyboard):
        try:
            return FreePieTypeCheck._strict_check(keyboard, 'KeyboardGlobal')
        except Exception, e:
            raise Exception('freepie_helper.FreePieTypeCheck.check_keyboard - ' + str(e))

    @staticmethod
    def check_key(key):
        try:
            return FreePieTypeCheck._strict_check(key, 'GlobalIndexer[JoystickGlobal, int, str]')
        except Exception, e:
            raise Exception('freepie_helper.FreePieTypeCheck.check_key - ' + str(e))

    @staticmethod
    def check_joystick(joy):
        try:
            return FreePieTypeCheck._strict_check(joy, 'GlobalIndexer[JoystickGlobal, int, str]')
        except Exception, e:
            raise Exception('freepie_helper.FreePieTypeCheck.check_joystick - ' + str(e))

    @staticmethod
    def check_vjoy(vjoy):
        try:
            return FreePieTypeCheck._strict_check(vjoy, 'GlobalIndexer[VJoyGlobal, UInt32]')
        except Exception, e:
            raise Exception('freepie_helper.FreePieTypeCheck.check_vjoy - ' + str(e))

    @staticmethod
    def check_diagnostics(diagnostics):
        try:
            return FreePieTypeCheck._strict_check(diagnostics, 'DiagnosticHelper')
        except Exception, e:
            raise Exception('freepie_helper.FreePieTypeCheck.check_diagnostics - ' + str(e))

class KeyExtended:
    # Wrap known values
    D0              = KeyFP.D0
    D1              = KeyFP.D1
    D2              = KeyFP.D2
    D3              = KeyFP.D3
    D4              = KeyFP.D4
    D5              = KeyFP.D5
    D6              = KeyFP.D6
    D7              = KeyFP.D7
    D8              = KeyFP.D8
    D9              = KeyFP.D9
    A               = KeyFP.A
    B               = KeyFP.B
    C               = KeyFP.C
    D               = KeyFP.D
    E               = KeyFP.E
    F               = KeyFP.F
    G               = KeyFP.G
    H               = KeyFP.H
    I               = KeyFP.I
    J               = KeyFP.J
    K               = KeyFP.K
    L               = KeyFP.L
    M               = KeyFP.M
    N               = KeyFP.N
    O               = KeyFP.O
    P               = KeyFP.P
    Q               = KeyFP.Q
    R               = KeyFP.R
    S               = KeyFP.S
    T               = KeyFP.T
    U               = KeyFP.U
    V               = KeyFP.V
    W               = KeyFP.W
    X               = KeyFP.X
    Y               = KeyFP.Y
    Z               = KeyFP.Z
    AbntC1          = KeyFP.AbntC1
    AbntC2          = KeyFP.AbntC2
    Apostrophe      = KeyFP.Apostrophe
    Applications    = KeyFP.Applications
    AT              = KeyFP.AT
    AX              = KeyFP.AX
    Backspace       = KeyFP.Backspace
    Backslash       = KeyFP.Backslash
    Calculator      = KeyFP.Calculator
    CapsLock        = KeyFP.CapsLock
    Colon           = KeyFP.Colon
    Comma           = KeyFP.Comma
    Convert         = KeyFP.Convert
    Delete          = KeyFP.Delete
    DownArrow       = KeyFP.DownArrow
    End             = KeyFP.End
    Equals          = KeyFP.Equals
    Escape          = KeyFP.Escape
    F1              = KeyFP.F1
    F2              = KeyFP.F2
    F3              = KeyFP.F3
    F4              = KeyFP.F4
    F5              = KeyFP.F5
    F6              = KeyFP.F6
    F7              = KeyFP.F7
    F8              = KeyFP.F8
    F9              = KeyFP.F9
    F10             = KeyFP.F10
    F11             = KeyFP.F11
    F12             = KeyFP.F12
    F13             = KeyFP.F13
    F14             = KeyFP.F14
    F15             = KeyFP.F15
    Grave           = KeyFP.Grave
    Home            = KeyFP.Home
    Insert          = KeyFP.Insert
    Kana            = KeyFP.Kana
    Kanji           = KeyFP.Kanji
    LeftBracket     = KeyFP.LeftBracket
    LeftControl     = KeyFP.LeftControl
    LeftArrow       = KeyFP.LeftArrow
    LeftAlt         = KeyFP.LeftAlt
    LeftShift       = KeyFP.LeftShift
    LeftWindowsKey  = KeyFP.LeftWindowsKey
    Mail            = KeyFP.Mail
    MediaSelect     = KeyFP.MediaSelect
    MediaStop       = KeyFP.MediaStop
    Minus           = KeyFP.Minus
    Mute            = KeyFP.Mute
    MyComputer      = KeyFP.MyComputer
    NextTrack       = KeyFP.NextTrack
    NoConvert       = KeyFP.NoConvert
    NumberLock      = KeyFP.NumberLock
    NumberPad0      = KeyFP.NumberPad0
    NumberPad1      = KeyFP.NumberPad1
    NumberPad2      = KeyFP.NumberPad2
    NumberPad3      = KeyFP.NumberPad3
    NumberPad4      = KeyFP.NumberPad4
    NumberPad5      = KeyFP.NumberPad5
    NumberPad6      = KeyFP.NumberPad6
    NumberPad7      = KeyFP.NumberPad7
    NumberPad8      = KeyFP.NumberPad8
    NumberPad9      = KeyFP.NumberPad9
    NumberPadComma  = KeyFP.NumberPadComma
    NumberPadEnter  = KeyFP.NumberPadEnter
    NumberPadEquals = KeyFP.NumberPadEquals
    NumberPadMinus  = KeyFP.NumberPadMinus
    NumberPadPeriod = KeyFP.NumberPadPeriod
    NumberPadPlus   = KeyFP.NumberPadPlus
    NumberPadSlash  = KeyFP.NumberPadSlash
    NumberPadStar   = KeyFP.NumberPadStar
    Oem102          = KeyFP.Oem102
    PageDown        = KeyFP.PageDown
    PageUp          = KeyFP.PageUp
    Pause           = KeyFP.Pause
    Period          = KeyFP.Period
    PlayPause       = KeyFP.PlayPause
    Power           = KeyFP.Power
    PreviousTrack   = KeyFP.PreviousTrack
    RightBracket    = KeyFP.RightBracket
    RightControl    = KeyFP.RightControl
    Return          = KeyFP.Return
    RightArrow      = KeyFP.RightArrow
    RightAlt        = KeyFP.RightAlt
    RightShift      = KeyFP.RightShift
    RightWindowsKey = KeyFP.RightWindowsKey
    ScrollLock      = KeyFP.ScrollLock
    Semicolon       = KeyFP.Semicolon
    Slash           = KeyFP.Slash
    Sleep           = KeyFP.Sleep
    Space           = KeyFP.Space
    Stop            = KeyFP.Stop
    PrintScreen     = KeyFP.PrintScreen
    Tab             = KeyFP.Tab
    Underline       = KeyFP.Underline
    Unlabeled       = KeyFP.Unlabeled
    UpArrow         = KeyFP.UpArrow
    VolumeDown      = KeyFP.VolumeDown
    VolumeUp        = KeyFP.VolumeUp
    Wake            = KeyFP.Wake
    WebBack         = KeyFP.WebBack
    WebFavorites    = KeyFP.WebFavorites
    WebForward      = KeyFP.WebForward
    WebHome         = KeyFP.WebHome
    WebRefresh      = KeyFP.WebRefresh
    WebSearch       = KeyFP.WebSearch
    WebStop         = KeyFP.WebStop
    Yen             = KeyFP.Yen
    Unknown         = KeyFP.Unknown

    # Custom attributes

    ArrowAft        = KeyFP.DownArrow
    ArrowDown       = KeyFP.DownArrow
    ArrowForward    = KeyFP.UpArrow
    ArrowLeft       = KeyFP.LeftArrow
    ArrowRight      = KeyFP.RightArrow
    ArrowUp         = KeyFP.UpArrow

    AftArrow        = KeyFP.DownArrow
    ForwardArrow    = KeyFP.UpArrow

    Enter           = Return

    LWin            = LeftWindowsKey
    LWindows        = LeftWindowsKey
    LeftWin         = LeftWindowsKey
    LeftWindows     = LeftWindowsKey

    RWin            = RightWindowsKey
    RWindows        = RightWindowsKey
    RightWin        = RightWindowsKey
    RightWindows    = RightWindowsKey

    LSht            = LeftShift
    LShift          = LeftShift
    LeftSht         = LeftShift

    RSht            = RightShift
    RShift          = RightShift
    RightSht        = RightShift

    LCtl            = LeftControl
    LCtrl           = LeftControl
    LControl        = LeftControl
    LeftCtl         = LeftControl
    LeftCtrl        = LeftControl

    RCtl            = RightControl
    RCtrl           = RightControl
    RControl        = RightControl
    RightCtl        = RightControl
    RightCtrl       = RightControl

    LAlt            = LeftAlt
    RAlt            = RightAlt

    Num0            = NumberPad0
    Num1            = NumberPad1
    Num2            = NumberPad2
    Num3            = NumberPad3
    Num4            = NumberPad4
    Num5            = NumberPad5
    Num6            = NumberPad6
    Num7            = NumberPad7
    Num8            = NumberPad8
    Num9            = NumberPad9

    NumLock         = NumberLock

    NumComma        = NumberPadComma
    NumEnter        = NumberPadEnter
    NumEquals       = NumberPadEquals
    NumMinus        = NumberPadMinus
    NumPeriod       = NumberPadPeriod
    NumPlus         = NumberPadPlus
    NumSlash        = NumberPadSlash
    NumStar         = NumberPadStar

    modifiers = (
        LeftShift,
        LeftControl,
        LeftAlt,
        LeftWindowsKey,

        RightShift,
        RightControl,
        RightAlt,
        RightWindowsKey,
    )

    str_to_var = {
        ':' : Colon,
        ';' : Semicolon,

        '.' : Period,
        ',' : Comma,

        '-' : Minus,
        '=' : Equals,
        "'" : Apostrophe,
        '`' : Grave,
        '/' : Slash,
        '\\' : Backslash,

        '[' : LeftBracket,
        ']' : RightBracket,

        '0' : D0,
        '1' : D1,
        '2' : D2,
        '3' : D3,
        '4' : D4,
        '5' : D5,
        '6' : D6,
        '7' : D7,
        '8' : D8,
        '9' : D9,

        'Num *' : NumberPadStar,
        #'Num +' : NumberPadPlus, # special case to handle
        'Num -' : NumberPadMinus,
        'Num /' : NumberPadSlash,
        'Num .' : NumberPadPeriod,

    }

    @staticmethod
    def is_a_modifier_key(key):
        return True if key in KeyExtended.modifiers else False

    @staticmethod
    def str_split_keys(key_combination_str):
        keys_str = []

        for key_str in key_combination_str.replace(" ", "").split('+'):
            keys_str.append(key_str)

        keys_not_modifiers = []
        keys_modifiers     = []

        for key_str in keys_str:
            key_found     = False
            key_str_lower = key_str.lower()

            for member_str in vars(KeyExtended):
                if key_str_lower == member_str.lower():
                    key_found = True
                    key = eval('KeyExtended.' + member_str)
                    break

                else:

                    for key_dict, val_dict in KeyExtended.str_to_var.iteritems():
                        if key_dict.replace(" ", "").lower() == key_str_lower:
                            key_found = True
                            key = val_dict
                            break

            if key_found:
                if KeyExtended.is_a_modifier_key(key):
                    keys_modifiers.append(key)
                else:
                    keys_not_modifiers.append(key)
            else:
                raise ValueError("Key '{0}' unknown (key combination: '{1}')".format(key_str, key_combination_str))

        return (keys_modifiers, keys_not_modifiers)

class JoystickWrapper:

    def __init__(self, joy, joy_axis_max):
        self.joy = joy
        self.axisMax = joy_axis_max

    @property
    def x(self):
        return self.joy.x

    @property
    def y(self):
        return self.joy.y

    @property
    def z(self):
        return self.joy.z

    @property
    def xRotation(self):
        return self.joy.xRotation

    @property
    def yRotation(self):
        return self.joy.yRotation

    @property
    def zRotation(self):
        return self.joy.zRotation

    @property
    def pov(self):
        return self.joy.pov

    @property
    def sliders(self):
        return self.joy.sliders

    def getDown(self, button):
        return self.joy.getDown(button)

    def getDownPov(self, pov_index, pov_value):
        return self.joy.pov[pov_index] == pov_value

    def getPressed(self, button):
        return self.joy.getPressed(button)

    def setRange(self, lowerRange, upperRange):
        self.joy.setRange(lowerRange, upperRange)

class Debug:

    def __init__(self, diagnostics):
        self.diagnostics = diagnostics
        self.povs_last_val = {}
        self.axes_last_val = {}
        self.is_first_activity_call = True

    def show_joy_activity(self, joy, joy_axis_max):
        if self.is_first_activity_call:
            self.diagnostics.debug("<Debug> Joystick activity watch is ON")
            self.is_first_activity_call = False

        # show all buttons pressed
        for i in range(0, 128):
            if joy.getPressed(i):
                self.diagnostics.debug("<Button " + str(i) + "> Pressed")

        # show all pov "pressed"
        for i in range(0, len(joy.pov)):
            pov_value = joy.pov[i]

            # Skip initial idle state
            if pov_value == -1 and i not in self.povs_last_val:
                continue

            # little trick to show pov value only once
            if i not in self.povs_last_val or self.povs_last_val[i] != pov_value:
                self.povs_last_val[i] = pov_value
                self.diagnostics.debug("<POV " + str(i)  + "> Direction: " + str(pov_value) +  "")

        self.diagnostics.watch('----------------------------------------------------------------------------------------------------------------------------', '-- DEBUG JOYSTICK AXES -----------------------------------------------------------------------------------------------------------------------------------------------------------')
        self.diagnostics.watch("{0}     |     {1}%".format(joy.x, 100.0 * joy.x/joy_axis_max), "Axis X  :")
        self.diagnostics.watch(joy.y, "Axis Y   :")
        self.diagnostics.watch(joy.z, "Axis Z   :")
        self.diagnostics.watch(joy.xRotation, "Axis RX :")
        self.diagnostics.watch(joy.yRotation, "Axis RY :")
        self.diagnostics.watch(joy.zRotation, "Axis RZ :")

        for i in range(0, len(joy.sliders)):
            self.diagnostics.watch(joy.sliders[i], "Axis SLIDER" + str(i) + " :")

        self.diagnostics.watch('----------------------------------------------------------------------------------------------------------------------------', '-- /DEBUG JOYSTICK AXES -----------------------------------------------------------------------------------------------------------------------------------------------------------')

    def watch_joy_vjoy_axis(self, joy, vjoy):
        self.diagnostics.watch(joy.x,         'joy.x')
        self.diagnostics.watch(joy.y,         'joy.y')
        self.diagnostics.watch(joy.zRotation, 'joy.zRotation')
        self.diagnostics.watch(vjoy.x,        'vjoy.x')
        self.diagnostics.watch(vjoy.y,        'vjoy.y')
        self.diagnostics.watch(vjoy.rz,       'vjoy.rz')

def reload_modules_from(script_path):
    import sys, imp

    # Reload our modules in order to acknowledge any modifications.
    for key, value in sys.modules.items():
        if value is not None and script_path in str(value):
            imp.reload(sys.modules[key])
        #diagnostics.debug("key :  " + str(key) + "    |    value :  " + str(value))
        #diagnostics.debug("")

def debug_watch_joy_all(joy, diagnostics):

    # STICK VALUES
    ## Axis
    diagnostics.watch('-------------------------------', '-- STICK ----------------------')
    diagnostics.watch(joy.x, 'joy.x')
    diagnostics.watch(joy.y, 'joy.y')
    diagnostics.watch(joy.zRotation, 'joy.zRotation')

    ## Stick Buttons - 0: INDEX FIRE, 14: INDEX FIRE DEEP, 1: MIDDLE TOP, 2: RIGHT TOP, 3: RIGHT BOTTOM, 4: LEFT BOTTOM, 5: PINKIE
    diagnostics.watch('0: INDEX FIRE, 14: INDEX FIRE DEEP, 1: MIDDLE TOP, 2: RIGHT TOP, 3: RIGHT BOTTOM, 4: LEFT BOTTOM, 5: PINKIE', '-- Stick Buttons')
    diagnostics.watch(joy.getDown(0), 'joy.getDown(0)')
    diagnostics.watch(joy.getDown(14), 'joy.getDown(14)')
    diagnostics.watch(joy.getDown(1), 'joy.getDown(1)')
    diagnostics.watch(joy.getDown(2), 'joy.getDown(2)')
    diagnostics.watch(joy.getDown(3), 'joy.getDown(3)')
    diagnostics.watch(joy.getDown(4), 'joy.getDown(4)')
    diagnostics.watch(joy.getDown(5), 'joy.getDown(5)')

    # Top Hat - 19: UP, 20: RIGHT, 21: DOWN, 22: LEFT
    diagnostics.watch('19: UP, 20: RIGHT, 21: DOWN, 22: LEFT', '-- Top Hat')
    diagnostics.watch(joy.getDown(19), 'joy.getDown(19)')
    diagnostics.watch(joy.getDown(20), 'joy.getDown(20)')
    diagnostics.watch(joy.getDown(21), 'joy.getDown(21)')
    diagnostics.watch(joy.getDown(22), 'joy.getDown(22)')

    # Bottom Hat - NEUTRAL: -1, N: 0, NE: 4500, E: 9000, SE: 13500, S: 18000, SW: 22500, W: 27000, NW: 31500
    diagnostics.watch('NEUTRAL: -1, N: 0, NE: 4500, E: 9000, SE: 13500, S: 18000, SW: 22500, W: 27000, NW: 31500', '-- Bottom Hat')
    diagnostics.watch(joy.pov[0], 'joy.pov[0]')

    # Bottom Switches - 8: LEFT UP, 9: LEFT DOWN, 10: MIDDLE UP, 11: MIDDLE DOWN, 12: RIGHT UP, 13: RIGHT DOWN
    diagnostics.watch('8: LEFT UP, 9: LEFT DOWN, 10: MIDDLE UP, 11: MIDDLE DOWN, 12: RIGHT UP, 13: RIGHT DOWN', '-- Bottom Switches')
    diagnostics.watch(joy.getDown(8), 'joy.getDown(8)')
    diagnostics.watch(joy.getDown(9), 'joy.getDown(9)')
    diagnostics.watch(joy.getDown(10), 'joy.getDown(10)')
    diagnostics.watch(joy.getDown(11), 'joy.getDown(11)')
    diagnostics.watch(joy.getDown(12), 'joy.getDown(12)')
    diagnostics.watch(joy.getDown(13), 'joy.getDown(13)')

    # THROTTLE VALUES
    ## Axis
    diagnostics.watch('-------------------------------', '-- THROTTLE -------------------')
    diagnostics.watch(joy.z, 'joy.z')
    diagnostics.watch(joy.xRotation, 'joy.xRotation')
    diagnostics.watch(joy.yRotation, 'joy.yRotation')
    diagnostics.watch(joy.sliders[0], 'joy.sliders[0]')

    # Thumb Buttons - 6: MIDLE, 7: TOP, 30: BOTTOM
    diagnostics.watch('6: MIDLE, 7: TOP, 30: BOTTOM', '-- Buttons')
    diagnostics.watch(joy.getDown(6), 'joy.getDown(6)')
    diagnostics.watch(joy.getDown(7), 'joy.getDown(7)')
    diagnostics.watch(joy.getDown(30), 'joy.getDown(30)')

    # Hat - 23: DOWN , 24: RIGHT, 25: UP, 26: LEFT
    diagnostics.watch('23: DOWN , 24: RIGHT, 25: UP, 26: LEFT', '-- Hat')
    diagnostics.watch(joy.getDown(23), 'joy.getDown(23)')
    diagnostics.watch(joy.getDown(24), 'joy.getDown(24)')
    diagnostics.watch(joy.getDown(25), 'joy.getDown(25)')
    diagnostics.watch(joy.getDown(26), 'joy.getDown(26)')

    # MFD Buttons - 31: LEFT WHEEL, 32: MIDDLE UP, 33: MIDDLE DOWN, 38: RIGHT WHEEL
    diagnostics.watch('31: LEFT WHEEL, 32: MIDDLE UP, 33: MIDDLE DOWN, 38: RIGHT WHEEL', '-- MFD Buttons')
    diagnostics.watch(joy.getDown(31), 'joy.getDown(31)')
    diagnostics.watch(joy.getDown(32), 'joy.getDown(32)')
    diagnostics.watch(joy.getDown(33), 'joy.getDown(33)')
    diagnostics.watch(joy.getDown(38), 'joy.getDown(38)')

    # MFD Wheels - 34: LEFT WHEEL UP, 35: LEFT WHEEL DOWN, 36: RIGHT WHEEL UP, 37: RIGHT WHEEL DOWN
    diagnostics.watch('34: LEFT WHEEL UP, 35: LEFT WHEEL DOWN, 36: RIGHT WHEEL UP, 37: RIGHT WHEEL DOWN', '-- MFD Wheels')
    diagnostics.watch(joy.getDown(34), 'joy.getDown(34)')
    diagnostics.watch(joy.getDown(35), 'joy.getDown(35)')
    diagnostics.watch(joy.getDown(36), 'joy.getDown(36)')
    diagnostics.watch(joy.getDown(37), 'joy.getDown(37)')

    # Mouse Wheel - 16: WHEEL UP, 17: WHEEL DOWN, 18: WHEEL CLICK
    diagnostics.watch('16: WHEEL UP, 17: WHEEL DOWN, 18: WHEEL CLICK', '-- Mouse Wheel')
    diagnostics.watch(joy.getDown(16), 'joy.getDown(16)')
    diagnostics.watch(joy.getDown(17), 'joy.getDown(17)')
    diagnostics.watch(joy.getDown(18), 'joy.getDown(18)')

    # Mouse Click - 15: CLICK
    diagnostics.watch('15: CLICK', '-- Mouse Click')
    diagnostics.watch(joy.getDown(15), 'joy.getDown(15)')

    # diagnostics.watch('-------------------------------', '-- Other -------------------')
    # diagnostics.watch(joy.pov[1], 'joy.pov[1]')
    # diagnostics.watch(joy.pov[2], 'joy.pov[2]')
    # diagnostics.watch(joy.pov[3], 'joy.pov[3]')
    # diagnostics.watch(joy.getDown(27), 'joy.getDown(27)')
    # diagnostics.watch(joy.getDown(28), 'joy.getDown(28)')
    # diagnostics.watch(joy.getDown(29), 'joy.getDown(29)')
    # diagnostics.watch(joy.getDown(39), 'joy.getDown(39)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(40)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(41)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(42)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(43)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(44)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(45)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(46)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(47)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(48)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(49)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(50)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(51)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(52)')
    # diagnostics.watch(joy.getDown(40), 'joy.getDown(53)')

class AppInformation:

    # The name of the .NET installation on which the app is running
    framwork   = System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription
    os_version = System.Runtime.InteropServices.RuntimeInformation.OSDescription

    # This script was developed on FreePie version: 1.11.724.0
    app_version = System.Reflection.Assembly.GetEntryAssembly().GetName().Version

def throw_error(exception, error_message, diagnostics, notify_message):
    diagnostics.notify(notify_message)
    raise exception(error_message)