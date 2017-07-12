from OAuth2.globe import app
from test import test_token
import logging

host = 'www.lucima.cn'
port = 3001

#t = test_token.TokenTest()
#t.run()
app.run(host=host, port=port)
