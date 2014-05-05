#!/usr/bin/env python

import socket, ssl, sys

SERVER_ADDRESS=('localhost',10023)
PATH_TO_CERT='cert.pem'

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss=ssl.wrap_socket(s,ca_certs=PATH_TO_CERT,cert_reqs=ssl.CERT_REQUIRED)
ss.connect(SERVER_ADDRESS)
data=''
for x in sys.argv[1:]:
    data= data + x
ss.send(data)
print ss.recv(1024)
