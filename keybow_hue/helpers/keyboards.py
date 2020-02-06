from . import *

def generate_keyboards(room, keyboard, state_engine):
    keyboard_one = keyboard.Keyboard()
    keyboard_one.add_key(build_bright_button(room, keyboard, 0))
    keyboard_one.add_key(build_blank_button(room, keyboard, 3))
    keyboard_one.add_key(build_dimmer_button(room, keyboard, 6))

    keyboard_one.add_key(build_increase_sat_button(room, keyboard, 1))
    keyboard_one.add_key(build_saturation_indicator(room, keyboard, 4))
    keyboard_one.add_key(build_decrease_sat_button(room, keyboard, 7))

    keyboard_one.add_key(build_increase_hue_button(room, keyboard, 2))
    keyboard_one.add_key(build_hue_indicator(room, keyboard, 5))
    keyboard_one.add_key(build_decrease_hue_button(room, keyboard, 8))

    keyboard_one.add_key(build_blank_button(room, keyboard, 9))
    keyboard_one.add_key(build_mode_button(state_engine, room, keyboard, 10))
    keyboard_one.add_key(build_power_button(room, keyboard, 11))

    keyboard_two = keyboard.Keyboard()
    keyboard_two.add_key(build_mode_button(state_engine, room, keyboard, 10))
    keyboard_two.add_key(build_power_button(room, keyboard, 11))
    
    state_engine.add_keyboard(keyboard_one)
    state_engine.add_keyboard(keyboard_two)