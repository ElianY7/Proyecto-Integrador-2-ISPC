from tkinter import * 
from tkinter import ttk 
from ClaseConectar import * 


root = Tk() 
root.title("Disqueria")
root.iconbitmap("images/cd_icon.ico")
root.geometry("1250x680") 

bg = PhotoImage(file="images/back.png")
bg_label = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

#Creacion del Notebook para crear varias pestañas.

notebook = ttk.Notebook(root) 

#Creacion de frames para las diferentes pestañas

tab = Frame(notebook)  
tab1 = Frame(notebook) 
tab2 = Frame(notebook) 
tab3 = Frame(notebook)


#Se añaden las tabs (o pestañas) al notebook con el metodo "add"

notebook.add(tab, text="Busqueda") 
notebook.add(tab1, text="Agregar/Actualizar") 
notebook.add(tab2, text="Borrar")
notebook.add(tab3, text="Referencias ID")


bg1 = PhotoImage(file="images/blue_back.png")

bg_label1 = Label(tab, image=bg1).place(x=0, y=0, relwidth=1, relheight=1)
bg_label2 = Label(tab1, image=bg1).place(x=0, y=0, relwidth=1, relheight=1)
bg_label3 = Label(tab2, image=bg1).place(x=0, y=0, relwidth=1, relheight=1)
bg_label4 = Label(tab3, image=bg1).place(x=0, y=0, relwidth=1, relheight=1)


#                        CREACION TABLA                        #

tabla = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="11")


# Configuracion de las columnas

tabla.column(1,width=50, minwidth=50, anchor="center")  
tabla.column(2,width=90, minwidth=90, anchor="center")  
tabla.column(3,width=180, minwidth=180, anchor="center") 
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

tabla.heading(1, text="ID", anchor="center")    
tabla.heading(2, text="Código", anchor="center")
tabla.heading(3, text="Nombre", anchor="center")
tabla.heading(4, text="Interprete", anchor="center")
tabla.heading(5, text="Genero", anchor="center")
tabla.heading(6, text="Temas", anchor="center")
tabla.heading(7, text="Discografia", anchor="center")
tabla.heading(8, text="Formato", anchor="center")
tabla.heading(9, text="Fecha", anchor="center")
tabla.heading(10, text="Precio", anchor="center")
tabla.heading(11, text="Stock", anchor="center")
tabla.heading(12, text="Caratula", anchor="center")



#######       SCROLLBARS DE LA TABLA       #######

scroll1 = Scrollbar(root, orient="vertical")
scroll1.configure(command=tabla.yview)
tabla.configure(yscrollcommand=scroll1.set)
scroll1.pack(fill=Y,side=RIGHT)

scroll = Scrollbar(root, orient="horizontal")
scroll.configure(command=tabla.xview)
tabla.configure(xscrollcommand=scroll.set)
scroll.pack(fill=X,side=BOTTOM)


#######################   ELEMENTOS TAB 0  #######################

def MostrarTabla():

    for row in tabla.get_children():
        tabla.delete(row)

    con = Conectar()
    resultados = con.MostrarAlbum()
    i = 0
    for ro in resultados:
        tabla.insert("", i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11]))
        i += 1

def BuscarTabla(var, value):

    for row in tabla.get_children():
        tabla.delete(row)

    con1 = Conectar()
    resultados = con1.BuscarAlbum(var, value)

    i = 0
    for ro in resultados:
        tabla.insert("", i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11]))
        i += 1

def ActualizarTabla():

    for row in tabla.get_children():
        tabla.delete(row)
    
    MostrarTabla()

    for row in tablagenero.get_children():
        tablagenero.delete(row)
    
    TablaGenero()   

    for row in tablainterprete.get_children():
        tablainterprete.delete(row)
    
    TablaInterprete()

    for row in tabladiscografia.get_children():
        tabladiscografia.delete(row)
    
    TablaDiscografia()


def BorrarRegistro(id_album):
    con2 = Conectar()
    con2.BorrarAlbum(id_album)



#######       VARIABLES       #######

Nombre_search= StringVar()
Interprete_search= StringVar()
Genero_search= StringVar()


Nombre_tx_search=Label(tab, text="Nombre Album", relief="groove", font=(40)).grid(row=0,column=0, padx=70, pady=30)
Nombre_ent_search=Entry(tab, textvariable=Nombre_search).grid(row=0,column=1, padx=10, pady=10)
Nombre_bt_search=Button(tab, text="Buscar por nombre", command=lambda:BuscarTabla("A.nombre", Nombre_search.get())).grid(row=0,column=2, padx=40, pady=10)

