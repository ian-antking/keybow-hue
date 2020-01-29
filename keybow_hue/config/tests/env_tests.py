from nose.tools import assert_true
import config
import os

os.environ["HUE_TOKEN"] = "1234"
os.environ["ROOM_NAME"] = "test_room"

def test():
  env_vars = ['HUE_TOKEN', 'ROOM_NAME']
  conf = config.Env(env_vars)
  assert_true(conf.env['HUE_TOKEN'] == "1234" and conf.env['ROOM_NAME'] == "test_room")