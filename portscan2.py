import os, sys
import socket

argumento = sys.argv

try:
    dominio = argumento[1]
except:
    print('Algo deu errado!')
    sys.exit

portas = []
for n in range(1, 1000):
    portas.append(n)
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.2)
    codigo = cliente.connect_ex((dominio, porta))
    if codigo == 0:
        print(f'PORT {porta} OPEN')
