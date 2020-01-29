from dotenv import load_dotenv
import os

load_dotenv()

class Env:
    def __init__(self, args=[]):
        self.env = {}
        for arg in args:
            env = os.getenv(arg)
            if env == None:
                raise TypeError(f'{arg} is not set')
            self.env[arg] = env

if __name__ == '__main__':
    config_vars = ['HUE_TOKEN', 'ROOM_NAMEs']
    conf = Env(config_vars)
    print(conf.env)