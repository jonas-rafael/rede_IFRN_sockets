
import socket

porta=("0.0.0.0",8080)

serv= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv.bind(porta)
print("esperando byte")
dadosbyte, endereco= serv.recvfrom(2000)

texto=dadosbyte.decode()
print(texto)

serv.close()