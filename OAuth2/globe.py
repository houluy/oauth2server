from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import yaml

config_file = 'config/OAuth2.yml'
with open(config_file, 'r') as f:
    config = yaml.load(f)

app = Flask(config.get('main_name'))
app.config['SQLALCHEMY_DATABASE_URL'] = '{database}://{username}:{password}@{db_host}/{db_name}'.format(config.get('db_config'))

db = SQLAlchemy(app)
