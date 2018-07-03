#Objetivo: muestra como agregar un Entry widget de ttk
# Importo las librerias necesarias
import tkinter as tk
from tkinter import ttk

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()
#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi Quinta App con Tkinter - GUI con un Label, un Button y un Entry")

#Se define un evento que se dispara cuando se hace click en el Button - event handler
def clickMe():
    aButton.configure(text="Hola "+nombre.get())

# Le agrego un Label a la ventana y lo coloco con el grid layout manager
ttk.Label(ventana, text="Ingrese su Nombre:").grid(row=0,column=0)

# Le agrego un Entry a la ventana y lo coloco con el grid layout manager
# Ademas defino la variable nombre y la asocio al Entry para poder recuperar su valor
nombre = tk.StringVar()
nombreEntry = ttk.Entry(ventana,width=20, textvariable=nombre)
nombreEntry.grid(row=0,column=1)

#Se define un widget Button, se lo asigna a una variable
aButton = ttk.Button(ventana, text="Clickeame!!!",command=clickMe)
#Posiciono el Button en el grid layout manager
aButton.grid(row=1, column=1)

#Ejecuto el eventloop de la instancia llamado al metodo mainloop
ventana.mainloop()