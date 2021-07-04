import time
from abc import ABCMeta, abstractmethod
from src.utils.utilities import tuple_it_if_needed

class ICommand(object):
    __metaclass__ = ABCMeta

    def __init__(self, is_press = False):
        self._is_press = is_press

    def is_press(self):
        self._is_press

    @abstractmethod
    def hold(self):
        pass

    @abstractmethod
    def release(self):
        pass

    def press(self):
        self.hold()
        time.sleep(0.03)
        self.release()

class BundleCommand(ICommand):
    def __init__(self, commands):
        super(BundleCommand, self).__init__()

        self.commands = tuple_it_if_needed(commands)

    def hold(self):
        for command in self.commands:
            command.hold()

    def release(self):
        for command in self.commands:
            command.release()

class VjoyBtnCommand(ICommand):

    def __init__(self, vjoy, btn):
        super(VjoyBtnCommand, self).__init__()

        self.vjoy       = vjoy
        self.btn        = btn

    def hold(self):
        self.vjoy.setButton(self.btn, True)

    def release(self):
        self.vjoy.setButton(self.btn, False)

class VjoyPovCommand(ICommand):

    def __init__(self, vjoy, pov_index, cardinal):
        super(VjoyPovCommand, self).__init__()

        self.vjoy       = vjoy
        self.pov_index  = pov_index
        self.cardinal   = cardinal

    def hold(self):
        self.vjoy.setAnalogPov(self.pov_index, self.cardinal)

    def release(self):
        self.vjoy.setAnalogPov(self.pov_index, -1)

class KeybCommand(ICommand):

    def __init__(self, keyboard, keyb_modifiers, keyb_key):
        super(KeybCommand, self).__init__()

        self.keyboard = keyboard
        self.keyb_modifiers = tuple_it_if_needed(keyb_modifiers)
        self.keyb_key = tuple_it_if_needed(keyb_key)

    def _hold_keyb_modifiers(self):
        for keyb_modifier in self.keyb_modifiers:
            self.keyboard.setKeyDown(keyb_modifier)

    def _release_keyb_modifiers(self):
        for keyb_modifier in self.keyb_modifiers:
            self.keyboard.setKeyUp(keyb_modifier)

    def _hold_keyb_key(self):
        for keyb_key in self.keyb_key:
            self.keyboard.setKeyDown(keyb_key)

    def _release_keyb_key(self):
        for keyb_key in self.keyb_key:
            self.keyboard.setKeyUp(keyb_key)

    def hold(self):
        self._hold_keyb_modifiers()
        # mandatory to register correctly the modifiers in-game
        time.sleep(0.03)
        self._hold_keyb_key()

    def release(self):
        self._release_keyb_key()
        self._release_keyb_modifiers()

class SequenceRotateCommand(ICommand):
    def __init__(self, commands):
        super(SequenceRotateCommand, self).__init__()

        self.cur_index = 0
        self.max_index = len(commands) - 1
        self.commands  = tuple_it_if_needed(commands)

    def _index_incr(self):
        if self.cur_index == self.max_index:
            self.cur_index = 0
        else:
            self.cur_index += 1

    def hold(self):
        self.commands[self.cur_index].hold()

    def release(self):
        self.commands[self.cur_index].release()
        self._index_incr()

class SequenceCommand(ICommand):
    def __init__(self, commands):
        super(SequenceCommand, self).__init__(True)

        self.commands   = tuple_it_if_needed(commands)
        self.is_on_hold = False

    def hold(self):
        if not self.is_on_hold:
            for command in self.commands:
                command.press()

            self.is_on_hold = True

    def release(self):
        self.is_on_hold = False

    def press(self):
        for command in self.commands:
                command.press()

# class SequenceCommand(ICommand):

#     def __init__(self, rotate, commands):
#         self.cur_index = 0
#         self.max_index = len(commands) - 1

#         self.rotate   = rotate
#         self.commands = tuple_it_if_needed(commands)

#     def _index_incr(self):
#         if self.cur_index == self.max_index:
#             self.cur_index = 0
#         else:
#             self.cur_index += 1

#     def hold(self):
#         if self.rotate:
#             self.commands[self.cur_index].hold()
#         else:
#             for command in self.commands:
#                 command.hold()

#     def release(self):
#         if self.rotate:
#             self.commands[self.cur_index].release()
#             self._index_incr()
#         else:
#             for command in self.commands:
#                 command.release()

# class SequenceMixCommand(ICommand):
#     def __init__(self, rotational_sequences, no_rotational_sequence):
#         super(SequenceMixCommand, self).__init__()

#         # check if is SequenceCommand, check is rotate or not
#         self.rot_seqs   = rotational_sequences
#         self.no_rot_seq = no_rotational_sequence

#     def hold(self):
#         for rot_seq in self.rot_seqs:
#             rot_seq.hold()

#         no_rot_seq.hold()

#     def release(self):
#         for rot_seq in self.rot_seqs:
#             rot_seq.hold()

#         no_rot_seq.release()

def combine_commands(*commands):
    bundle_cmds = []

    for command in commands:
        if isinstance(command, (VjoyBtnCommand, VjoyPovCommand, KeybCommand, SequenceCommand, SequenceRotateCommand,  BundleCommand)):
            bundle_cmds.append(command)
        else:
            raise ValueError("Combining commands failed: there's a unknown command type ({}, val ={}).".format(type(command), command))

    if len(bundle_cmds) == 1:
        return bundle_cmds[0]

    else:
        return BundleCommand(tuple_it_if_needed(bundle_cmds))



