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
    print(validar_idPokemon(request.json['idPokemon'], conexion))
    if (validar_idPokemon(request.json['idPokemon'], conexion)): # and validar_idTipo(request.json['idTipo']) and validar_pokeName(request.json['nombre'])):
        try:
            poke = conexion.validar_idPokemon()
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
    



