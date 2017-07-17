import hashlib
import string
import random
from ..globe import config
from ..models.models import User

config = config.get('security')

def generate_random_string(length=None):
    '''Generate random string
    @ length: the length of the salt, default is configured in config file
    % Salt string in string
    '''
    if not length:
        length = config.get('salt_len')

    return ''.join(random.choice(string.printable) for i in range(length))


def salting(old_password, salt=None):
    '''Salting the given password using the given(or random) salt
    @ old_password: the password ready to salting
    @ salt: salt string
    % Salted password
    '''
    if not salt:
        salt = generate_random_salt()
    new_password = config.get('global_salt') + old_password + salt
    new_password = hashlib.sha256(new_password.encode()).hexdigest()
    return new_password

#Please change this function in your own way
def check_password(recv_password, saved_password, salt):
    recv_password = salting(recv_password, salt)
    return True if recv_password == saved_password else False

def get_password_and_check(username, password):
    '''Get saved password from database and verify it
    @ username: username
    @ recv_password: Received password from clients
    % True or False
    '''
    c_user = User.query.filter_by(username=username).first()
    return check_password(recv_password, c_user.password, c_user.salt)

