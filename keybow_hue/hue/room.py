import requests


class Room:
    def __init__(self, hue_token, bridge_ip):
        self.url = f'http://{bridge_ip}/api/{hue_token}'
    
    def get_groups(self):
        return requests.get(f'{self.url}/groups').content



if __name__ == '__main__':
    from dotenv import load_dotenv
    import os
    load_dotenv()
    hue_token = os.getenv('HUE_TOKEN')
    bridge_ip = os.getenv('BRIDGE_IP')

    room = Room(hue_token, bridge_ip)
    print(room.get_groups())

    