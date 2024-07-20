from flask import Flask, make_response,request,jsonify,render_template
import urllib.parse
from socketserver import ThreadingMixIn, TCPServer
from flask_socketio import SocketIO, emit

from flask import Flask, make_response, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    response_text='''
    apple
    "Azzk aikx 189098"
'''
    response = make_response(response_text)
    response.set_cookie('my_cookie', 'cookie_value',max_age=10)
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    url_path = request.path
    decoded_path = urllib.parse.unquote(url_path)
    print("Request path:", url_path)
    print("Decoded path:", decoded_path)

    return response

@app.route('/cookie_test')
def cookie_test():
    if 'my_cookie' in request.cookies and request.cookies['my_cookie'] == 'cookie_value':
        response = "Hello world"
    else:
        response = "cookie error"
    return response

@app.route('/post', methods=['POST'])
def post_test():
    para1 = request.form.get('p1')
    para2 = request.form.get('p2')
    print('{},{}'.format(para1,para2))
    response = {
        'status': 'success',
        'message': '数据处理成功',
        'param1':para1,
        'param2':para2
    }
    return jsonify(response)

@app.route('/get')
def get_test():
    arg1 = request.args.get('p1')
    arg2 = request.args.get('p2')
    print('{},{}'.format(arg1,arg2))
    response = {
        'status': 'success',
        'message': '数据处理成功',
        'arg1':arg1,
        'arg2':arg2
    }
    return jsonify(response)



class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

@app.route('/tcp')
def tcp_path():
    ip_address = request.remote_addr
    print("Your IP address is: {}".format(ip_address))
    return "Hello World!"

@app.route('/example/world')
def example_world():
    name = "World"
    # 将变量传入模板
    return render_template('example.html', name=name)

@app.route('/example/<username>/')
def example_banana(username):
    # 将变量传入模板
    return render_template('example.html', name=username)

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

@socketio.on('connect')
def on_connect():
    print("Client connected")

@socketio.on('message')
def on_message(data):
    print(f"Received message: {data}")
    # 假设我们回应客户端发送的消息
    emit('response', f"You said: {data}")
    

if __name__ == '__main__':
    app.run(host='192.168.3.130',port=999,debug=True)
    #socketio.run(app, host='127.0.0.1', port=5000, debug=True)