Interprete_tx_search=Label(tab, text="Intérprete",relief="groove", font=(40)).grid(row=1,column=0, padx=10, pady=30)
Interprete_ent_search=Entry(tab, textvariable=Interprete_search).grid(row=1,column=1, padx=10, pady=10)
Interprete_bt_search=Button(tab, text="Buscar por intérprete", command=lambda:BuscarTabla("I.nombre", Interprete_search.get())).grid(row=1,column=2, padx=10, pady=10)

Genero_tx_search=Label(tab, text="Género",relief="groove", font=(40)).grid(row=2,column=0, padx=10, pady=30)
Genero_ent_search=Entry(tab, textvariable=Genero_search).grid(row=2,column=1, padx=10, pady=10)
Genero_bt_search=Button(tab, text="Buscar por género", command=lambda:BuscarTabla("G.nombre", Genero_search.get())).grid(row=2,column=2, padx=10, pady=10)

ActualizarTabla_bt= Button(tab, text="Refrescar tabla", command=lambda:ActualizarTabla()).grid(row=3,column=1, pady=30)


#######################   ELEMENTOS TAB 1(AGREGAR/ACTUALIZAR)   #######################


#######       VARIABLES       #######

Id = StringVar() 
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

ID_tx = Label(tab1, text = "ID", relief="groove").grid(row=0, column=0, padx=10, pady=10)  
ID_ent = Entry(tab1, textvariable=Id).grid(row=0, column=1, padx=10, pady=10) 

Codigo_tx = Label(tab1, text = "Código", relief="groove").grid(row=1, column=0, padx=40, pady=10)
Codigo_ent = Entry(tab1, textvariable=Codigo).grid(row=1, column=1, padx=10, pady=10)

Nombre_tx = Label(tab1, text = "Nombre", relief="groove").grid(row=2, column=0, padx=10, pady=10)
Nombre_ent = Entry(tab1, textvariable=Nombre).grid(row=2, column=1, padx=10, pady=10)

Stock_tx = Label(tab1, text = "Stock", relief="groove").grid(row=0, column=3, padx=10, pady=10)
Stock_ent = Entry(tab1, textvariable=Stock).grid(row=0, column=4, padx=10, pady=10)

Cantidad_tx = Label(tab1, text = "Temas", relief="groove").grid(row=1, column=3, padx=10, pady=10)
Cantidad_ent = Entry(tab1, textvariable=Cantidad).grid(row=1, column=4, padx=10, pady=10)

Precio_tx = Label(tab1, text = "Precio", relief="groove").grid(row=2, column=3, padx=10, pady=10)
Precio_ent = Entry(tab1, textvariable=Precio).grid(row=2, column=4, padx=10, pady=10)

Interprete_tx = Label(tab1, text = "Intérprete", relief="groove").grid(row=4, column=0, padx=10, pady=(40,10))
Interprete_ent = Entry(tab1, textvariable=Interprete).grid(row=4, column=1, padx=10, pady=(40,10))

Genero_tx = Label(tab1, text = "Género", relief="groove").grid(row=5, column=0, padx=10, pady=10)
Genero_ent = Entry(tab1, textvariable=Genero).grid(row=5, column=1, padx=10, pady=10)

Discografia_tx = Label(tab1, text = "Discografía", relief="groove").grid(row=6, column=0, padx=10, pady=10)
Discografia_ent = Entry(tab1, textvariable=Discografia).grid(row=6, column=1, padx=10, pady=10)

Formato_tx = Label(tab1, text = "Formato", relief="groove").grid(row=4, column=3, padx=10, pady=(40,10))
Formato_ent = Entry(tab1, textvariable=Formato).grid(row=4, column=4, padx=10, pady=(40,10))

Fecha_tx = Label(tab1, text = "Año", relief="groove").grid(row=5, column=3, padx=10, pady=10)
Fecha_ent = Entry(tab1, textvariable=Fecha).grid(row=5, column=4, padx=10, pady=10)

Caratula_tx = Label(tab1, text = "Carátula", relief="groove").grid(row=6, column=3, padx=10, pady=10)
Caratula_ent = Entry(tab1, textvariable=Caratula).grid(row=6, column=4, padx=10, pady=10)


#---------------------------HASTA ACA---------------------------#

