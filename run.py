from src import main_server
import logging

host = 'www.lucima.cn'
port = 3001

main_server.app.run(host=host, port=port)
