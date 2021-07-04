# from profile to internal joy mapping

from src.helpers.freepie_vars import FreePieVars
#joy = FreePieVars.joysticks["X52 Professional H.O.T.A.S."]
#vjoy = FreePieVars.vjoys[0]

from src.helpers.axis_type import AxisType

from src.mapping.composite.axis import JoyAxisTransfer, VJoyAxisManager, TransferRange, AxisFilter, VJoyAxisTransfer

from src.mapping.composite.commands import KeybCommand, SequenceCommand, VjoyBtnCommand, VjoyPovCommand, BundleCommand, SequenceRotateCommand, combine_commands

from src.mapping.composite.actions import JoyModifiersAction, JoyBtnAction, JoyPovAction, AxisThresholdAction, FlaggedAction

from src.mapping.joy_mapping_orchestration import JoyMapping
from src.helpers.freepie_helper import JoystickWrapper

from src.utils.filters import LowPassFilter, CurveFilter

def client_to_internal_mapping(client_joy):
    # client_joy type check
    pass

def _test_internal_mapping(joy, vjoys, speech, keyboard, Key):

    if joy is None:
        raise RuntimeError("Joystick doesn't exist!")

    joy = JoystickWrapper(joy, 1000)

    joy_modifiers_actions = []

    # joy_modifiers_actions.append(
    #     JoyModifiersAction(joy, (6),
    #         [
    #             JoyBtnAction(joy, 0, FlaggedAction(
    #                     "Some test",
    #                     "",
    #                     command = VjoyBtnCommand(vjoys[0], 9),
    #                     speech = speech
    #                 )
    #             )
    #         ],
    #         [

    #         ],
    #         [

    #         ]
    #     )
    # )

    joy_modifiers_actions.append(
        JoyModifiersAction(joy, (),
            [
                JoyBtnAction(joy, 3, FlaggedAction(
                        "Some test",
                        "Sequence: Next",
                        command = SequenceRotateCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 1, FlaggedAction(
                        "Some test",
                        "",
                        command = SequenceCommand(commands = (
                                KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                                KeybCommand(keyboard, (Key.LeftShift), (Key.B))
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 2, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 4, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 5, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 6, FlaggedAction(
                        "Some test",
                        "",
                        command = VjoyBtnCommand(vjoys[0], 7),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 7, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 8, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 9, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 10, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 11, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 12, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 13, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 14, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 15, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 16, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 17, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 18, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 19, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 20, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 21, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 22, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 23, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 24, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 25, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 26, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 27, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 28, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 29, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 30, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 31, FlaggedAction(
                        "Some test",
                        "",
                        command = VjoyBtnCommand(vjoys[0], 32),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 32, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 33, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 34, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 35, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 36, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                ),

                JoyBtnAction(joy, 37, FlaggedAction(
                        "Some test",
                        "",
                        command = KeybCommand(keyboard, (Key.LeftShift), (Key.A)),
                        speech = speech
                    )
                )
            ],
            [
                JoyPovAction(joy, 0, 9000, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 4500, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 13500, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 22500, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 2700, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 315, FlaggedAction(
                        "Some test",
                        "Sequence: All in",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 0, FlaggedAction(
                        "Some test",
                        "",
                        command = BundleCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 51),
                                VjoyPovCommand(vjoys[0], 3, 27000)
                            )
                        ),
                        speech = speech
                    )
                ),

                JoyPovAction(joy, 0, 18000, FlaggedAction(
                        "Some test",
                        "",
                        command = combine_commands(
                                VjoyBtnCommand(vjoys[0], 23),
                                SequenceRotateCommand(commands = (
                                    VjoyBtnCommand(vjoys[0], 22),
                                    VjoyPovCommand(vjoys[0], 2, 27000)
                                )
                            )
                        ),
                        speech = speech
                    )
                )
            ],
            [
                AxisThresholdAction(
                    VJoyAxisManager(vjoys[0], AxisType.X),
                    20,
                    'up',
                    FlaggedAction(
                        "Some test",
                        "x: 20 percent above",
                        command = SequenceCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 46),
                                VjoyPovCommand(vjoys[0], 3, 18000)
                            )
                        ),
                        speech = speech
                    )
                ),

                AxisThresholdAction(
                    VJoyAxisManager(vjoys[0], AxisType.X),
                    20,
                    'down',
                    FlaggedAction(
                        "Some test",
                        "X: 20 percent below",
                        command = BundleCommand(commands = (
                                VjoyBtnCommand(vjoys[0], 1),
                                VjoyBtnCommand(vjoys[0], 0)
                            )
                        ),
                        speech = speech
                    )
                )
            ]
        )
    )

    joy_modifiers_actions.append(
        JoyModifiersAction(joy, (30, 6),
            [
                JoyBtnAction(joy, 2, FlaggedAction(
                        "Some test",
                        "",
                        command = VjoyPovCommand(vjoys[0], 1, 4500),
                        speech = speech
                    )
                )
            ],
            [

            ],
            [

            ]
        )
    )


    joy_axes_transfer = []

    linear_curve_dz = CurveFilter(

        max_value    = 1000,
        deadzone     = 2.3,
        saturation_x = 100,
        saturation_y = 100,
        curvature    = 5

    )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.X, (
                VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.X), axis_filter = AxisFilter(linear_curve_dz, invert=False)),
            )
        )
    )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.Y, (
                VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.Y), axis_filter = AxisFilter(linear_curve_dz, invert=False)),
            )
        )
    )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.Z, (
                VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.Z), axis_filter = AxisFilter(linear_curve_dz, invert=False)),
            )
        )
    )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.RX, (
                VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.RX), axis_filter = AxisFilter(linear_curve_dz, invert=False)),
            )
        )
    )

    # joy_axes_transfer.append(
    #     JoyAxisTransfer(
    #         joy, 1000, AxisType.RY, (
    #             VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.RY), axis_filter = AxisFilter(linear_curve_dz, invert=False)),
    #         )
    #     )
    # )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.RZ, (
                VJoyAxisTransfer(
                    VJoyAxisManager(vjoys[0], AxisType.RZ),
                    axis_filter = AxisFilter(
                        linear_curve_dz,
                        invert=False
                    ),
                    transfer_range = TransferRange(-100, 0, -100, 0, 1000, vjoys[0].axisMax)
                ),

                VJoyAxisTransfer(
                    VJoyAxisManager(vjoys[0], AxisType.Y),
                    axis_filter = AxisFilter(
                        linear_curve_dz,
                        invert=False
                    ),
                    transfer_range = TransferRange(-100, -50, 50, 100, 1000, vjoys[0].axisMax)
                )
            )
        )
    )

    joy_axes_transfer.append(
        JoyAxisTransfer(
            joy, 1000, AxisType.SLIDER1, (
                VJoyAxisTransfer(VJoyAxisManager(vjoys[0], AxisType.SLIDER1), axis_filter = AxisFilter(
                        (linear_curve_dz,
                        LowPassFilter()),
                        invert=True
                    ),
                    transfer_range = TransferRange(-100, 100, 0, 100, 1000, vjoys[0].axisMax)
                ),
            )
        )
    )

    return JoyMapping(joy_modifiers_actions, joy_axes_transfer)