from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import yaml

config_file = 'config/OAuth2.yml'
with open(config_file, 'r') as f:
    config = yaml.load(f)

app = Flask(config.get('main_name'), template_folder='../templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = '{database}://{username}:{password}@{db_host}/{db_name}'.format(**config.get('db_config'))
app.config['REDIS_URL'] = 'redis://:{password}@{host}:{port}/0'.format(**config.get('redis_config'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
cache_db = FlaskRedis(app)
