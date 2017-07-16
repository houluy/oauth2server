from flask import Flask, request, render_template, jsonify
import logging
import yaml

from .logger import enc_logger
from .models.models import User, Client
from .globe import config, app, db, cache_db
from .utils.utilities import salting, get_password_and_check
from .token import form_token

enc_logger(logging.getLogger('werkzeug'), config.get('log'))
other_config = config.get('other')

@app.route('/oauth2', methods=['GET'])
def oauth2():
    grant_type = request.args.get('grant_type')
    if (grant_type == 'code'):
        redirect_uri = request.args.get('redirect_uri')
        state = request.args.get('code')
        client_id = request.args.get('client_id')
        client_secret = request.args.get('client_secret')
        scope = request.args.get('scope')

        if not redirect_uri or not state or not client_id or not grant_type:
            return "Parameter not enough"
    
        client = Client.query.filter_by(client_id=client_id).first()
        if not client:
            return "Client ID has not registered yet"

        client_name = client.company_name
        pipeline = cache_db.pipeline()
        key = "client_id{}".format(client_id)
        pipeline.set(key, state).expireat(key, other_config.get('state_expiration')).execute()
        return render_template('login.html', entries=entries)
    elif (grant_type == 'password'):
        username = request.args.get('username')
        password = request.args.get('password')
        scope = request.args.get('scope')

@app.route('/oauth2/authorise', methods=['POST'])
def authorise():

    username = request.form.get('username')
    password = request.form.get('password')

    if get_password_and_check(username, password):
        return "Password is correct"
    else:
        return "Password is wrong"

@app.route('/oauth2/token', methods=['POST'])
def issue_token():
    return jsonify(form_token())

if __name__ == '__main__':
    app.run(host=host, port=port)

