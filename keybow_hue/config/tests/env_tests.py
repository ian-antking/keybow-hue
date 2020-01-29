from nose.tools import assert_true, assert_raises
import config
import os

os.environ["TEST_TOKEN"] = "1234"
os.environ["TEST_NAME"] = "test_room"


def test_Env_GivenVariableArray_LoadsVariablesFromOs():
    env_vars = ['TEST_TOKEN', 'TEST_NAME']
    conf = config.Env(env_vars)
    assert_true(conf.env['TEST_TOKEN'] == "1234" and conf.env['TEST_NAME'] == "test_room")


def test_Env_VariableNotInOs_ThrowsError():
    env_vars = ['MISSING_VAR']
    assert_raises(TypeError, config.Env, env_vars)