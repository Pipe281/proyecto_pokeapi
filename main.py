from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from validaciones import validar_idPokemon
from eliminar import eliminar_Poke

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

@app.route("/pokemon/<id>", methods=['GET'])
def getOnePokemon(id): 
    try:
        conexion.conectar()
        query="SELECT * FROM pokemon WHERE idPokemon = '{0}'".format(id)
        resultado=conexion.query_select_one(query)
        resultado = {'idPokemon': resultado[0], 'idTipo': resultado[1], 'Nombre': resultado[2]}
        print(resultado)
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

    return resultado

@app.route("/pokemon/nuevo", methods=['POST'])
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

@app.route("/pokemon/<id>", methods=['DELETE'])
def eliminarPoke(id):
    conexion.conectar()
    try:      
        poke = eliminar_Poke(id, conexion)
        print(poke)
        return jsonify({"Mensaje": "Pokemon Eliminado correctamente, 'Estado': 'Eliminado' "})
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al eliminar Pokemon"})    

@app.route("/pokemon/actualizar", methods=['PUT'])
def actualizar_poke():
    conexion.conectar()
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



