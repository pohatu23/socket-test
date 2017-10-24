import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('78.223.16.25', 55556))

#connexion_avec_serveur.send(b"coucou")
#connexion_avec_serveur.recv(1024)


#SAAAAAALUUUT

def coucou(3):
  print("coucou"*3)

coucou(4)
