#!/usr/bin/env python
import keybow
import time

control_keys = [0, 3, 6, 9]

for key in control_keys:
  keybow.set_led(key, 127, 127, 127)

@keybow.on()
def handle_key(index, state):
    print("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))

    if state:
        keybow.set_led(index, 0, 255, 0)
    else:
        keybow.set_led(index, 0, 0, 0)


while True:
    keybow.show()
    time.sleep(1.0 / 60.0)