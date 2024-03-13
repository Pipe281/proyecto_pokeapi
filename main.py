from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from prueba import users_list

@app.route('/')
def hello():
    return jsonify({"message": "Hello!"})


@app.route("/pokemon")
def getPokemon():
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

    return resultado

if __name__ == '__main__':
    app.run(debug=True, port=4000)




