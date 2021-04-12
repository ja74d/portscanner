#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input(str('[*]enter host to scan:'))

sporrport = input(str('''single port or range port:
    1 = single port
    2 = range port
    :'''))
#def part!
def portscanner(port):
    if sock.connect_ex((host, port)):
        print(f'port {port} is clodes')
    else:
        print(f'port {port} is open')
if sporrport == '1':
    port = int(input('[*]enter port number to scan:'))
    portscanner(port)
elif sporrport == '2':
    start = int(input('enter start of range:'))
    end = int(input('enter end of range:'))
    for port in range(start, end):
        portscanner(port)
