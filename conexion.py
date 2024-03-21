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
    
    def query_leerPoke(self, consulta):
        cursor=self.connect.cursor()
        cursor.execute(consulta)
        return cursor.fetchone()

    def query_insert(self, ingreso):
        cursor=self.connect.cursor()
        cursor.execute(ingreso)
        self.connect.commit()
        return cursor.fetchall()


