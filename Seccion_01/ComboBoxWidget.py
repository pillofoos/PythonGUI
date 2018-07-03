#Objetivo: muestra como agregar un ComboBox widget - Ojo se pueden modificar los valores de entrada
# Importo las librerias necesarias
import tkinter as tk
from tkinter import ttk

#Creo una instancia de la clase tk llamando al constructor
ventana = tk.Tk()
#Le coloco un titulo a la ventana con la propiedad title
ventana.title("Mi Septima App con Tkinter - GUI con un Label, un Button y un Entry")

#Se define un evento que se dispara cuando se hace click en el Button - event handler
def clickMe():
    aButton.configure(text="Hola "+nombre.get())

# Le agrego un Label a la ventana y lo coloco con el grid layout manager
tk.Label(ventana, text="Ingrese su nombre").grid(row=0, column=0)

# Le agrego un Entry a la ventana y lo coloco con el grid layout manager
# Ademas defino la variable nombre y la asocio al Entry para poder recuperar su valor
nombre = tk.StringVar()
nombreTextBox = tk.Entry(ventana, width=20, textvariable=nombre)
nombreTextBox.grid(row=0, column=1)

# Le agrego un ComboBox a la ventana y lo coloco con el grid layout manager
# Ademas defino la variable numero y la asocio al ComboBox para poder recuperar su valor
numero = tk.StringVar()
numeroComboBox = ttk.Combobox(ventana, width=20, textvariable=numero)
numeroComboBox['values']=(1,5,10,20)
numeroComboBox.current(0)
numeroComboBox.grid(row=0, column=2)


#Se define un widget Button, se lo asigna a una variable
aButton = ttk.Button(ventana, text="Clickeame!!!",command=clickMe)
#Posiciono el Button en el grid layout manager
aButton.grid(row=0, column=3)


#Pongo el foco sobre el Entry widget usando el metodo focus()
nombreTextBox.focus()

ventana.mainloop()