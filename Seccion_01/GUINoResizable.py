#Objetivo: lograr que una GUI no sea resizable

# Importo las librerias necesarias
import tkinter as tk

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()

#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi Segunda App con Tkinter - GUI No Resizable")

#Le coloco la propiedad resizable(0,0) para evitar que la GUI se modifique de tamanio
ventana.resizable(0,0)

#Ejecuto el eventloop de la instancia llamado al metodo mainloop
ventana.mainloop()