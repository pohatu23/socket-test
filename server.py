import socket
from time import time, sleep

GRAPHIC_DISPLAY = False

def disp(*args):
    if GRAPHIC_DISPLAY:
        print(**args)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = ""
port = 55556

s.bind((host,port))
s.listen(5)

s.settimeout(0.0)


clients = []

t = time()

while time()-t<20.0:

    try:
        co,inf = s.accept()
        i = len(clients)
        clients.append((co,inf,i))
        disp("received client",i,":",co,inf)
    except socket.error:
        pass

disp("Discussion is open\n")
        

def receive():
    t = time()
    
    while time()-t < 600.0:
        for client in clients:
            try:
                msg = client[0].recv(2048)
                print(msg.decode())
                if msg.decode() == "fin":
                    return
                i = client[2]

                for client in clients:
                    if client[2] != i:
                        client[0].send(str(inf).encode()+b" : "+msg)
                    
            except socket.error:
                sleep(0.1)

receive()

s.close()


