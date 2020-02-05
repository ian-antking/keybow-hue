import colorsys

def build_power_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.toggle_on_off, lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0))

def build_dimmer_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.dim, lambda: [room.get_state('bri') - 50] * 3 if room.get_state('on') else [0] * 3)

def build_bright_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.bright, lambda: [room.get_state('bri') + 50] * 3 if room.get_state('on') else [0] * 3)

def build_increase_hue_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.increase_hue, lambda: colorsys.hsv_to_rgb(360 * (int((room.get_state('hue') + 6553) / 65535)), int(room.get_state('sat') / 254), int(room.get_state('bri') / 254)))

def build_decrease_hue_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.decrease_hue, lambda: colorsys.hsv_to_rgb(360 * (int((room.get_state('hue') - 6553) / 65535)), int(room.get_state('sat') / 254), int(room.get_state('bri') / 254)))