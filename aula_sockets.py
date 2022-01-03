import socket
# gethostname: retorna o nome de host
# gethostbyname: retorna o IP a partir do nome de host
# gethostbyname_ex: retorna o (nome de host, os alias, os IPs) a partir do nome de host
# gethostbyaddr: retorna o (nome de host, os alias, os IPs) a partir do IP
nome = socket.gethostname()
ip = socket.gethostbyname(nome)
ip2 = socket.gethostbyname("localhost")
extra1=socket.gethostbyname_ex(nome)
print(nome)
print(ip)
print(ip2)
print(extra1)

ifrn= socket.gethostbyname_ex("www.ifrn.edu.br")
ifrnip=socket.gethostbyname("www.ifrn.edu.br")
ifrn2=socket.gethostbyaddr(ifrnip)

print(ifrn)
print(ifrnip)
print(ifrn2)