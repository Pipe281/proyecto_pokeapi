from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from validaciones import validar_idPokemon, validar_post
from eliminar import eliminar_Poke
from actualizar import actualizar_poke
from Tipo.nuevo_tipo import insert_tipo
from Tipo.consultar_tipo import get_tipo
from Tipo.eliminar_tipo import eliminar_tipo
from Tipo.actualizar_tipo import update_tipo

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
    conexion.conectar()
    poke = validar_idPokemon(id, conexion)
  
    if (isinstance(poke, int) and poke > 0) and poke <= 151:
        try:
            conexion.conectar()
            query="SELECT * FROM pokemon WHERE idPokemon = '{0}'".format(id)
            resultado=conexion.query_select_one(query)
            resultado = {'idPokemon': resultado[0], 'idTipo': resultado[1], 'Nombre': resultado[2]}
            return resultado
            #print(resultado)
        except mysql.connector.Error as error: 
            print("Error al conectarse a la base de datos", error)
        finally:
            conexion.desconectar()

    if (isinstance(poke, int) and poke == 0):
        return jsonify({'Mensaje': "Pokemon no existe"})    
    else:
        return jsonify({'Mensaje': "Error SQL", 'Estado': 'Fallido'})

@app.route("/pokemon/nuevo", methods=['POST'])
def nuevoPokemon():
    conexion.conectar()
    poke = validar_post(request.json['idPokemon'], conexion)
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

@app.route("/pokemon/<id>", methods=['PUT'])
def actualizarPoke(id):
    conexion.conectar()
    try:      
        poke = actualizar_poke(id, conexion)
        print(poke)
        return jsonify({"Mensaje": "Pokemon Actualizado correctamente, 'Estado': 'Actualizado' "})
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al eliminar Pokemon"})    

#Sección para Tipo de Pokemon

@app.route("/pokemon/tipos")
def getTipo(): 
    conexion.conectar()
    poke_tipo = get_tipo(conexion)
    return poke_tipo

@app.route("/pokemon/tipos/nuevo", methods=['POST'])
def tipo():
    conexion.conectar()
    poke_tipo = insert_tipo(request.json['idTipo'],request.json['nombre'], conexion)
    return poke_tipo

@app.route("/pokemon/tipos/<id>", methods=['DELETE'])
def deleteTipo(id):
    conexion.conectar()
    try:      
        poke = eliminar_tipo(id, conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al eliminar el Tipo del Pokemon"}) 

@app.route("/pokemon/tipos/<id>", methods=['PUT'])
def updateTipo(id):
    try:
        conexion.conectar()
        poke_tipo = update_tipo(id, conexion)
        return poke_tipo
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al eliminar Pokemon"})  

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



