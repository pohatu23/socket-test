import socket
from tkinter import *

#============ conexion serveur =============#

#hote = ""
#port = 55556

#connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connexion_avec_serveur.connect((hote, port))
#connexion_avec_serveur.settimeout(0)

#============ fenetre tkinter =============#

class Interface(Frame):
    
  """Notre fenêtre principale. Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
  def __init__(self, fenetre, **kwargs):
    Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
    self.pack(fill=BOTH)
    self.nb_clic = 0
        
    # Création des widgets
    self.messageTop = Label(self, text="Messagerie rudimentaire")
    self.messageTop.pack()

    self.champ_label = [""]*10
    for i in range(10):
      self.champ_label[i] = Label(fenetre, text="")
      self.champ_label[i]["text"] = ""
      self.champ_label[i].pack()

    self.var_texte = StringVar()
    self.ligne_texte = Entry(fenetre, textvariable = self.var_texte, width = 30)
    self.ligne_texte.pack()

    self.ligne_texte.bind("<Return>", self.envoyer)
        
    self.bouton_quitter = Button(self, text="Quitter", command=self.end)
    self.bouton_quitter.pack(side="left")
    
  def envoyer(self, touche):

    message = self.var_texte.get()
    self.var_texte.set("")
    print(message)
    self.afficher(message)
    connexion_avec_serveur.send(message.encode()) #envoie serveur
    self.ligne_texte.delete(0, 100)

  def recevoir(self):

    try:
      msg = connexion_avec_serveur.recv(1024).decode()
      print(msg)
      self.afficher(msg)
    except socket.error:
      pass

  
  def afficher(self, message):

    for champ in self.champ_label:
      if champ["text"] == "":
        champ["text"] = message
        return
    for i in range(0,9):
      self.champ_label[i]["text"] = self.champ_label[i+1]["text"]
    self.champ_label[9]["text"] = message

  def end(self):
    interface.destroy()
    fenetre.destroy()
    global continuer
    continuer = False

fenetre = Tk()
interface = Interface(fenetre)

print("=============== Bonjour ! ===============")

#connexion_avec_serveur.send(b"coucou")
#connexion_avec_serveur.recv(1024)

continuer = True

while continuer:
    fenetre.update_idletasks()
    fenetre.update()
    interface.recevoir()
