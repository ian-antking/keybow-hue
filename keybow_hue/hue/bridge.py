import json

class Bridge:
    def __init__(self, hue_token, request_manager):
        self.requests_manager = request_manager
        self.bridge_ip = self.resolve_bridge_ip()
        self.bridge_url = f"http://{self.bridge_ip}/api/{hue_token}"

    def get_room(self, room_name):
        rooms = self.requests_manager.get(f'{self.bridge_url}/groups').json()
        room = [room for room in rooms.items() if room[1]['name'] == room_name][0]
        return {
            'id': room[0],
            'state': room[1]
        }

    def resolve_bridge_ip(self):
        response = self.requests_manager.get('https://discovery.meethue.com/')
        return response.json()[0]['internalipaddress']

    def get_scenes(self, room_id):
        scenes = self.requests_manager.get(f'{self.bridge_url}/scenes').json()
        group_scenes = [scene for scene in scenes.items() if scene[1]['type'] == 'GroupScene']
        return [scene[0] for scene in group_scenes if scene[1]['group'] == room_id]

    def get_scene(self, scene_id):
        response = self.requests_manager.get(f'{self.bridge_url}/scenes/{scene_id}')
        return response.json()

    def set_scene(self, scene_id):
        url = f'{self.bridge_url}/groups/0/action'
        payload = { 'scene': scene_id }
        response = self.requests_manager.put(url, json.dumps(payload))
        return response.status_code

    def update_group(self, group_id, payload):
        url = f'{self.bridge_url}/groups/{group_id}/action'
        response = self.requests_manager.put(url, json.dumps(payload))
        return response.status_code

if __name__ == '__main__':
    exit()
