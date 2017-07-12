import argparse

parser = argparse.ArgumentParser(description='OAuth2 Server based on Flask framework')

parser.add_argument('--host', help="host name or IP address, default 'localhost'", default='localhost', dest='host')
parser.add_argument('--port', help="port, default '80' (root permission required)", default=80, dest='port')

args = parser.parse_args()