#Boton de Ingresar Datos
IngresarRegistro_bt = Button(tab1, text = "Ingresar Registro", command=lambda:InsertarRegistro(Id.get(), Codigo.get(), Nombre.get(), Interprete.get(), Genero.get(), Cantidad.get(), Discografia.get(), Formato.get(), Fecha.get(), Precio.get(), Stock.get(), Caratula.get())).grid(row=7, column=2, padx=10, pady=10)
ActualizarRegistro_bt = Button(tab1, text = "Actualizar Registro", command=lambda:ActualizarRegistro(Id.get(), Codigo.get(), Nombre.get(), Interprete.get(), Genero.get(), Cantidad.get(), Discografia.get(), Formato.get(), Fecha.get(), Precio.get(), Stock.get(), Caratula.get())).grid(row=8, column=2, padx=10, pady=10)



#######################   ELEMENTOS TAB 2 (BORRAR)   #######################
Cuidado_msg = Label(tab2, text = "Precaución!!! El registro será borrado permanentemente".upper(),bg='#fff', fg='#f00', font=(70),relief="sunken").grid(row=0, column=0, padx=30, pady=10, columnspan=3)

Borrar = IntVar()

Borrar_tx = Label(tab2, text = "ID de Album", relief="groove", font=(40)).grid(row=1, column=0, padx=10, pady=40)
Borrar_ent = Entry(tab2, textvariable=Borrar).grid(row=1, column=1, padx=10)
Borrar_bt = Button(tab2, text = "Borrar", command=lambda:BorrarRegistro(Borrar.get())).grid(row=1, column=2, padx=10)


def InsertarRegistro(Id, Codigo, Nombre, Interprete, Genero, Cantidad, Discografia, Formato, Fecha, Precio, Stock, Caratula):
    con3 = Conectar()
    con3.InsertarAlbum(Id, Codigo, Nombre, Interprete, Genero, Cantidad, Discografia, Formato, Fecha, Precio, Stock, Caratula)


def ActualizarRegistro(Id, Codigo, Nombre, Interprete, Genero, Cantidad, Discografia, Formato, Fecha, Precio, Stock, Caratula):
    con4 = Conectar()
    con4.ActualizarAlbum(Id, Codigo, Nombre, Interprete, Genero, Cantidad, Discografia, Formato, Fecha, Precio, Stock, Caratula)




#######################   ELEMENTOS TAB 3 (TABLAS ADICIONALES)   #######################

def TablaGenero():

    for row in tablagenero.get_children():
        tablagenero.delete(row)

    con5 = Conectar()
    resultados = con5.MostrarGenero()
    i = 0
    for ro in resultados:
        tablagenero.insert("", i, text="", values=(ro[0],ro[1]))
        i += 1

def TablaInterprete():

    for row in tablainterprete.get_children():
        tablainterprete.delete(row)

    con5 = Conectar()
    resultados = con5.MostrarInterprete()
    i = 0
    for ro in resultados:
        tablainterprete.insert("", i, text="", values=(ro[0],ro[1]))
        i += 1

def TablaDiscografia():

    for row in tabladiscografia.get_children():
        tabladiscografia.delete(row)

    con5 = Conectar()
    resultados = con5.MostrarDiscografia()
    i = 0
    for ro in resultados:
        tabladiscografia.insert("", i, text="", values=(ro[0],ro[1]))
        i += 1

def TablaFormato():
    for row in tablaformato.get_children():
        tablaformato.delete(row)

    con5 = Conectar()
    resultados = con5.MostrarFormato()
    i = 0
    for ro in resultados:
        tablaformato.insert("", i, text="", values=(ro[0],ro[1]))
        i += 1

#######################   TABLA DE GENERO   #######################

tablagenero = ttk.Treeview(tab3, columns=(1,2), show="headings", height="7")

# Configuracion de las columnas
tablagenero.column(1,width=30, minwidth=30, anchor="center")
tablagenero.column(2,width=90, minwidth=90, anchor="center")


# Esto es para el renglon de los encabezados
tablagenero.heading(1, text="ID", anchor="center")
tablagenero.heading(2, text="Genero", anchor="center")


TablaGenero()
tablagenero.grid(row=0, column=0, padx=30, pady=3)

#######################   TABLA DE INTERPRETE   #######################

tablainterprete = ttk.Treeview(tab3, columns=(1,2), show="headings", height="7")

# Configuracion de las columnas
tablainterprete.column(1,width=30, minwidth=30, anchor="center")
tablainterprete.column(2,width=110, minwidth=110, anchor="center")


