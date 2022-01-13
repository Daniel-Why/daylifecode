import socket
import threading
import multiprocessing
import time

serveraddr1 = ('127.0.0.1', 8080)#定义server的ip和地址
serveraddr2 = ('127.0.0.1', 8081)#定义server的ip和地址

def client_thread(client,port):#客户端建立socket
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.bind(('127.0.0.1', port))
    client.listen(1)
    while(True):
        clientsocket, address = client.accept()
        print(clientsocket.recv(1024).decode('utf-8'))

def client_connect(serveraddr,client_name,input_text):
    #login指令
    target = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    target.connect(serveraddr)
    id = client_name #input('请输入你的用户名: ')
    target.send(('none login '+id).encode('utf-8'))
    port = int(target.recv(1024).decode('utf-8'))
    print('链接成功')
    target.close()
    #启动客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    threading.Thread(target=client_thread, args=(client,port)).start()
    #开始发送指令
    while(True):
        time.sleep(1)
        input_text=input_method()
        put = id+' '+ input_text #input()
        target = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        target.connect(serveraddr)
        target.send(put.encode('utf-8'))
        callback = target.recv(1024).decode('utf-8')
        if(callback!='success'):
            print(callback)
        target.close()
        if put.split(' ')[1] == 'close':#关闭客户端
            break
    client.close()

def input_method():
    input_text = input()
    return input_text

def main():
    input_text=input_method()
    p1 = multiprocessing.Process(target=client_connect,args=(serveraddr1,"daniel",input_text))
    p1.start()
    #p2 = multiprocessing.Process(target=client_connect,args=(serveraddr2,"daniel"))
    #p2.start()

if __name__ == "__main__":
    main()