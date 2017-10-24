import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connexion_principale.bind((hote, port))
connexion_principale.listen(5)

connexion_avec_client, infos_connexion = connexion_principale.accept()

