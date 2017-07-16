from ..globe import db, config

config = config.get('model')
class User(db.Model):
    uid = db.Column(db.String(config.get('uid_len')), primary_key=True)
    username = db.Column(db.String(config.get('username_len')))
    password = db.Column(db.String(config.get('password_len')))
    salt = db.Column(db.String(config.get('salt_len')))
    email = db.Column(db.String(config.get('email_len')))
    def __init__(self, uid, username, password, salt, email=None):
        self.uid = uid
        self.username = username
        self.password = password
        self.salt = salt
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username


class Client(db.Model):
    client_id = db.Column(db.String(config.get('client_id_len')), primary_key=True)
    client_secret = db.Column(db.String(config.get('client_secret_len')))
    company_name = db.Column(db.String(config.get('company_name')), nullable=True)
    def __init__(self, client_id, client_secret, company_name):
        self.client_id = client_id
        self.client_secret = client_secret
        self.company_name = company_name

    def __repr__(self):
        return '<Client: %r, Company_name: %r>' % client_id, company_name
