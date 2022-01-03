import socket

ipporta_servidor=("157.0.0.1",80000)

socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client.connect(ipporta_servidor)

texto=""


while texto.lower != "sair":
    print(23*"-")
    texto=input("Texto a ser enviado: ")
    socket_client.sendall(texto.encode())
    print("Texo enviado!")

    dados_bytes=socket_client.recvfrom(1024)
    resposta=int(dados_bytes.decode())
    print(f"A resposta recebida é :{resposta}")

socket_client.close()