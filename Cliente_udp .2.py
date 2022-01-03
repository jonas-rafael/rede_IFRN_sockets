import socket
# gethostname: retorna o nome de host
# gethostbyname: retorna o IP a partir do nome de host
# gethostbyname_ex: retorna o (nome de host, os alias, os IPs) a partir do nome de host
# gethostbyaddr: retorna o (nome de host, os alias, os IPs) a partir do IP
ip_porta_servidor = ("127.0.0.1", 8080)
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
texto = ""

while texto.lower() != "sair":
    texto = input("Digite o texto a ser enviado: ")
    socket_cliente.sendto(texto.encode(), ip_porta_servidor)
    print("Mensagem enviada!")

    dados_bytes, endereco = socket_cliente.recvfrom(1024)
    resposta = int(dados_bytes.decode())
    print(f"Resposta recebida: {resposta}")

socket_cliente.close()