import requests
import json

class Room:
    def __init__(self, config):
        self.name = config['ROOM_NAME']
        self.url = f"http://{config['BRIDGE_IP']}/api/{config['HUE_TOKEN']}"
        self.update_room()
        self.get_scenes()

    def get_scenes(self):
        response = requests.get(f'{self.url}/scenes')
        scenes = response.json()
        group_scenes = [scene for scene in scenes.items() if scene[1]['type'] == 'GroupScene']
        self.scenes = [scene[0] for scene in group_scenes if scene[1]['group'] == self.id]

    def get_scene(self, scene_id):
        response = requests.get(f'{self.url}/scenes/{scene_id}')
        return response.json()

    def set_scene(self, scene_id):
        url = f'{self.url}/groups/0/action'
        payload = { 'scene': scene_id }
        response = requests.put(url, json.dumps(payload))
        self.update_room()

    def update_room(self):
        rooms = requests.get(f'{self.url}/groups').json()
        room = [room for room in rooms.items() if room[1]['name'] == self.name][0]
        self.id = room[0]
        self.state = room[1]

    def get_state(self, property):
        return self.state['action'][property]

    def change_brightness(self, payload):
        url = f'{self.url}/groups/{self.id}/action'
        response = requests.put(url, json.dumps(payload))
        self.update_room()

    def dim(self):
        brightness = self.get_state('bri') - 50
        payload = { "bri": brightness if brightness >= 0 else 0 }
        self.change_brightness(payload)

    def brighten(self):
        brightness = self.get_state('bri') + 50
        payload = { "bri": brightness if brightness <= 254 else 254 }
        self.change_brightness(payload)

    def toggle_on_off(self):
        url = f'{self.url}/groups/{self.id}/action'
        payload = { "on": not self.get_state('on') }
        response = requests.put(url, json.dumps(payload))
        self.update_room()

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

    