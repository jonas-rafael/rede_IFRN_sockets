import socket

porta_cliente=("127.0.0.1", 50080)

socket_cliente=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dados = "Olá, Servidor".encode()

socket_cliente.sendto(dados, porta_cliente)

socket_cliente.close()