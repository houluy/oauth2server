import jwt
from copy import deepcopy
from time import time

from .globe import config

config = config.get('token')
def gen_access_token(iss=None, aud=None, nbf=False, algorithm='HS256', **kwargs):
    if not iss or not aud:
        raise Exception('Not enough field in JWT')
    payload = deepcopy(kwargs)
    payload['iss'] = config.get('issuer')
    payload['aud'] = config.get('audience')
    payload['iat'] = time.time()
    payload['exp'] = payload.get('iat') + config.get('expiration')
    

