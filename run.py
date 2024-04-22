from apps import create_app
from apps.config import config_dict

DEBUG = 'True'

config_mode = 'Debug' if DEBUG else 'Production'

try:
  app_config = config_dict[config_mode]

except KeyError:
  exit('Error: Invalid config mode. Expected values [Debug]')

app = create_app(app_config)

if __name__ == '__main__':
  app.run(debug=True)