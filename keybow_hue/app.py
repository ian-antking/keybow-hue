#!/usr/bin/env python
from constants import DISCOVERY_URL

class App():
    def __init__(self, room, state, led_controller):

        self.room = room
        self.state = state
        self.led_controller = led_controller
        self.update_leds()

    def validate_brightness(self, brightness):
        if brightness >= 255:
            return 255
        if brightness <= 0:
            return 0
        return brightness

    def validate_color(self, color=[]):
        validated_color = []
        for value in color:
            validated_color.append(self.validate_brightness(value))
        return validated_color

    def update_leds(self):
        for key in self.state.get_keyboard().keys:
            color = self.validate_color(self.state.get_keyboard().get_key(key.index).color())
            self.led_controller.set_led(key.index, *color)

    def execute_action(self, key):
        keyboard = self.state.get_keyboard()
        key = keyboard.get_key(key)
        key.action()

if __name__ == '__main__':
    import keybow
    import keyboard
    import shutdown
    import hue
    import time
    import config
    import state
    import helpers
    
    conf = config.Env(['HUE_TOKEN', 'ROOM_NAME'])
    room = hue.Room(conf.env['ROOM_NAME'], hue.Bridge(conf.env['HUE_TOKEN'], DISCOVERY_URL))

    keyboard_one = keyboard.Keyboard()
    state_engine = state.Engine()

    keyboard_one.add_key(helpers.keys.build_bright_button(room, keyboard, 0))
    keyboard_one.add_key(helpers.keys.build_blank_button(room, keyboard, 3))
    keyboard_one.add_key(helpers.keys.build_dimmer_button(room, keyboard, 6))

    keyboard_one.add_key(helpers.keys.build_increase_sat_button(room, keyboard, 1))
    keyboard_one.add_key(helpers.keys.build_saturation_indicator(room, keyboard, 4))
    keyboard_one.add_key(helpers.keys.build_decrease_sat_button(room, keyboard, 7))

    keyboard_one.add_key(helpers.keys.build_increase_hue_button(room, keyboard, 2))
    keyboard_one.add_key(helpers.keys.build_hue_indicator(room, keyboard, 5))
    keyboard_one.add_key(helpers.keys.build_decrease_hue_button(room, keyboard, 8))

    keyboard_one.add_key(helpers.keys.build_blank_button(room, keyboard, 9))
    keyboard_one.add_key(helpers.keys.build_mode_button(state_engine, room, keyboard, 10))
    keyboard_one.add_key(helpers.keys.build_power_button(room, keyboard, 11))

    keyboard_two = keyboard.Keyboard()
    keyboard_two.add_key(helpers.keys.build_mode_button(state_engine, room, keyboard, 10))
    
    state_engine.add_keyboard(keyboard_one)
    state_engine.add_keyboard(keyboard_two)
    app = App(hue, state_engine, keybow)

    @keybow.on()
    def handle_key(index, state):

        if state:
            keybow.set_led(index, 0, 0, 255)
            app.execute_action(index)
        else:
            app.update_leds()


    killer = shutdown.Detector()
    while not killer.kill_now:
        keybow.show()
        time.sleep(1.0 / 60.0)

    exit()
