import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
s.bind(('192.168.88.232',8888))
print('Bind UDP on 8888')
while True:
    # 接收数据
    data,addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
    print('Received from %s:%s.'% addr)
    s.sendto(b'Hello,%s!'% data,addr)