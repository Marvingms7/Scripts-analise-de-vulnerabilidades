import socket, sys
	
try:
	s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 110))
	r = s.recv(1024)
	print r
	s.send("USER teste\r\n")
	r = s.recv(1024)
	print r
	s.send("PASS teste\r\n")
	r = s.recv(1024)
	print r
	s.send("QUIT \r\n")
	r = s.recv(1024)
	print r
except:
	print 'erro ao conectar'
