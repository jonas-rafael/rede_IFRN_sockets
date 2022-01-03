import socket

socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_servidor.bind(("0.0.0.0", 8080))
socket_servidor.listen(2)
palavras={
    "coxinha": "comida de massa e frango",
    "agua": "bebida da vida",
}

while True:
    print("Aguardando dados...")
    socket_conexão,endereco_cliente=socket_servidor.accept()
    while True:
        dados_bytes=socket_conexão.recvfrom(1024)

        
        lista = dados_bytes.decode().split(";")
        lista[0]= int(lista[0])

        if lista[0] == 1:
            palavras[lista[1]]=lista[2]

        elif lista[0] == 2:

            if palavras.pop(lista[1], None) is None:
                print("Chave removida!")
        elif lista[0] == 3:
            resposta=palavras.get(lista[1], "-")
            socket_servidor.sendto(resposta.encode(),endereço_cliente)
        else:
            print(f"Operação desconhecida recebida do cliente {endereço_cliente}")
