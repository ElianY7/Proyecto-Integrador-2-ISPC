import mysql.connector

class Conectar():

############ CONSTRUCTOR DE LA CLASE ############

    def __init__(self):

        try:
            self.conexion = mysql.connector.connect(
                host = "localhost", 
                port = 3306,        
                user = "root",      
                password = "FhCD48203",   
                db = "proyecto_discografica" 
                )


        except Exception as ex: 
            print("Error de conexion -->" + str(ex))                                                   
            print("Revise los datos de conexion.")


################### METODOS DE LA CLASE ###################


    def MostrarAlbum(self):     
   
        try:
            cursor = self.conexion.cursor()           
            cursor.execute("""SELECT id_album,cod_album,A.nombre,I.nombre,G.nombre,cant_temas,D.nombre,tipo,fec_lanzamiento,precio,cantidad,caratula
            FROM Album A, Interprete I, Discografia D, Formato F, Genero G
            WHERE A.id_interprete = I.id_interprete  
            AND A.id_discografia = D.id_discografia
            AND A.id_formato = F.id_formato
            AND A.id_genero = G.id_genero
            ORDER BY id_album""")  

            resultados = cursor.fetchall() 
            cursor.close() 
            self.conexion.close() 

            return resultados 

        except mysql.connector.Error as ex: 
            print("Error de conexion.")
            print(ex)


    def MostrarGenero(self):
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""SELECT * FROM Genero ORDER BY nombre""") 

            resultados = cursor.fetchall()
            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:
            print("Error al mostrar Género.")
            print(ex)

   
    def MostrarInterprete(self):
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute("""SELECT * FROM Interprete ORDER BY nombre""") 

            resultados = cursor.fetchall()
            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:
            print("Error al mostrar Intérprete.")
            print(ex)


    def MostrarDiscografia(self):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("""SELECT * FROM Discografia ORDER BY nombre""") 

            resultados = cursor.fetchall()
            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:
            print("Error al mostrar Discografia.")
            print(ex)


    def MostrarFormato(self):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("""SELECT * FROM Formato""") 

            resultados = cursor.fetchall()
            cursor.close()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:
            print("Error al mostrar Formato.")
            print(ex)


########## METODO PARA INSERTAR ALBUMS ##########

    def InsertarAlbum(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula): 
        
        try:
            cursor = self.conexion.cursor()          
            cursor.execute("""INSERT INTO Album (id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula)
            VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")""".format(id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula))
     
            self.conexion.commit() 
            cursor.close() 
            self.conexion.close()
            print("Album insertado correctamente")

        except Exception as ex:
            print("Error al intentar ingresar registro:" + str(ex))


########## METODO PARA BORRAR ALBUMS ##########

    def BorrarAlbum(self,id_album):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("DELETE FROM Album WHERE id_album = {} ".format(id_album))
            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            print("Borrado exitoso")

        except Exception as ex:
            print("Error al intentar borrar registro con ID:" + str(id_album) + "\nInformacion de error: " + str(ex))


########## METODO PARA BUSCAR ALBUMS ##########

    def BuscarAlbum(self,var,value):

        try:
            cursor = self.conexion.cursor()                
            cursor.execute(""" SELECT id_album,cod_album,A.nombre,I.nombre,G.nombre,cant_temas,D.nombre,tipo,fec_lanzamiento,precio,cantidad,caratula
            FROM Album A, Interprete I, Discografia D, Formato F, Genero G
            WHERE A.id_interprete = I.id_interprete AND A.id_discografia = D.id_discografia AND A.id_formato = F.id_formato AND A.id_genero = G.id_genero
            AND  {} LIKE "{}%" 
            ORDER BY id_album""".format(var,value))

            resultados = cursor.fetchall()
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:
            print("Error de Busqueda.")
            print(ex)        


########## METODO PARA ACTUALIZAR ALBUMS ##########

    def ActualizarAlbum(self,id_album,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula):
        
        try:
            cursor = self.conexion.cursor()       
            cursor.execute("""UPDATE Album SET cod_album = {}, nombre = "{}", id_interprete = {}, id_genero = {}, cant_temas = {}, 
            id_discografia = {}, id_formato = {}, fec_lanzamiento = "{}", precio = {}, cantidad = {}, caratula = "{}"
            WHERE id_album = {} """.format(cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografia,id_formato,fec_lanzamiento,precio,cantidad,caratula,id_album))
            
            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            print("Album actualizado")

        except Exception as ex:
            print("Error al intentar actualizar registro. " + str(ex))


########## METODO PARA INSERTAR INTERPRETE, GENERO, DISCOGRAFIA ##########

    def InsertarArtista(self,id_interprete,nombre,pais):

        try:
            cursor = self.conexion.cursor()
            cursor.execute("""INSERT INTO Interprete (id_interprete,nombre,pais) VALUES ("{}","{}","{}")""".format(id_interprete,nombre,pais))

            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            print("Intérprete agregado correctamente")

        except Exception as ex:
            print("Error al intentar ingresar Artista:" + str(ex))


    def InsertarGenero(self,id_genero,nombre):

        try:
            cursor = self.conexion.cursor()          
            cursor.execute("""INSERT INTO Genero (id_genero,nombre) VALUES ("{}","{}")""".format(id_genero,nombre))

            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            print("Género agregado correctamente")

        except Exception as ex:
            print("Error al intentar ingresar Genero:" + str(ex))


    def InsertarDiscografia(self,id_discografia,nombre):

        try:
            cursor = self.conexion.cursor()          
            cursor.execute("""INSERT INTO Discografia (id_discografia,nombre) VALUES ("{}","{}")""".format(id_discografia,nombre))

            self.conexion.commit()
            cursor.close()
            self.conexion.close()
            print("Discografía agregada correctamente")

        except Exception as ex:
            print("Error al intentar ingresar Discografia:" + str(ex))



