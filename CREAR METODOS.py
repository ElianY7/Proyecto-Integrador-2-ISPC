
import mysql.connector #Se importa el mysql connector que nos permite establecer la conexion con la base de datos que hemos creado

class Conectar(): #Se crea la clase "Conectar" para poder crear objetos en el otro archivo de la interfaz grafica

################################# CONSTRUCTOR DE LA CLASE #################################

#El constructor o  metodo __init__ siempre se debe usar al crear una clase.
#Se puede crear una clase sin constructor, porque python establece uno por defecto, pero lo recomendado es escribirlo manualmente.
#El constructor permite establecer ciertos valores que despues seran usado por los objetos que salgan de esta clase.

    def __init__(self):


        try:                    #El try - except sirven para que el programa no se detenga apenas encuentre un error.
                                #Primero el programa intenta ejecutar lo que esta dentro de try. Si algo falla, salta al except y ejecuta lo del except.
                                # Si dentro del try, no hay ningun error, se ejecuta todo lo del try y se omite los que esta en el except 

            #Se establece el atributo "self.conexion" al cual le pasamos los datos necesarios para poder realizar la conexion con nuestra base de datos

            self.conexion = mysql.connector.connect(
                host = "localhost", #Host por defecto
                port = 3306,        #Puerto por defecto para la conexion con MySQL
                user = "root",      #Nombre de usuario establecido en MySQL, por defecto se pone root, a no ser de que se haya creado un usuario diferente en MySQL
                password = "FhCD48203",   #Contraseña que se usa para acceder a la base de datos
                db = "proyecto_discografica" #Nombre de la base de datos creada en MySQL
                )


        except Exception as ex: #Se captura la excepcion (o el error que se produjo en el try) en la variable "ex"
            print("Error de conexion -->" + str(ex)) #Con este print se muestra la informacion del error.                                                    
            print("Revise los datos de conexion.")


################################# METODOS DE LA CLASE #################################


    def MostrarAlbum(self):     #Metodo de la clase conectar para mostrar la tabla principal con todos los albums y sus datos.
   
        try:

            cursor = self.conexion.cursor() #Se crea la variable cursor que se encarga de realizar la consulta sql a la base de datos y traer los datos obtenidos.

            #"cursor.execute" se encarga de mandar la sentencia SQL que esta entre parentesis.
            cursor.execute("""SELECT id_album,cod_album,A.nombre,I.nombre,G.nombre,cant_temas,D.nombre,tipo,fec_lanzamiento,precio,cantidad,caratula
            FROM Album A, Interprete I, Discografia D, Formato F, Genero G
            WHERE A.id_interprete = I.id_interprete  
            AND A.id_discografia = D.id_discografia
            AND A.id_formato = F.id_formato
            AND A.id_genero = G.id_genero
            ORDER BY id_album""")  #Se ordena por el id_album

            #El **SELECT** trae una tabla con los siguentes encabezados: id_album,cod_album,A.nombre,I.nombre,G.nombre,cant_temas,D.nombre,tipo,fec_lanzamiento,precio,cantidad,caratula

            #El **FROM** indica de que tablas se sacan esas columnas: Album A, Interprete I, Discografia D, Formato F, Genero G
            #La letra que esta al lado de cada tabla en el **FROM** por ejemplo en: "Genero G", esa letra se usa para abreviar y no tener que escribir todo el nombre de la tabla genero en ese caso.
            #Por eso en la primera linea donde esta el **SELECT** cuando dice, por ejemplo, A.nombre, esto es lo mismo que poner Album.nombre
            #Por ejemplo el A.nombre, trae la columna nombre de la tabla Album
            #Los que tiene la abreviacion es porque es necesario especificar a que tabla pertenece esa columna, por ejemplo en "A.nombre,I.nombre,G.nombre", hay tres columnas con el mismo nombre pero de distintas tablas.

            #El **WHERE** relaciona las columnas de la tabla album(que son claves foraneas), con las claves primarias de las otras tablas.


            resultados = cursor.fetchall() #La variable resultados almacena todos los registros que trae el cursor

            cursor.close() #Se debe cerrar el cursor.
            self.conexion.close() #Se debe cerrar la conexion para que la base de datos nos deje hacer mas consultas.

            return resultados #Esto indica que el metodo MostrarAlbum, cuando se lo use, va a devolver todo lo que se encuentra en la variable resultados.

        except mysql.connector.Error as ex: #Esto funciona igual que el Except anterior

            print("Error de conexion.")
            print(ex)

#Estas otras tablas funcionan igual que la primera pero son mucho mas simples.
#Estas tablas se muestran en la ultima pestaña de la Interfaz grafica.

    def MostrarGenero(self):
        
        try:

            cursor = self.conexion.cursor()

            cursor.execute("""SELECT * FROM Genero""") #Se trae toda la tabla Genero

            resultados = cursor.fetchall()

            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:

            print("Error al mostrar genero.")
            print(ex)

   
    def MostrarInterprete(self):
        
        try:

            cursor = self.conexion.cursor()

            cursor.execute("""SELECT * FROM Interprete""") #Se trae toda la tabla Interprete

            resultados = cursor.fetchall()

            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:

            print("Error al mostrar Interprete.")
            print(ex)
    
    def MostrarDiscografia(self):

        try:

            cursor = self.conexion.cursor()

            cursor.execute("""SELECT * FROM Discografia""") #Se trae toda la tabla discografia

            resultados = cursor.fetchall()

            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:

            print("Error al mostrar Discografia.")
            print(ex)

########## METODO PARA INSERTAR ALBUMS ##########

    def InsertarAlbum(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula): #Se establecen estos parametros que van a recibir los datos que ingresemos en la interfaz virtual
        
        try:

            cursor = self.conexion.cursor()          

            cursor.execute("""INSERT INTO Album (id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula)
            VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula))
            #Las llaves remplazan el valor que se les pasa.
            #Por ejemplo, la primera llave correspone al id_album, este argumento se lo pasamos cuando ingresamos el id del album en la pestaña de agregar album en la interfaz grafica.

            self.conexion.commit() #EL commit nos sirve para realizar el cambio en la base de datos directamente.
                                    #El commit se va a usar cada vez que se quiera modificar algo en la base de datos, ya sea eliminar, agregar o actualizar algun registro.
                                    #El commit no es necesario con los metodos que solo muestran tablas ya que no se esta modificando la estructura de la tabla, solo se le esta haciendo una consulta y se traen los datos, pero no se modifica nada.

            cursor.close() #Se cierra el cursor
            self.conexion.close() #Se cierra la conexion

        except Exception as ex:
            print("Error al intentar ingresar registro:" + str(ex))