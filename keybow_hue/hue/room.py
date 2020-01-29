class Room:
    def __init__(self, room_name, bridge):
        self.name = room_name
        self.bridge = bridge
        room_data = self.bridge.get_room(self.name)
        self.id = room_data['id']
        self.state = room_data['state']
        self.scenes = self.bridge.get_scenes

    def update_room(self):
        room_data = self.bridge.get_room(self.name)
        self.state = room_data['state']

    def get_state(self, property):
        return self.state['action'][property]

    def dim(self):
        brightness = self.get_state('bri') - 50
        payload = { "bri": brightness if brightness >= 0 else 0 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def bright(self):
        brightness = self.get_state('bri') + 50
        payload = { "bri": brightness if brightness <= 254 else 254 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def toggle_on_off(self):
        payload = { "on": not self.get_state('on') }
        self.bridge.update_group(self.id, payload)
        self.update_room()

if __name__ == '__main__':
    exit()
    