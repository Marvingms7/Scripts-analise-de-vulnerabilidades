# -*- coding: utf-8 -*-
#!/bin/python
import socket,sys,re,time

file = open("/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt")
porta =  int(sys.argv[2])
for i in file:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((sys.argv[1], porta))
    banner = tcp.recv(2048)
    tcp.send("VRFY" +i)
    user = tcp.recv(2048)
    if re.search("252", user):
        print "Usuário Encontrado:", user.strip("252 2.0.0")
