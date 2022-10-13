from tkinter import * #Importa biblioteca Tkinter
from tkinter import ttk #Da acceso a widgets adicionales
from ClaseConectar import *

#######       CONFIGURACION DE VENTANA       #######

root = Tk()
root.title("Disquería")
root.geometry("1250x680")

#######       CONFIGURACION DE NOTEBOOK       #######

notebook = ttk.Notebook(root) #Este widget notebook nos permite almacenar varias ventanas

#Creacion de frames para las diferentes ventanas
tab = Frame(notebook)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)


notebook.add(tab, text="Busqueda")
notebook.add(tab1, text="Agregar/Actualizar")
notebook.add(tab2, text="Borrar")
notebook.add(tab3, text="Referencias ID")


notebook.pack()



root.resizable(0,0)
root.mainloop()