import socket,threading,time
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#创建 socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口
## 绑定监听的IP和端口
s.bind(('127.0.0.1',9999))
## 用 Listen 方法监听端口
s.listen(5)
print('Waiting for connection ...')
# 无线循环接收连接
while True:
    #接收一个新连接
    sock,addr = s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

