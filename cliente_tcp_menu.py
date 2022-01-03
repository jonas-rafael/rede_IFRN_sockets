import socket

socket_cliente=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_porta_servidor=("localhost ",8080)


while True:
    print("escolha uma opção.")
    print("0 - sair do programa.")
    print("1 - Adcionar/atualizar uma palavra.")
    print("2 - Remover palavra.")
    print("3 - Consulta palavra.")
    opção=int(input(">> "))

    if opção == 0:
        print("Saindo do programa...")
        socket_cliente.close()
    elif opção ==1:
        palavra=input("Digite a palavra: ")
        significado=input("Digite o significado:")


        socket_cliente.sendall(f"1;{palavra};{significado}".encode())
        print("Palavra adcionada/atualizada com sucesso.")
        resposta=bool(socket_cliente.recvfrom(1024).decode())
        if resposta:
            print("A operação foi bem sucedida")
        else:
            print("A operação não foi finalizada!")
       #socket_cliente.sendto(palavra.encode(),ip_porta_servidor)
       #socket_cliente.sendto(significado.encode(),ip_porta_servidor)

        #envia para o servidor
    elif opção ==2:
        palavra=input("Digite a palavra:")
        socket_cliente.sendto(f"2;{palavra};{significado}".encode(),ip_porta_servidor)
        print("Palavra removida co sucesso! ")

        #envia para o servidor
    elif opção == 3:
        palavra=input("Digite a pálavra: ")
        socket_cliente.sendto(f"2;{palavra}".encode,ip_porta_servidor)
        dados_bytes, endereço =socket_cliente.recvfrom(1024)
        print("significado",dados_bytes.decode())
    else:
        print("Opção invalida tente novamente!")

