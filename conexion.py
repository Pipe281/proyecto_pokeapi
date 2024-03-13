import mysql.connector

class conexion_bd:
    def __init__(self, host, user, password, database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.connect=None

    def conectar(self):
        self.connect=mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def desconectar(self):
        if self.connect:
            self.connect.close()

    def query_select(self, consulta):
        cursor=self.connect.cursor()
        cursor.execute(consulta)
        return cursor.fetchall()

def main():
    conexion= conexion_bd("localhost","root", "root", "dbpoke")
    try:
        conexion.conectar()
        query="SELECT * FROM pokemon"
        resultado=conexion.query_select(query)
        print(resultado)
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

main()
''' 
# Verifica si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

    # Ejecuta consultas u operaciones en la base de datos
    # Aquí puedes ejecutar tus consultas SQL, por ejemplo:
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pokemon")
    filas = cursor.fetchall()

    # Imprime los resultados
    for fila in filas:
        print(fila)

    # Cierra el cursor y la conexión
    cursor.close()
    conexion.close()
    
else:
    print("Error al conectar a la base de datos")
'''