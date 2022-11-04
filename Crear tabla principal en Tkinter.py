from tkinter import * #Se Importa toda la biblioteca Tkinter. El "*" indica que se importa toda la bibloteca o modulo.
from tkinter import ttk #Se importa el ttk, el cual da acceso a widgets adicionales de Tkinter(como por ejemplo el Treeview que es la tabla).
from claseconectar import * #Se importa todo el archivo "claseconectar.py"


root = Tk() #Se crea un objeto de la clase Tk, el cual va a ser nuestra ventana
root.title("Disqueria") #Le cambiamos el nombre de la ventana con root.title
root.geometry("1250x680") #Se establece el tamaño o las dimensiones de la ventana


#Creacion del Notebook para crear varias pestañas.

notebook = ttk.Notebook(root) #Se crea un objeto de la clase "Notebook" y se le pasa como argumento el valor root. Este valor indica que el notebook va a estar ubicado dentro de la ventana

#Creacion de frames para las diferentes pestañas

tab = Frame(notebook)  #Se crea un objeto de la clase Frame llamado, en este caso, "tab". Este objeto sirve para almacenar los widgets de Tkinter en un espacio.
tab1 = Frame(notebook) #Los widgets de Tkinter son los Entry(cuadros en los que se puede ingresar texto), los Label(texto que se muestra en pantalla), los Button(botones), etc...
tab2 = Frame(notebook) #Entonces en los frames almacenamos y ubicamos los diferentes elementos de nuestra interfaz grafica
tab3 = Frame(notebook)


#Se añaden las tabs (o pestañas) al notebook con el metodo "add"

notebook.add(tab, text="Busqueda") #Se le pasan dos argumentos al metodo add, el primero, tab (indica que esa pestaña va a ser añadida al notebook), y se le pasa el argumento text = "busqueda" para nombrar la pestaña esa.
notebook.add(tab1, text="Agregar/Actualizar") #Se repite el proceso con las demas pestañas
notebook.add(tab2, text="Borrar")
notebook.add(tab3, text="Referencias ID")




#                        CREACION TABLA                        #

tabla = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="11")

#Se crea un objeto (llamado "tabla") de la clase TreeView.
#Un objeto de la clase TreeView es basicamente una tabla.
#El primer argumento ("root") indica a donde pertenece este objeto.
#Se pasan cada una de las columnas que va a tener la tabla con el argumento "columns"
#"show=headings" sirve para ocultar la columna 0 (Esta columna viene por defecto con la tabla)
#El argumento "height" indica la cantidad de filas que va a mostrar la tabla


# Configuracion de las columnas

tabla.column(1,width=50, minwidth=50, anchor="center")  #Se pasan varios parametros para configurar las columnas
tabla.column(2,width=90, minwidth=90, anchor="center")  #El primer parametro(que es un numero) establece la posicion de esa columna
tabla.column(3,width=180, minwidth=180, anchor="center") #Se establece el ancho(width) y el ancho minimo(minwidth) de cada columna
tabla.column(4,width=140, minwidth=140, anchor="center")
tabla.column(5,width=90, minwidth=90, anchor="center")
tabla.column(6,width=60, minwidth=60, anchor="center")
tabla.column(7,width=140, minwidth=140, anchor="center")
tabla.column(8,width=80, minwidth=80, anchor="center")
tabla.column(9,width=80, minwidth=80, anchor="center")
tabla.column(10,width=80, minwidth=80, anchor="center")
tabla.column(11,width=60, minwidth=60, anchor="center")
tabla.column(12,width=170, minwidth=170, anchor="center")

# Esto es para configurar el renglon de los encabezados que se encuentran en la tabla

tabla.heading(1, text="ID", anchor="center")    #El primerargumento indica la posicion del encabezado
tabla.heading(2, text="Código", anchor="center")#Con el argumento "text" pasamos el texto de cada encabezado
tabla.heading(3, text="Nombre", anchor="center")#Con "anchor = center" centramos el texto
tabla.heading(4, text="Interprete", anchor="center")
tabla.heading(5, text="Genero", anchor="center")
tabla.heading(6, text="Cantidad", anchor="center")
tabla.heading(7, text="Discografia", anchor="center")
tabla.heading(8, text="Formato", anchor="center")
tabla.heading(9, text="Fecha", anchor="center")
tabla.heading(10, text="Precio", anchor="center")
tabla.heading(11, text="Stock", anchor="center")
tabla.heading(12, text="Caratula", anchor="center")