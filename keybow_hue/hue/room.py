import requests
import json

class Room:
    def __init__(self, hue_token, bridge_ip, room_name):
        self.room_name = room_name
        self.url = f'http://{bridge_ip}/api/{hue_token}'
        self.setup_room()
    
    def setup_room(self):
        rooms = requests.get(f'{self.url}/groups').json()
        room = [room for room in rooms.items() if room[1]['name'] == self.room_name][0]
        self.id = room[0]
        self.room = room[1]
        self.brightness = self.room['action']['bri']

    def change_brightness(self, payload):
        url = f'{self.url}/groups/{self.id}/action'
        response = requests.put(url, json.dumps(payload))
        self.brightness = payload['bri'] if response.status_code == 200 else self.brightness

    def dim(self):
        brightness = self.brightness - 50
        payload = { "bri": brightness if brightness >= 0 else 0 }
        self.change_brightness(payload)

    def brighten(self):
        brightness = self.brightness + 50
        payload = { "bri": brightness if brightness <= 254 else 254 }
        self.change_brightness(payload)

if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    room = Room(hue_token, bridge_ip, room_name)
    room.brighten()

    