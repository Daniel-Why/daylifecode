import socket

UDP_IP = "192.168.88.232"  # Flask 应用程序的 IP 地址
UDP_PORT = 5005  # Flask 应用程序的端口号
MESSAGE = b"Hello, Flask!"  # 要发送的消息
PATH = "/udp"  # 要发送到的路径

# 将消息和路径组合成一个字符串
data = MESSAGE + PATH.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建 UDP 套接字
sock.sendto(data, (UDP_IP, UDP_PORT))