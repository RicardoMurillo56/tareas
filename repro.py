"RICARDO VAZQUEZ MURILLO"
from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog

pygame.init() 
def openFileSong():
    cancion = filedialog.askopenfilename() 
    print(cancion)
    pygame.mixer.music.load(cancion)
        
    
def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()
    
def pauseSong():
    pygame.mixer.music.pause()
    
def volumenUp():
    levelup=pygame.mixer.music.get_volume() +0.1
    print(levelup)
    pygame.mixer.music.set_volume(levelup)

def volumenDown():
    leveldown=pygame.mixer.music.get_volume() -0.1
    print(leveldown)
    pygame.mixer.music.set_volume(leveldown)

raiz = Tk()
raiz.title("REPRODUCTOR DE MUSIC")
raiz.geometry("700x500")

framePrincipal = Frame(raiz, bg="#293133")
framePrincipal.pack(fill="both", expand=1)

Reproductor = Label(framePrincipal, text="REPRODUCTOR DE MUSIC", font=("Arial", 18, "bold"), bg="#000000", fg="#fbfbfb")
Reproductor.place(relx=0.28,rely=0.4)

botonabrir = Button(framePrincipal, text="Abrir cancion", bg="#677862", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=openFileSong)
botonabrir.place(relx=0.05, rely=0.5)

bottonReproducir = Button(framePrincipal, text="Reproducir", bg="#476087", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=playSong) #e2504c rojo, #42ab49 verde, #ffc400 amarillo, #55009 morado, #0000FF
bottonReproducir.place(relx= 0.25, rely=0.5)

bottonparar = Button(framePrincipal, text="Parar", bg="#677862", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=stopSong)
bottonparar.place(relx= 0.8, rely=0.5)

bottoncontinuar = Button(framePrincipal, text="Continuar", bg="#677862", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=resumeSong)
bottoncontinuar.place(relx= 0.45, rely=0.5)

bottonPausa = Button(framePrincipal, text="Pausar", bg="#476087", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=pauseSong)
bottonPausa.place(relx= 0.63, rely=0.5)

bottonVolumenmas = Button(framePrincipal, text="Volumen +", bg="#4c1929", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenUp)
bottonVolumenmas.place(relx= 0.20, rely=0.7)

bottonVolumenbajo = Button(framePrincipal, text="Volumen -", bg="#4c1929", fg="#fbfbfb", font=("Roboto", 10, "bold"), width=12, height=2, command=volumenDown)
bottonVolumenbajo.place(relx= 0.57, rely=0.7)

raiz.mainloop()




