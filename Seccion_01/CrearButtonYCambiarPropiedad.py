#Objetivo: muestra como agregar un Label y un Button widget de ttk y disparar un evento que modifica las propiedades
# Importo las librerias necesarias
import tkinter as tk
from tkinter import ttk

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()
#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi Cuarta App con Tkinter - GUI con un Label y Un Button que Actualiza el Label")

#Ahora el Label se guarda en una variable para poder modificar sus propiedades
#Ver como cambia el proceso de agregar a la ventana y colocarlo con el grid layout manager
aLabel = ttk.Label(ventana, text="Un Label")
#Posiciono el Label en el grid layout manager
aLabel.grid(row=0,column=0)

#Se define un evento que se dispara cuando se hace click en el Button - event handler
def clickMe():
    aButton.configure(text="El Button ha sido presionado")
    aLabel.configure(foreground="red")
    aLabel.configure(text="Un Label de color Rojo")

#Se define un widget Button, se lo asigna a una variable
aButton = ttk.Button(ventana, text="Un Button", command=clickMe)
#Posiciono el Button en el grid layout manager
aButton.grid(row=0, column=1)

#Ejecuto el eventloop de la instancia llamado al metodo mainloop
ventana.mainloop()