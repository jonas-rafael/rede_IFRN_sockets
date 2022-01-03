import socket

socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_servidor.bind(("0.0.0.0", 8080))

while True:
    print("Aguardando os dados...")
    dados_b, endereço_cliente=socket_servidor.recvfrom(1024)
    lista=dados_b.decode().split(";")
    lista[0]=int(lista[0])

    if lista[0]==1:
        n1=int(lista[1])
        n2=int(lista[2])
        soma=str(n1+n2)
        socket_servidor.sendto(soma.encode(), endereço_cliente)
        #print("A Soma foi realizada e devolvida ao Cliente")
    elif lista[0]==2:

        n1 = int(lista[1])
        n2 = int(lista[2])
        sub=str(n1-n2)

        socket_servidor.sendto(sub.encode(), endereço_cliente)
        #print("A Subtração foi realizada e devolvida ao Cliente")

    elif lista[0]==3:
        n1 = int(lista[1])
        n2 = int(lista[2])
        mult=str(n1*n2)
        socket_servidor.sendto(mult.encode(), endereço_cliente)
        print("A Multiplicação foi realizada e devolvida ao Cliente")

    elif lista[0]==4:
        n1 = int(lista[1])
        n2 = int(lista[2])
        div=str(n1//n2)
        socket_servidor.sendto(div.encode(), endereço_cliente)
        print("A Divisão foi realizada e devolvida ao Cliente")

    else:
        print(f"Operação desconhecida recebida do cliente {endereço_cliente}")
socket_servidor.close()