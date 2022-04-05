
#!/usr/bin/python
import socket, sys, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 21))
time.sleep(1)
r = s.recv(4096)
s.send("USER anonymous\r\n")
r = s.recv(1024)
s.send("PASS anonymous\r\n")
r = s.recv(1024)


buffer = ["A"]
contador = 100
while len(buffer) <= 100:
	buffer.append("A" * contador)
	contador += 1000
comandos=["CWD","LIST","PWD"]
for comando in comandos:
	for string in buffer:
		print "Fuzzing Comando %s com %s bytes" %(comando,len(string))
		s.send("%s %s \r\n"%(comando,len(string)))
		r = s.recv(1024)
