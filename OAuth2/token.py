import jwt
from copy import deepcopy
from time import time
import sys

from .globe import config

config = config.get('token')

def gen_token(iss=None, aud=None, sub=None, nbf=False, typ='access_token', algorithm='HS256', **kwargs):
    '''Generate access_token and refresh_token in JWT format
    @ iss: URN of the issuer
    @ aud: URN of the audience
    @ sub: URN of the subject
        both default in config file
    @ nbf: whether need the Not Before restriction
    @ typ: access_token or refresh_token
    @ algorithm: digital signature algorithm, default HS256
    @ kwargs: custom payload
    % return the encoded token
    '''
    try:
        key = open(config.get('server_key_file')).read()
    except:
        print('A server key file is required')
        sys.exit(0)
    payload = deepcopy(kwargs)
    payload['iss'] = iss if iss else config.get('issuer') 
    payload['aud'] = aud if aud else config.get('audience')
    payload['sub'] = sub if sub else config.get('subject')
    payload['iat'] = time()
    if nbf:
        payload['nbf'] = payload.get('iat') + config.get('not_before')
    payload['fun'] = typ
    # Expiration is different between access and refresh
    print(config.get('expiration').get(typ))
    payload['exp'] = payload.get('iat') + config.get('expiration').get(typ)
    encoded = jwt.encode(payload, key, algorithm=algorithm)
    return encoded.decode()

def form_token():
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
