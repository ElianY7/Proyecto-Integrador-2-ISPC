import mysql.connector

class Conectar():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "sql10.freesqldatabase.com",
                port = 3306,
                user = "sql10524975",
                password = "C1IUWSssA1",
                db = "sql10524975"
                )

        except Exception as ex:
            print("Error de conexion -->" + str(ex))
            print("Revise los datos de conexion.")

    
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
            self.conexion.close()

            return resultados

        except mysql.connector.Error as ex:

            print("Error de conexion.")
            print(ex)

