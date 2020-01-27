from dotenv import load_dotenv
import os

def load(args=[]):
    env_variables = {}
    for arg in args:
        env_variables[arg] = os.getenv(arg)
    return env_variables

if __name__ == '__main__':
    config_vars = ['HUE_TOKEN', 'BRIDGE_IP', 'ROOM_NAME']
    config = loader(config_vars)
    print(config)