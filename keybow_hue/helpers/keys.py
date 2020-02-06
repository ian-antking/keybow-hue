import colorsys

def convert_hue_color(hue, saturaton, brightness):
    color = colorsys.hsv_to_rgb(hue / 65535, saturaton / 254, brightness / 254)
    return [int(value * 255) for value in color]

def generate_keybow_color(hue, saturaton, brightness):
    color = colorsys.hsv_to_rgb(hue, saturaton, brightness)
    return [int(value * 255) for value in color]

def build_power_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.toggle_on_off, lambda: (0, 255, 0) if room.get_state('on') else (25, 0, 0))

def build_dimmer_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.dim, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat'), room.get_state('bri') - 50) if room.get_state('on') else [0] * 3))

def build_bright_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.bright, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat'), room.get_state('bri') + 50) if room.get_state('on') else [0] * 3))

def build_increase_sat_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.increase_sat, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat') + 50, 254) if room.get_state('on') else [0] * 3))

def build_decrease_sat_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.decrease_sat, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat') - 50, 254) if room.get_state('on') else [0] * 3))

def build_increase_hue_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.increase_hue, lambda: (convert_hue_color(room.get_state('hue') + 6553, 254, 254) if room.get_state('on') else [0] * 3))

def build_decrease_hue_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.decrease_hue, lambda: (convert_hue_color(room.get_state('hue') - 6553, 254, 254) if room.get_state('on') else [0] * 3))

def build_hue_indicator(room, keyboard, key_index):
    return keyboard.Key(key_index, room.update_room, lambda: (convert_hue_color(room.get_state('hue'), 254, 254) if room.get_state('on') else [0] * 3))

def build_saturation_indicator(room, keyboard, key_index):
    return keyboard.Key(key_index, room.update_room, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat'), 254) if room.get_state('on') else [0] * 3))

def build_blank_button(room, keyboard, key_index):
    return keyboard.Key(key_index, room.update_room, lambda: (convert_hue_color(room.get_state('hue'), room.get_state('sat'), room.get_state('bri')) if room.get_state('on') else [0] * 3))

def build_mode_button(engine, room, keyboard, key_index):
    return keyboard.Key(key_index, engine.change_mode, lambda: generate_keybow_color(engine.mode % len(engine.keyboards)/10,1,1) if room.get_state('on') else [0] * 3)
