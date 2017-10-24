import socket

hote = ""
port = 55556

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

#connexion_avec_serveur.send(b"coucou")
#connexion_avec_serveur.recv(1024)
