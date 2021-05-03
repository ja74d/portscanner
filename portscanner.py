#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input(str('[*]enter host to scan:'))

sporrport = input(str('''single port or range port:
    1 = single port
    2 = range port
    :'''))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored(f'[!!]port {port} is closed', 'red'))
    else:
        print(colored(f'[+]port {port} is open', 'green'))

if sporrport == '1':
    port = int(input('[*]enter port number to scan:'))
    portscanner(port)
elif sporrport == '2':
    start = int(input('start with:'))
    end = int(input('end with:'))
    for port in range(start, end):
        portscanner(port)
