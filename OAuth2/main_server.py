from flask import Flask, request
import logging
import yaml

from .logger import enc_logger
from .models.models import User
from .globe import config, app
from .utils.utilities import salting
from .token import gen_token

enc_logger(logging.getLogger('werkzeug'), config.get('log'))

@app.route('/oauth2', methods='GET')
def oauth2():
    redirect_uri = request.args.get('redirect_uri')
    state = request.args.get('code')
    if not redirect_uri or not state:
        return "Parameter not enough"
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

@app.route('/oauth2/token', method='POST')
def issue_token():
    access_token = gen_token() #Custom data is allowed
    refresh_token = gen_token(typ='refresh_token')
    expires_in = config.get('token').get('expiration').get('access_token')
    token_type = "Bearer" #Default Bearer

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expires_in': expires_in,
        'token_type': token_type,
    }

if __name__ == '__main__':
    app.run(host=host, port=port)

