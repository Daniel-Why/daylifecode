import socket

def create_proxy_server(host='localhost', port=8888):
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 防止“Address already in use”错误
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定IP和端口
    server_socket.bind((host, port))
    
    # 开始监听，最大连接数为5
    server_socket.listen(5)
    print(f"Proxy server is listening on {host}:{port}")
    
    while True:
        # 接受一个客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # 接收数据
        data = client_socket.recv(1024)
        if data:
            # 打印接收到的数据
            print("Received data:", data.decode())
            
            # 这里可以添加处理数据的逻辑，或者转发到其他地方
            # 为了简单起见，我们直接回显数据给客户端
            client_socket.send(data)
        
        # 关闭客户端连接
        client_socket.close()

if __name__ == "__main__":
    create_proxy_server()