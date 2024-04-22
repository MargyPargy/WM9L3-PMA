import os

class Config(object):
  basedir = os.path.abspath(os.path.dirname(__file__))

  # assets management
  ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

class DebugConfig(Config):
  DEBUG=True

# load all possible configs
config_dict = {
  'Debug' : DebugConfig,
}