# Esto es para el renglon de los encabezados
tablainterprete.heading(1, text="ID", anchor="center")
tablainterprete.heading(2, text="Interprete", anchor="center")


TablaInterprete()
tablainterprete.grid(row=0, column=1, padx=30, pady=3)

#######################   TABLA DE DISCOGRAFIA   #######################

tabladiscografia = ttk.Treeview(tab3, columns=(1,2), show="headings", height="7")

# Configuracion de las columnas de la tabla de discografia
tabladiscografia.column(1,width=30, minwidth=30, anchor="center")
tabladiscografia.column(2,width=150, minwidth=150, anchor="center")


# Esto es para el renglon de los encabezados de la tabla de discografia
tabladiscografia.heading(1, text="ID", anchor="center")
tabladiscografia.heading(2, text="Discografia", anchor="center")


TablaDiscografia()
tabladiscografia.grid(row=0, column=2, padx=30, pady=3)

#######################   TABLA DE FORMATO   #######################

tablaformato = ttk.Treeview(tab3, columns=(1,2), show="headings", height="4")

# Configuracion de las columnas de la tabla de formato
tablaformato.column(1,width=30, minwidth=30, anchor="center")
tablaformato.column(2,width=150, minwidth=150, anchor="center")


# Esto es para el renglon de los encabezados de la tabla de formato
tablaformato.heading(1, text="ID", anchor="center")
tablaformato.heading(2, text="Formato", anchor="center")


TablaFormato()
tablaformato.grid(row=4, column=2, padx=30, pady=3, rowspan=3)


#######################   AGERGAR INTERPRETE, GENERO Y DISCOGRAFIA   #######################

##### VARIABLES #####

Id1 = StringVar()
Id2 = StringVar()
Id3 = StringVar()

Nombre1 = StringVar()
Nombre2 = StringVar()
Nombre3 = StringVar()

Pais = StringVar()

##### FUNCIONES DE INSERT #####
def InsertarInterpreteTk(id,nombre,pais):
    InsObj1=Conectar()
    InsObj1.InsertarArtista(id,nombre,pais)


def InsertarGeneroTk(id,nombre):
    InsObj2=Conectar()
    InsObj2.InsertarGenero(id,nombre)


def InsertarDiscografiaTk(id,nombre):
    InsObj3=Conectar()
    InsObj3.InsertarDiscografia(id,nombre)




##### ENCABEZADO DE LABELS #####
IdIns_tx = Label(tab3, text = "ID", relief="groove").grid(row=1, column=0,pady=4)
NombreIns_tx = Label(tab3, text = "Nombre", relief="groove").grid(row=1, column=1)
PaisIns_tx = Label(tab3, text = "Pais", relief="groove").grid(row=1, column=2)

##### ENTRYS DE INTERPRETE #####
IdInterprete_ent = Entry(tab3, textvariable=Id1).grid(row=2, column=0)
NombreIns1_ent = Entry(tab3, textvariable=Nombre1).grid(row=2, column=1)
PaisIns_ent = Entry(tab3, textvariable=Pais).grid(row=2, column=2)

##### ENTRYS DE GENERO #####
IdGenero_ent = Entry(tab3, textvariable=Id2).grid(row=4, column=0)
NombreIns2_ent = Entry(tab3, textvariable=Nombre2).grid(row=4, column=1)

##### ENTRYS DE DISCOGRAFIA #####
IdDiscografia_ent = Entry(tab3, textvariable=Id3).grid(row=6, column=0)
NombreIns3_ent = Entry(tab3, textvariable=Nombre3).grid(row=6, column=1)

##### BOTONES PARA INSERTAR #####
InterperteIns_bt = Button(tab3, text = "Agregar Intérprete", command=lambda:InsertarInterpreteTk(Id1.get(),Nombre1.get(),Pais.get())).grid(row=3, column=1, pady=10)
GeneroIns_bt = Button(tab3, text = "Agregar Género", command=lambda:InsertarGeneroTk(Id2.get(),Nombre2.get())).grid(row=5, column=1, pady=10)
DiscografiaIns_bt = Button(tab3, text = "Agregar Discografía", command=lambda:InsertarDiscografiaTk(Id3.get(),Nombre3.get())).grid(row=7, column=1, pady=10)



notebook.pack()

tabla.pack()


MostrarTabla()

notebook.pack()


root.resizable(0,0)
root.mainloop()