import unittest
import jwt

from OAuth2.token import gen_token

class TokenTest(unittest.TestCase):
    def setUp(self):
        self.access_token = gen_token()
        self.refresh_token = gen_token(typ='refresh_token')

    def test_token_validation(self):
        decoded = jwt.decode(self.access_token, verify=False)
        payload = decoded.get('payload')
        req_field = ['iss', 'aud', 'sub', 'iat', 'fun'] 
        fun_list = ['access_token', 'refresh_token']
        for field in req_field:
            self.assertIsNotNone(payload.get(field))
        self.assertIn(payload.get('fun'), fun_list)
        if 'exp' in payload.keys():
            self.assertGreater(payload.get('exp'), payload.get('iat'))

        if 'nbf' in payload.keys():
            self.assertGreater(payload.get('iat'), payload.get('nbf'))

if __name__ == '__main__':
    unittest.main()
