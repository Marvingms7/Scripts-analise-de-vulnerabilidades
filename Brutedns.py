import os, sys
import dns.resolver

argumentos = sys.argv
try:
	dominio = argumentos[1]
	lista = argumentos[2]
except:
	print('Faltam argumentos no comando')
	sys.exit

try:
	arquivo = open(lista)
	linhas = arquivo.read().splitlines()
except:
	print('Arquivo nao encontrado ou invalido')
	sys.exit

for linha in linhas:
	subdominio = linha +'.'+ dominio
	try:
		respostas = dns.resolver.query(subdominio, 'a')
		for resultado in respostas:
			print( subdominio, resultado)
	except:
		pass
