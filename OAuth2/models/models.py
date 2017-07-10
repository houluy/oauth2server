from ..globe import db, config

config = config.get('model')
class User(db.Model):
    uid = db.Column(db.String(config.get('uid_len')), primary_key=True)
    username = db.Column(db.String(config.get('username_len'))
    password = db.Column(db.String(config.get('password_len'))
    email = db.Column(db.String(config.get('email_len')))
    def __init__(self, uid, username, password, email=None):
        self.uid = uid
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username


