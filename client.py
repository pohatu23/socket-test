import socket

class Client():
  def __init__(self):
    hote = ""
    port = 55556

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    connexion_avec_serveur.settimeout(0)

    print("=============== Bonjour ! ===============")

  def recv():
    try:
      msg = connexion_avec_serveur.recv(1024)
      print(msg.decode())
    except socket.error:
      pass

  def send(message):
    recv()
    connexion_avec_serveur.send(message.encode())
