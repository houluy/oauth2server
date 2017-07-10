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
        key = open(config.get('server_key_file'))
    except:
        print('A server key file is required')
        sys.exit(0)
    payload = deepcopy(kwargs)
    payload['iss'] = iss if iss else config.get('issuer') 
    payload['aud'] = aud if aud else config.get('audience')
    payload['sub'] = sub if sub else config.get('subject')
    payload['iat'] = time.time()
    if nbf:
        payload['nbf'] = payload.get('iat') + config.get('not_before')
    payload['fun'] = typ
    # Expiration is different between access and refresh
    payload['exp'] = payload.get('iat') + config.get('expiration').get(typ)
    encoded = jwt.encode(payload, key, algorithm=algorithm)
    return encoded

