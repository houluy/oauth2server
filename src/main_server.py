from flask import Flask, request
from .logger import enc_logger
import logging
import yaml

app = Flask("OAuth2")
config_file = 'config/OAuth2.yml'
with open(config_file, 'r') as f:
    config = yaml.load(f)

enc_logger(logging.getLogger('werkzeug'), config.get('log'))

@app.route('/oauth2', methods='GET')
def oauth2():

    return "Hello"

@app.route('/oauth2/authorise', methods='POST')
def authorise():
    
    return "authorise"

@app.route('/oauth2/token')
def issue_token():
    pass

if __name__ == '__main__':
    app.run(host=host, port=port)

