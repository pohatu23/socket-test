import socket
from time import time, sleep

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_principale.bind((hote, port))
connexion_principale.listen(5)

connexion_avec_client, infos_connexion = connexion_principale.accept()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = ""
port = 55556

s.bind((host,port))
s.listen(5)

s.settimeout(0.0)


clients = []

while time()-t<5.0:

    try:
        co,inf = s.accept()
        i = len(clients)
        clients.append((co,inf,i))
        print("received client",i,":",co,inf)
    except socket.error:
        pass
        


msg = b""

for client in clients:
    try:
        msg = client[0].recv(1024)
        print(msg.decode())
        i = client[2]

        for client in clients:
            if client[2] != i:
                client[0].send(msg)
            
    except socket.error:
        sleep(0.1)
