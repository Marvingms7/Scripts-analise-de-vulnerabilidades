#!/bin/python3
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.registro.br", 43))
s.send( sys.argv[1].encode()+'/r/n'.encode())
resposta = s.recv(2048).split()
print(f'{resposta}')

