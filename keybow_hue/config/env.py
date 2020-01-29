from dotenv import load_dotenv
import os

load_dotenv()

class Env:
    def __init__(self, args=[]):
        self.env = {}
        for arg in args:
            self.env[arg] = os.getenv(arg)

if __name__ == '__main__':
    config_vars = ['HUE_TOKEN', 'ROOM_NAME']
    conf = Env(config_vars)
    print(conf.env)