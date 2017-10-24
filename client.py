import socket

socket.settimeout(0)

hote = ""
port = 55556

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))

print("=============== Bonjour ! ===============")

#connexion_avec_serveur.send(b"coucou")
#connexion_avec_serveur.recv(1024)

def recv():
  try:
    msg = connexion_avec_serveur.recv(1024)
    print(msg)
  except socket.error:
    pass

def send(message):
  connexion_avec_serveur.send(message)
