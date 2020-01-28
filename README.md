# Keybow-Hue
Control Phillips Hue lights with the [Pimoroni Keybow](https://shop.pimoroni.com/products/keybow).

Also compatible with the [Keybow Mini](https://shop.pimoroni.com/products/keybow-mini-3-key-macro-pad-kit?variant=27890392039507)

## Getting Started

This project requires a Raspberry Pi, running raspbian/raspbian lite, and a connected keybow.

### Configure the app

Create a file in the root of the project called `.env`. Add the following:

```
HUE_TOKEN=<hue bridge access token>
ROOM_NAME=<name of room being controlled (in "" if more than one word)>
```

See [this guide](https://developers.meethue.com/develop/get-started-2/) for details on how to obtain an access token.

### Install dependencies

Open a terminal, and run this command from the project root:

```
pip3 install -r requirements.txt
```

### Running the app

Open a terminal, and run this command from the project root:

```
python3 keybow_hue/app.py 
```

If no config variables are found, all keys will turn red. Otherwise, key 1 will turn red/green depending on if the lights in your room are currently on. If they are on, keys 0 & 2 can be used to adjust the brightness.
