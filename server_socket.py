# -*- coding:utf-8 -*-

import socket


HOST = "127.0.0.1"
PORT = 65530

def send_msg(server,client):
    msg = input("server message : ")
    if msg == "exit":
        client.send(b'Connection terminated')
        print("Connection terminated")
        server.close()
        exit()
        
    return msg.encode("utf-8")

def recieve_msg(client):
    msg = client.recv(4096)
    msg.decode("utf-8")   
    if msg == "exit":
        client.send(b'Connection terminated')
        print("Connection terminated")
        client.close()

    return msg

def main():
    # IPv4/TCPで通信
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.bind((HOST, PORT))

    # サーバー待機状態
    server.listen()
    print('waiting ...')
    # クライアントからのデータを取得
    client, (client_address, client_port) = server.accept()
    print(f'connection from {client_address} : {client_port}')
   
    while True:
        #クライアントからのメッセージを表示
        response = recieve_msg(client)             
        print ("client message : %s " % (response))

        #クライアントにメッセージを送信
        client.send(send_msg(server,client)) 

if __name__ == '__main__':
    main()