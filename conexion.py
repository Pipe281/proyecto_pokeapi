import mysql.connector

# Establece los parámetros de conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dbpoke"
)

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
