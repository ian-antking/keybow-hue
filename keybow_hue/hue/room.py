import requests
import json

class Room:
    def __init__(self, hue_token, bridge_ip, room_name):
        self.room_name = room_name
        self.url = f'http://{bridge_ip}/api/{hue_token}'
        self.update_room()
    
    def update_room(self):
        rooms = requests.get(f'{self.url}/groups').json()
        room = [room for room in rooms.items() if room[1]['name'] == self.room_name][0]
        self.id = room[0]
        self.room = room[1]

    def dim_room(self):
        url = f'{self.url}/groups/{self.id}/action'
        brightness = self.room['action']['bri'] - 25
        payload = { "bri": brightness if brightness >= 0 else 0 }
        response = requests.put(url, json.dumps(payload))
        print(response.json())
        self.update_room()

    def brighten_room(self):
        url = f'{self.url}/groups/{self.id}/action'
        brightness = self.room['action']['bri'] + 25
        payload = { "bri": brightness if brightness <= 254 else 254 }
        response = requests.put(url, json.dumps(payload))
        print(response.content)
        self.update_room()


if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    room = Room(hue_token, bridge_ip, room_name)
    room.brighten_room()

    