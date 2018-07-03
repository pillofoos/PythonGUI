import tkinter as tk

class MainApp:
    def __init__(self, main):
        self.main_window = main
        self.main_window.title("Mi App OOP con Tkinter")
        self.frame = tk.Frame(self.main_window)
        self.button1 = tk.Button(self.frame, text='Nueva Ventana', width=25,command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        #crear el resto de la GUI aqui


    def new_window(self):
        self.newWindow = tk.Toplevel(self.main_window)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.main_window = master
        self.frame = tk.Frame(self.main_window)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.main_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
