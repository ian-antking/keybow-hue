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
        brightness = -50
        payload = { "bri_inc": brightness }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def bright(self):
        brightness = +50
        payload = { "bri_inc": brightness }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def toggle_on_off(self):
        payload = { "on": not self.get_state('on') }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def increase_hue(self):
        payload = { "hue_inc": 6553 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def decrease_hue(self):
        payload = { "hue_inc": -6553 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def increase_sat(self):
        payload = { "sat_inc": 50 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

    def decrease_sat(self):
        payload = { "sat_inc": -50 }
        self.bridge.update_group(self.id, payload)
        self.update_room()

if __name__ == '__main__':
    exit()
    