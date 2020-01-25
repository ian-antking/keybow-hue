import requests
import json

class Room:
    def __init__(self, hue_token, bridge_ip, room_name):
        self.token = hue_token
        self.bridge = bridge_ip
        self.room_name = room_name
        self.url = f'http://{bridge_ip}/api/{hue_token}'
        self.lights = self.get_lights()
    
    def get_lights(self):
        rooms = requests.get(f'{self.url}/groups').json()
        return [room[1] for room in rooms.items() if room[1]['name'] == self.room_name][0]['lights']



if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')
    room_name = os.getenv('ROOM_NAME')

    room = Room(hue_token, bridge_ip, room_name)
    print(room.lights)

    