#######################   ELEMENTOS TAB 1(AGREGAR/ACTUALIZAR)   #######################


#######       VARIABLES       #######

Id = StringVar()  #Todas estas variables de tipo StringVar o string, nos van a servir para almacenar todos los datos que ingresemos en los campos de la pestaña de añadir o actualizar album.
Codigo = StringVar()
Nombre = StringVar()
Cantidad = StringVar()
Stock = StringVar()
Precio = StringVar()
Formato = StringVar()
Discografia = StringVar()
Genero = StringVar()
Interprete = StringVar()
Caratula = StringVar()
Fecha = StringVar()

#######       LABELS Y ENTRYS PARA TAB1       #######

#Los labels permiten mostrar texto en la interfaz. Los entrys son campos vacios en los que se puede ingresar texto.

ID_tx = Label(tab1, text = "ID").grid(row=0, column=0, padx=10, pady=10)  #Se crea un un objeto (llamado "ID_tx") de la clase Label. Este objeto nos sirve para mostrar texto en la interfaz grafica.
#Se le pasan 2 parametros, el primero indica a que pestaña pertenece (tab1 en este caso), y el argumento text="ID" sirve para establecer el texto que queremos que aparezca en pantalla
                                #Se usa el metodo .grid para ubicar el Label dentro de tab1. Y se le pasan varios argumentos
                                #row indica la fila en la que se va a ubicar y column la columna. padx y pady indica el espacio que va a haber con otros elementos tanto en x como en y. En este caso son 10 y 10.

ID_ent = Entry(tab1, textvariable=Id).grid(row=0, column=1, padx=10, pady=10)  #Se crea un un objeto (llamado "ID_ent") de la clase Entry. Este objeto es un campo para ingresar texto.
                                                                                #IMPORTANTE# con el argumento textvariable=Id, establecemos que el texto que sea escrito en ese campo vacio va a ser almacenado en la variable Id


#Se repite el proceso con los demas variando parametros como la ubicacion que van a llevar y el texto, etc.

Codigo_tx = Label(tab1, text = "Código").grid(row=1, column=0, padx=10, pady=10)
Codigo_ent = Entry(tab1, textvariable=Codigo).grid(row=1, column=1, padx=10, pady=10)

Nombre_tx = Label(tab1, text = "Nombre").grid(row=2, column=0, padx=10, pady=10)
Nombre_ent = Entry(tab1, textvariable=Nombre).grid(row=2, column=1, padx=10, pady=10)

Stock_tx = Label(tab1, text = "Stock").grid(row=0, column=3, padx=10, pady=10)
Stock_ent = Entry(tab1, textvariable=Stock).grid(row=0, column=4, padx=10, pady=10)

Cantidad_tx = Label(tab1, text = "Cantidad").grid(row=1, column=3, padx=10, pady=10)
Cantidad_ent = Entry(tab1, textvariable=Cantidad).grid(row=1, column=4, padx=10, pady=10)

Precio_tx = Label(tab1, text = "Precio").grid(row=2, column=3, padx=10, pady=10)
Precio_ent = Entry(tab1, textvariable=Precio).grid(row=2, column=4, padx=10, pady=10)

Interprete_tx = Label(tab1, text = "Interprete").grid(row=4, column=0, padx=10, pady=(40,10))
Interprete_ent = Entry(tab1, textvariable=Interprete).grid(row=4, column=1, padx=10, pady=(40,10))

Genero_tx = Label(tab1, text = "Género").grid(row=5, column=0, padx=10, pady=10)
Genero_ent = Entry(tab1, textvariable=Genero).grid(row=5, column=1, padx=10, pady=10)

Discografia_tx = Label(tab1, text = "Discografía").grid(row=6, column=0, padx=10, pady=10)
Discografia_ent = Entry(tab1, textvariable=Discografia).grid(row=6, column=1, padx=10, pady=10)

Formato_tx = Label(tab1, text = "Formato").grid(row=4, column=3, padx=10, pady=(40,10))
Formato_ent = Entry(tab1, textvariable=Formato).grid(row=4, column=4, padx=10, pady=(40,10))

Fecha_tx = Label(tab1, text = "Año").grid(row=5, column=3, padx=10, pady=10)
Fecha_ent = Entry(tab1, textvariable=Fecha).grid(row=5, column=4, padx=10, pady=10)

Caratula_tx = Label(tab1, text = "Carátula").grid(row=6, column=3, padx=10, pady=10)
Caratula_ent = Entry(tab1, textvariable=Caratula).grid(row=6, column=4, padx=10, pady=10)

