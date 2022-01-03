import socket

# Tupla com o IP e porta a ser usada
ip_porta = ("0.0.0.0", 8080)

# Cria um socket para usar IPv4 (AF_INET) e UDP (SOCK_DGRAM)
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Faz o bind no IP e porta informados
socket_servidor.bind(ip_porta)

while True:
    # Esperando receber dados na porta informada pelo bind
    # dados_byte: conteúdo recebido em bytes
    # endereco: uma tupla (ip, porta) de quem mandou os dados
    print("Servidor esperando dados...")
    dados_byte, endereco = socket_servidor.recvfrom(1024)

    # Mostra os dados recebidos
    texto = dados_byte.decode()
    print(f"Recebido de {endereco}: {texto}")

    if texto == "sair":
        print(f"Cliente {endereco} está saindo...")

    resposta_bytes = str(len(texto)).encode()
    socket_servidor.sendto(resposta_bytes, endereco)
