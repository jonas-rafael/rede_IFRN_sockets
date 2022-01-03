import socket

ipporta=("0.0.0.0",80000)

socket_servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_servidor.bind(ipporta)

socket_servidor.listen(2)

while True:
    print("esperando conexão.....")
    socket_conexão,endereco_client= socket_servidor.accept()
    print(f"cliente {endereco_client} está conectado!")

    print("esperando dados..")
    dados_byte=socket_servidor.recvfrom(1024)


    texto=dados_byte.decode()
    print(f"recebido de {endereco_client}:{texto}")

    resposta_byte=str(len(texto)).encode()
    socket_conexão.sendall(resposta_byte)
    if texto == "sair":
        socket_conexão.close()
        print(f"cliente {endereco_client} desconectado")
        break