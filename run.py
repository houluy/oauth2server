from OAuth2.globe import app
from OAuth2.parser import args
from OAuth2 import main_server

from test import test_token
import logging

#t = test_token.TokenTest()
#t.run()
app.run(host=args.host, port=args.port)
