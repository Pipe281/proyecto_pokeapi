from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from prueba import users_list
from validaciones import validar_idPokemon

#Variables Globales
conexion= conexion_bd("localhost","root", "root", "dbpoke")

@app.route('/')
def hello():
    return jsonify({"message": "Hello!"})


@app.route("/pokemon")
def getPokemon(): 
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

@app.route("/nuevo", methods=['POST'])
def nuevoPokemon():
    conexion.conectar()
    poke = validar_idPokemon(request.json['idPokemon'], conexion)
    if (poke == 0): # and validar_idTipo(request.json['idTipo']) and validar_pokeName(request.json['nombre'])):
        try:           
            sql = "INSERT INTO dbpoke.pokemon (idPokemon, idTipo, nombre)VALUES('{0}', '{1}', '{2}')".format(request.json['idPokemon'],request.json['idTipo'],request.json['nombre'])
            resultado=conexion.query_insert(sql)     
            return jsonify({"Mensaje": "Pokemon Ingresado correctamente, 'Estado': 'Exitoso' "})
        except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al insertar Pokemon"})
    else:
        return jsonify({'Mensaje': "Pokemon ya existe o existe un error al validar el dato", 'Estado': 'Fallido' })    


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



