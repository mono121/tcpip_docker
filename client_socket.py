# -*- coding:utf-8 -*-

import socket


HOST = "127.0.0.1"
PORT = 65530

def send_msg(client):
    msg = input("client message : ")
    if msg == "exit":
        client.send(b'Connection terminated')
        print("Connection terminated")
        client.close()
        
    return msg.encode()

def recieve_msg(client):
    msg = client.recv(4096)
    msg.decode("utf-8")   
    if msg == "exit":
        client.send(b'Connection terminated')
        print("Connection terminated")
        client.close()

    return msg


def main():
    # IPv4 / TCP で通信するソケットを用意する
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        #サーバーにメッセージを送信
        client.send(send_msg(client)) 

        #サーバーからのメッセージを表示
        response = recieve_msg(client)                    
        print ("server message : %s " % (response))


if __name__ == '__main__':
    main()