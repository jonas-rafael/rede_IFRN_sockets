import socket
print (20*"*")
print ("Exercício de Sockets")
print (20*"*")


site1=socket.gethostbyname_ex("www.twitch.tv")
print(f"twitch.tv: {site1}")
print(20*"*")
site2=socket.gethostbyname_ex("www.youtube.com")
print(f"youtube.com: {site2}")
print(20*"*")
site3=socket.gethostbyname_ex("www.replit.com")
print(f"replit.com {site3}")
print(20*"*")
site4=socket.gethostbyname_ex("www.ahnegao.com.br")
print(f"ahnegão.com.br: {site4}")
print(20*"*")
site5=socket.gethostbyname_ex("www.spotify.com")
print(f"spotify.com: {site5}")
print(20*"*")
site6=socket.gethostbyname_ex("www.amazon.com.br")
print(f"Amazon.com.br: {site6}")
print(20*"*")
site7=socket.gethostbyname_ex("www.primevideo.com")
print(f"primevideo.com: {site7}")
print(20*"*")
site8=socket.gethostbyname_ex("br.pinterest.com")
print(f"br.pinterest.com: {site8}")
print(20*"*")
site9=socket.gethostbyname_ex("shopee.com.br")
print(f"shopee.com.br: {site9}")
print(20*"*")
site10=socket.gethostbyname_ex("www.magickando.com.br")
print(f"magickando.com.br: {site10}")