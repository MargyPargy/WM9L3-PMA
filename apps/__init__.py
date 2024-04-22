from flask import Flask
from importlib import import_module

def register_blueprints(app):
  for module_name in ['home']:
    module = import_module('apps.{}.routes'.format(module_name))
    app.register_blueprint(module.blueprint)

def configure_database(app):
  print("configure database")

def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)
  register_blueprints(app)
  configure_database(app)
  return app