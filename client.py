import socket
import tkinter as tk

#============ conexion serveur =============#

hote = ""
port = 55556

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
connexion_avec_serveur.settimeout(0)

#============ fenetre tkinter =============#

fenetre = tk.Tk

class Interface(Frame):
    
    """Notre fenêtre principale. Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        # Création de nos widgets
        self.message = Label(self, text="Messagerie rudimentaire")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_envoie = Button(self, text="Cliquez ici", fg="red", command=self.envoie)
        self.bouton_envoie.pack(side="right")
    
    def envoie(self):
        """Il y a eu un clic sur le bouton, on change la valeur du label message."""
        
        var_text.get()
        connexion_avec_serveur.send(message.encode())
        
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

champ_label = []

for i in range(10):
  champ_label.append(Label(fenetre, text="")
  champ_label[i]["text"] = "ligne {}".format(i)
champ_label.pack()

var_texte = StringVar()
ligne_texte = Entry(fenetre, textevariable = var_texte, width = 30)
lign_texte.pack()

fenetre.mainloop()

print("=============== Bonjour ! ===============")

#connexion_avec_serveur.send(b"coucou")
#connexion_avec_serveur.recv(1024)

def recv():
  try:
    msg = connexion_avec_serveur.recv(1024)
    print(msg.decode())
  except socket.error:
    pass

while True:
  recv()
