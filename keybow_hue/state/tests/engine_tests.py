from nose.tools import assert_true
from state import Engine

class Keyboard():
    def __init__(self):
        self.keys = []

def test_add_keyboard():
    engine = Engine()
    keyboard = Keyboard()
    engine.add_keyboard(keyboard)
    assert_true(engine.keyboards[0] == keyboard)

def test_get_keyboard__returns_same_keyboard_as_mode_0():
    engine = Engine()
    keyboard_zero = Keyboard()
    keyboard_zero.keys.append('mock_keys_zero')
    keyboard_one = Keyboard()
    keyboard_one.keys.append('mock_keys_one')
    engine.add_keyboard(keyboard_zero)
    engine.add_keyboard(keyboard_one)
    assert_true(engine.get_keyboard() == keyboard_zero)

def test_get_keyboard__returns_same_keyboard_as_mode_1():
    engine = Engine()
    keyboard_zero = Keyboard()
    keyboard_zero.keys.append('mock_keys_zero')
    keyboard_one = Keyboard()
    keyboard_one.keys.append('mock_keys_one')
    engine.add_keyboard(keyboard_zero)
    engine.add_keyboard(keyboard_one)
    engine.change_mode()
    assert_true(engine.get_keyboard() == keyboard_one)

def test_get_keyboard__wraps_round_to_keyobord_zero():
    engine = Engine()
    keyboard_zero = Keyboard()
    keyboard_zero.keys.append('mock_keys_zero')
    keyboard_one = Keyboard()
    keyboard_one.keys.append('mock_keys_one')
    engine.add_keyboard(keyboard_zero)
    engine.add_keyboard(keyboard_one)
    engine.change_mode()
    engine.change_mode()
    assert_true(engine.get_keyboard() == keyboard_zero)