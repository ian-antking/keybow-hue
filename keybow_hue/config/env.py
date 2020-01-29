from dotenv import load_dotenv
import os

load_dotenv()

class Env:
    def __init__(self, args=[]):
        self.var = {}
        for arg in args:
            self.var[arg] = os.getenv(arg)

if __name__ == '__main__':
    config_vars = ['HUE_TOKEN', 'ROOM_NAME']
    config = Env(config_vars)
    print(config.var)