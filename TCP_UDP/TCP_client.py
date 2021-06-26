import socket

#创建一个 socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1',9999))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
# 发送请求
for data in [b'Apple',b'Coconut',b'Peach']:
    s.send(data)
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

