#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(str('enter host:'))
port = int(input('enter port number:'))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(f'port {port} is clodes')
    else:
        print(f'port {port} is open')
portscanner(port)
