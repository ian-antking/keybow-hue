import requests
import json
from hue.bridge import Bridge

class Room:
    def __init__(self, config):
        self.name = config['ROOM_NAME']
        self.url = f"http://{config['BRIDGE_IP']}/api/{config['HUE_TOKEN']}"
        self.bridge = Bridge(config['HUE_TOKEN'])
        room_data = self.bridge.get_room(self.name)
        self.id = room_data['id']
        self.state = room_data['state']
        self.scenes = self.bridge.get_scenes

    def update_room(self):
        room_data = self.bridge.get_room(self.name)
        self.state = room_data[1]

    def get_state(self, property):
        return self.state['action'][property]

    def dim(self):
        brightness = self.get_state('bri') - 50
        payload = { "bri": brightness if brightness >= 0 else 0 }
        self.bridge.update_group(self.id, payload)

    def brighten(self):
        brightness = self.get_state('bri') + 50
        payload = { "bri": brightness if brightness <= 254 else 254 }
        self.bridge.update_group(self.id, payload)

    def toggle_on_off(self):
        payload = { "on": not self.get_state('on') }
        self.bridge.update_group(self.id, payload)

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    config_vars = ['HUE_TOKEN', 'BRIDGE_IP', 'ROOM_NAME']
    env_variables = {}
    for var in config_vars:
        env_variables[var] = os.getenv(var)

    room = Room(env_variables)
    exit()

    