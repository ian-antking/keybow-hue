from nose.tools import assert_true
from keyboard import Keyboard

class Key:
    def __init__(self, index):
        self.index = index
        self.action = 'mockAction'
        self.color = 'mockColor'

def test_add_key():
    keyboard = Keyboard()

    key = Key(0)
    keyboard.add_key(key)
    assert_true(keyboard.keys[0] == key)

def test_get_key():
    keyboard = Keyboard()
    key_zero = Key(0)
    key_one = Key(1)
    key_two = Key(2)

    keyboard.add_key(key_zero)
    keyboard.add_key(key_one)
    keyboard.add_key(key_two)

    assert_true(keyboard.get_key(1) == key_one)