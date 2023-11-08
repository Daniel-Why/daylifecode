from flask import Flask, make_response,request
import urllib.parse
from socketserver import ThreadingMixIn, TCPServer
import threading
import socket


app = Flask(__name__)

@app.route('/')
def index():
    response = make_response("Azzk aikx 189098")
    response.set_cookie('my_cookie', 'cookie_value')
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    url_path = request.path
    decoded_path = urllib.parse.unquote(url_path)
    print("Request path:", url_path)
    print("Decoded path:", decoded_path)

    return response

class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

@app.route('/tcp')
def tcp_path():
    ip_address = request.remote_addr
    print("Your IP address is: {}".format(ip_address))
    return "Hello World!"


@app.errorhandler(404)
def not_found(error):
    orgin_url = request.url
    url_path = request.path
    decoded_path = urllib.parse.unquote(url_path)
    print("Request url:", orgin_url)
    print("Request path:", url_path)
    print("Decoded path:", decoded_path)
    print("request:",request.headers)
    print("request:",request.get_data())

    return 'No No No i am not Dianna', 404
    

if __name__ == '__main__':
    app.run(host='192.168.88.232',port=5000)