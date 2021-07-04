import src.mapping.joy_mapping_orchestration
import src.mapping.composite.actions
import src.mapping.composite.axis
import src.mapping.composite.commands

import src.utils.filters

from src.utils.utilities           import Bunch, tuple_it_if_needed
from src.helpers.freepie_helper    import KeyExtended
from src.helpers.cardinal_type     import CardinalType
from src.helpers.axis_type         import AxisType

from src.client.models.joy_buttons import JoyBtnData, JoyBtnRef
from src.client.models.joy_povs    import JoyPovData, JoyPovCardinalRef
from src.client.models.joy_axes    import JoyAxisData
from src.client.models.actions     import ActionData, SequenceCommandData, ThresholdActionData
from src.client.models.vjoy        import VJoyIndexRefManager, TransferRange, VJoyBtnRef, VJoyPovCardinalRef

from src.helpers.freepie_vars import FreePieVars

class BtnsPovsAxesActionBundle(object):
    def __init__(self):
        self.btns_action            = []
        self.povs_action            = []
        self.axes_thresholds_action = []

class JoystickMappingClient(object):

    class Builder(object):

        def __init__(self, joy_name, joy_axis_max):
            self.joy_name          = joy_name
            self.joy_axis_max      = joy_axis_max

            self.buttons_data = set()
            self.povs_data    = set()
            self.axes_data    = set()

        def button(self, number):
            return Bunch(
                map_to     = lambda *actions : self._button_map(number, actions = actions),
                command_of = lambda modifiers: self._button_command_of(number, modifiers = modifiers)
            )

        def _button_map(self, number, actions):
            if type(number) is not int:
                raise ValueError("The button number specified for mapping is not an int (specified: {})".format(str(number)))

            button_data = JoyBtnData(number)

            if button_data in self.buttons_data:
                raise RuntimeError("The button {} was already mapped once!".format(number))

            self.buttons_data.add(button_data.map_to(*actions))

        def _button_command_of(self, number, modifiers):
            return JoyBtnData.command_of(number, modifiers)

        def pov(self, index):
            return Bunch(
                cardinal = lambda cardinal_val: self._pov_cardinal(index, cardinal_val)
            )

        def _pov_cardinal(self, index, cardinal):
            return Bunch(
                map_to     = lambda *actions : self._pov_cardinal_map(index, cardinal, actions = actions),
                command_of = lambda modifiers: self._pov_cardinal_command_of(index, cardinal, modifiers = modifiers)
            )

        def _pov_cardinal_map(self, index, cardinal, actions):
            if type(index) is not int:
                raise ValueError("The pov index specified for mapping is not an int (specified: {})".format(str(index)))

            pov_data = JoyPovData(index, cardinal)

            if pov_data in self.povs_data:
                raise RuntimeError("The pov {}  with index {} was already mapped once!".format(index, cardinal))

            self.povs_data.add(pov_data.map_to(*actions))

        def _pov_cardinal_command_of(self, index, cardinal, modifiers):
            return JoyPovData.command_of(index, cardinal, modifiers)

        def axis(self, axis):
            return Bunch(
                map_to = lambda *vjoys_axes_refs : self._axis_map(axis, vjoys_axes_refs = vjoys_axes_refs)
            )

        def _axis_map(self, axis, vjoys_axes_refs):
            if type(axis) is not str:
                raise ValueError("The axis specified for mapping is not a string (specified: {})".format(str(axis)))

            axis_data = JoyAxisData(axis)

            if axis_data in self.axes_data:
                raise RuntimeError("The axis {} was already mapped once!".format(axis))

            self.axes_data.add(axis_data.map_to(*vjoys_axes_refs))

        # TODO: check compilation of commands, tuple of commands (press hold all) vs sequence no rotate (press release each)
        # TODO: Before anything, make sure joy is not None (joystick with name not found) and for each vjoy[index] make sur is not none
        def build(self, joys, vjoys, keyboard, speech):

            joy = joys[self.joy_name]

            if joy is None:
                raise RuntimeError("The joystick with name '{}' was not found.".format(self.joy_name))

            # (3,2,1): BtnsPovsAxesActionBundle
            joy_btns_action_dict = {}
            joy_povs_action_dict = {}
            joy_axes_thresholds_action_dict = {}

            self._build_process_btns(joy, vjoys, keyboard, speech, joy_btns_action_dict)
            self._build_process_povs(joy, vjoys, keyboard, speech, joy_povs_action_dict)
            self._build_process_axes_thresholds(joy, vjoys, keyboard, speech, joy_axes_thresholds_action_dict)

            all_modifiers = set()

            for modifiers in joy_btns_action_dict:
                all_modifiers.add(modifiers)

            for modifiers in joy_povs_action_dict:
                all_modifiers.add(modifiers)

            for modifiers in joy_axes_thresholds_action_dict:
                all_modifiers.add(modifiers)

            joy_modifiers_actions_final = []

            for modifiers in all_modifiers:
                btns_action = []
                povs_action = []
                axes_thresholds_action = []

                if modifiers in joy_btns_action_dict:
                    btns_action = joy_btns_action_dict[modifiers]

                if modifiers in joy_povs_action_dict:
                    povs_action = joy_povs_action_dict[modifiers]

                if modifiers in joy_axes_thresholds_action_dict:
                    axes_thresholds_action = joy_axes_thresholds_action_dict[modifiers]

                joy_modifiers_actions_final.append(src.mapping.composite.actions.JoyModifiersAction(joy, modifiers, btns_action, povs_action, axes_thresholds_action))

            joy_axes_transfer = []
            self._build_process_axes_transfers(joy, vjoys, keyboard, speech, joy_axes_transfer)

            return src.mapping.joy_mapping_orchestration.JoyMapping(joy_modifiers_actions_final, joy_axes_transfer)

        def _build_command(self, command, vjoys, keyboard):

            command_final = []

            cmd = command

            if isinstance(cmd, str):
                command_final.append(src.mapping.composite.commands.KeybCommand(keyboard, *KeyExtended.str_split_keys(cmd)))

            elif isinstance(cmd, VJoyBtnRef):
                command_final.append(src.mapping.composite.commands.VjoyBtnCommand(vjoys[cmd.vjoy_index], cmd.button))

            elif isinstance(cmd, VJoyPovCardinalRef):
                command_final.append(src.mapping.composite.commands.VjoyPovCommand(vjoys[cmd.vjoy_index], cmd.pov_index, CardinalType.retrieve_value_from(cmd.cardinal)))

            elif isinstance(cmd, SequenceCommandData):
                sequence_commands = []

                for c in cmd.commands:
                    sequence_commands.append(self._build_command(c, vjoys, keyboard))

                sequence_commands = tuple_it_if_needed(sequence_commands)

                if cmd.is_rotate_activated:
                    command_final.append(src.mapping.composite.commands.SequenceRotateCommand(sequence_commands))

                else:
                    command_final.append(src.mapping.composite.commands.SequenceCommand(sequence_commands))

            else:
                raise ValueError("Build command: could not process the command of unknown type '{}' (val: {}).".format(type(command), command))

            if len(command_final) == 0:
                raise RuntimeError("Build command: could not figure out the final command.")

            elif len(command_final) == 1:
                return command_final[0]

            else:
                return tuple_it_if_needed(command_final)
                #return src.mapping.composite.commands.BundleCommand(tuple_it_if_needed(command_final))

        def _build_copy_command_lookup(self, copy_command_ref):
            if isinstance(copy_command_ref, JoyBtnRef):
                for button_data in self.buttons_data:
                    if button_data.button == copy_command_ref.button:
                       action = button_data.get_action_tied_to_modifiers(copy_command_ref.modifiers)

                       if action is not None:
                           return action.command

                raise RuntimeError("Build: a 'copy_command' element could not find the associated command (button: {}, modifiers: {}).".format(copy_command_ref.button, copy_command_ref.modifiers))

            elif isinstance(copy_command_ref, JoyPovCardinalRef):
                for pov_data in self.povs_data:
                    if pov_data.pov_index == copy_command_ref.pov_index and pov_data.cardinal == copy_command_ref.cardinal:
                       action = pov_data.get_action_tied_to_modifiers(copy_command_ref.modifiers)

                       if action is not None:
                           return action.command

                raise RuntimeError("Build: a 'copy_command' element could not find the associated command (pov index: {}, cardinal: {}, modifiers: {}).".format(copy_command_ref.pov_index, copy_command_ref.cardinal, copy_command_ref.modifiers))

        def _build_action_final_command(self, vjoys, keyboard, action_data):
            # gather all commands from 'command' and 'copy_commands' to make a single command later (multiple commands are translated into a sequence)
            commands = []

            if action_data.command is not None:
                for cmd in tuple_it_if_needed(action_data.command):
                    commands.append(self._build_command(cmd, vjoys, keyboard))

            if action_data.copy_commands is not None:

                for copy_command_ref in action_data.copy_commands:

                    for cmd in tuple_it_if_needed(self._build_copy_command_lookup(copy_command_ref)):
                        commands.append(self._build_command(cmd, vjoys, keyboard))

            if len(commands) == 0:
                raise RuntimeError("Build: an action could not create a final command, both 'command' and 'copy_command' were None (action's label: {}, joy_modifiers: {}).".format(action_data.label, action_data.joy_modifiers))

            commands = tuple_it_if_needed(commands)

            return src.mapping.composite.commands.combine_commands(*commands)

        def _build_process_btns(self, joy, vjoys, keyboard, speech, joy_modifiers_to_btns):

             for button_data in self.buttons_data:
                if not isinstance(button_data.button, int):
                    raise ValueError("Build Button: A button must be an int (specified: {}).".format(button))

                if button_data.actions is None:
                    raise RuntimeError("Build Button: The joystick button {} have no actions mapped.".format(button_data.button))

                for action_data in button_data.actions:

                    if action_data.joy_modifiers not in joy_modifiers_to_btns:
                        joy_modifiers_to_btns[action_data.joy_modifiers] = []

                    joy_modifiers_to_btns[action_data.joy_modifiers].append(
                        src.mapping.composite.actions.JoyBtnAction(
                            joy, button_data.button, src.mapping.composite.actions.FlaggedAction(
                                action_data.label,
                                action_data.speech_text,
                                self._build_action_final_command(vjoys, keyboard, action_data),
                                speech
                            )
                        )
                    )

        def _build_process_povs(self, joy, vjoys, keyboard, speech, joy_povs_action_dict):

            for pov_data in self.povs_data:
                if not isinstance(pov_data.pov_index, int):
                    raise ValueError("Build Button: A pov index must be an int (specified: {}).".format(button))

                if pov_data.actions is None:
                    raise RuntimeError("Build Button: The joystick pov {} with cardinal {} have no actions mapped.".format(pov_data.button, pov_data.cardinal))

                for action_data in pov_data.actions:

                    if action_data.joy_modifiers not in joy_povs_action_dict:
                        joy_povs_action_dict[action_data.joy_modifiers] = []

                    joy_povs_action_dict[action_data.joy_modifiers].append(
                        src.mapping.composite.actions.JoyPovAction(
                            joy, pov_data.pov_index, pov_data.cardinal, src.mapping.composite.actions.FlaggedAction(
                                action_data.label,
                                action_data.speech_text,
                                self._build_action_final_command(vjoys, keyboard, action_data),
                                speech
                            )
                        )
                    )

        def _build_process_axes_thresholds(self, joy, vjoys, keyboard, speech, joy_axes_thresholds_action_dict):
            for joy_axis_data in self.axes_data:
                break

        def _build_process_axes_transfers(self, joy, vjoys, keyboard, speech, joy_axes_transfer):

            for axis_data in self.axes_data:

                vjoy_axes_transfers = []

                if axis_data.vjoys_axes_refs is None:
                    raise RuntimeError("Build Axes: The joystick axis {} have no vjoy to transfer to.".format(axis_data.axis))

                for vjoy_axis_ref in axis_data.vjoys_axes_refs:

                    if vjoy_axis_ref.curve_filters is None and vjoy_axis_ref.invert is False:
                        axis_filter_final = None
                    else:
                        filters = () if vjoy_axis_ref.curve_filters is None else vjoy_axis_ref.curve_filters
                        axis_filter_final = src.mapping.composite.axis.AxisFilter(
                            filters,
                            vjoy_axis_ref.invert
                        )

                    if vjoy_axis_ref.transfer_range is None:
                        transfer_final = None
                    else:
                        transfer_final = src.mapping.composite.axis.TransferRange(
                            vjoy_axis_ref.transfer_range.joy_min,
                            vjoy_axis_ref.transfer_range.joy_max,
                            vjoy_axis_ref.transfer_range.vjoy_min,
                            vjoy_axis_ref.transfer_range.vjoy_max,
                            self.joy_axis_max,
                            vjoys[vjoy_axis_ref.vjoy_index].axisMax
                        )

                    vjoy_axes_transfers.append(
                        src.mapping.composite.axis.VJoyAxisTransfer(
                            src.mapping.composite.axis.VJoyAxisManager(
                                vjoys[vjoy_axis_ref.vjoy_index],
                                vjoy_axis_ref.axis
                            ),
                            axis_filter = axis_filter_final,
                            transfer_range = transfer_final
                        )
                    )

                if len(vjoy_axes_transfers) == 2:
                    second = vjoy_axes_transfers[1].transfer_range

                joy_axes_transfer.append(
                    src.mapping.composite.axis.JoyAxisTransfer(
                        joy, self.joy_axis_max, axis_data.axis, vjoy_axes_transfers
                    )
                )

Filter = src.utils.filters.Filter

def joy(name, axis_max):
    return JoystickMappingClient.Builder(name, axis_max)

def vjoy(index):
    return VJoyIndexRefManager.get_at_index(index)

def action(*args, **kwargs):
    return ActionData(*args, **kwargs)

def threshold(value):
    return ThresholdActionData(value)

sequence = Bunch(
    rotate = lambda is_sequence_a_rotation: SequenceCommandData(is_sequence_a_rotation)
)

transfer = Bunch(
    from_joy = lambda joy_min_percent, joy_max_percent: TransferRange().from_joy(joy_min_percent, joy_max_percent)
)