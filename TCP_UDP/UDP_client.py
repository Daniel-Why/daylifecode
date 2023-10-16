import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Apple',b'Coconut',b'Peach']:
    s.sendto(data,('192.168.88.232',5005))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close