from flask import Flask, request
import logging
import yaml

from .logger import enc_logger
from .models.models import User
from globe import config, app
from .utils.utilities import salting

enc_logger(logging.getLogger('werkzeug'), config.get('log'))

@app.route('/oauth2', methods='GET')
def oauth2():

    return "Hello"

@app.route('/oauth2/authorise', methods='POST')
def authorise():

    username = request.form.get('username')
    password = request.form.get('password')

    c_user = User.query.filter_by(username=username).first()
    if check_password(password, c_user, c_salt):
        return "Password is correct"
    else:
        return "Password is wrong"

@app.route('/oauth2/token')
def issue_token():
    pass

if __name__ == '__main__':
    app.run(host=host, port=port)

