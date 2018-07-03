#Objetivo: muestra como agregar un label widget a nuestra GUI.

# Importo las librerias necesarias
import tkinter as tk
from tkinter import ttk #ttk es una extension con mejores widgets

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()

#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi Tercera App con Tkinter - GUI con un Label")

# Le agrego un Label a la ventana y lo coloco con el grid layout manager
ttk.Label(ventana,text="Este es un Label").grid(row=0, column=0)

#Ejecuto el eventloop de la instancia llamado al metodo mainloop
ventana.mainloop()