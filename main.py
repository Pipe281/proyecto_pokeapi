from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from prueba import users_list
from validaciones import *

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

def leer_poke(id):
    try:
        conexion.conectar()
        sql = "SELECT idPokemon, idTipo, nombre FROM POKEMON WHERE idPokemon = '{0}'".format(id)
        resultado=conexion.query_leerPoke(sql)
        if resultado != None:
            poke = {'idPokemon': resultado[0], 'idTipo': resultado[1], 'nombre': resultado[2]}
            return poke
        else:
            return "Error", None
    except Exception as ex:
        raise ex

@app.route("/nuevo", methods=['POST'])
def nuevoPokemon():
    conexion.conectar()
    if (validar_idPokemon(request.json['idPokemon']) and validar_idTipo(request.json['idTipo']) and validar_pokeName(request.json['nombre'])):
        try:
            poke = leer_poke(request.json['idPokemon'])
            if poke != None:
                return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
            else:
                sql = "INSERT INTO dbpoke.pokemon (idPokemon, idTipo, nombre)VALUES('{0}', '{1}', '{2}')".format(request.json['idPokemon'],request.json['idTipo'],request.json['nombre'])
                resultado=conexion.query_insert(sql)     
                return jsonify({"mensaje": "Pokemon Ingresado correctamente"})
        except mysql.connector.Error as error: 
            print("Error al conectarse a la base de datos", error)   
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})    


if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



