import socket

socket_cliente=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ipporta_serv=("localhost",8080)

while True:

    print("escolha a operação que deseja realizar")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        try:
            opção=int(input(">> "))
            break

        except (ValueError, NameError):
            print("Digite um valor válido!")


    while True:
        try:
            numero1 = int(input("Digite primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            break
        except (ValueError, NameError):
            print("Insirá valor valido")




    # --------------------------------------------------------------
    if opção==1:
        socket_cliente.sendto(f"1;{numero1};{numero2} ".encode(),ipporta_serv)
        dados_b, endereço = socket_cliente.recvfrom(1024)
        print(f"A soma dos números {numero1} e {numero2} = ",dados_b.decode())

    # --------------------------------------------------------------
    elif opção==2:
        socket_cliente.sendto(f"2;{numero1};{numero2} ".encode(), ipporta_serv)
        dados_b, endereço = socket_cliente.recvfrom(1024)
        print(f"A subtração dos números {numero1} e {numero2} = ", dados_b.decode())
        print(dados_b.decode())

    # --------------------------------------------------------------
    elif opção==3:
        socket_cliente.sendto(f"3;{numero1};{numero2} ".encode(), ipporta_serv)
        dados_b, endereço = socket_cliente.recvfrom(1024)

        print(f"A multiplicação dos números {numero1} e {numero2} = ", dados_b.decode())

    # --------------------------------------------------------------
    elif opção==4:
        socket_cliente.sendto(f"4;{numero1};{numero2} ".encode(), ipporta_serv)
        dados_b, endereço = socket_cliente.recvfrom(1024)

        print(f"A divisão dos números {numero1} e {numero2} = ", dados_b.decode())
    else:
        print("Opção inválida tente novamente!")