import requests
import json

class Room:
    def __init__(self, config):
        self.name = config['ROOM_NAME']
        self.url = f"http://{config['BRIDGE_IP']}/api/{config['HUE_TOKEN']}"
        # self.update_room()
    
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
    exit()

    