#Objetivo: crear una GUI simple

# Importo las librerias necesarias
import tkinter as tk

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()

#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi primera App con Tkinker")

#Ejecuto el eventloop de la instancia llamado al metodo mainloop
ventana.mainloop()