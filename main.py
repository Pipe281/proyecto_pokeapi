from flask import Flask, jsonify, request
from conexion import conexion_bd
import mysql.connector
#from test import 
app = Flask(__name__)

from Pokemon.consultar_pokemon import get_pokemon, get_one_pokemon
from Pokemon.nuevo_pokemon import post_pokemon
from Pokemon.eliminar_pokemon import delete_pokemon
from Pokemon.actualizar_pokemon import update_pokemon
from Tipo.nuevo_tipo import post_tipo
from Tipo.consultar_tipo import get_tipo
from Tipo.eliminar_tipo import delete_tipo
from Tipo.actualizar_tipo import update_tipo
from Entrenador.consultar_entrenador import get_entrenador, get_one_entrenador
from Entrenador.nuevo_entrenador import post_entrenador
from Entrenador.eliminar_entrenador import delete_entrenador
from Entrenador.actualizar_entrenador import update_entrenador
from Gimnasio.consultar_gimnasio import get_gimnasio, get_one_gimnasio
from Gimnasio.nuevo_gimnasio import post_gimnasio
from Gimnasio.eliminar_gimnasio import delete_gimnasio
from Gimnasio.actualizar_gimnasio import update_gimnasio
from Equipo.consultar_equipo import get_equipo, get_one_equipo
from Equipo.nuevo_equipo import post_equipo
from Equipo.eliminar_equipo import delete_equipo
#Variables Globales
conexion= conexion_bd("localhost","root", "root", "dbpoke")

@app.route('/')
def hello():
    return jsonify({"message": "Hello!"})

#Sección para Pokemones
@app.route("/pokemon")
def getPokemon():
    conexion.conectar()
    entrenador = get_pokemon(conexion)
    return entrenador


@app.route("/pokemon/<id>", methods=['GET'])
def getOnePokemon(id):
    try:
        conexion.conectar()
        poke = get_one_pokemon(id, conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 


@app.route("/pokemon/nuevo", methods=['POST'])
def postPokemon():
    try:
        conexion.conectar()
        poke = post_pokemon(request.json['idPokemon'], request.json['idTipo'], request.json['nombre'], conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/pokemon/<id>", methods=['DELETE'])
def deletePokemon(id):
    try:
        conexion.conectar()   
        poke = delete_pokemon(id, conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 
    
       
@app.route("/pokemon/<id>", methods=['PUT'])
def updatePokemon(id):
    try:
        conexion.conectar()
        poke = update_pokemon(id, conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"})  

#Sección para Tipo de Pokemon

@app.route("/pokemon/tipos")
def getTipo(): 
    conexion.conectar()
    poke_tipo = get_tipo(conexion)
    return poke_tipo

@app.route("/pokemon/tipos/nuevo", methods=['POST'])
def tipo():
    conexion.conectar()
    poke_tipo = post_tipo(request.json['idTipo'],request.json['nombre'], conexion)
    return poke_tipo

@app.route("/pokemon/tipos/<id>", methods=['DELETE'])
def deleteTipo(id):
    conexion.conectar()
    try:      
        poke = delete_tipo(id, conexion)
        return poke
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"}) 

@app.route("/pokemon/tipos/<id>", methods=['PUT'])
def updateTipo(id):
    try:
        conexion.conectar()
        poke_tipo = update_tipo(id, conexion)
        return poke_tipo
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"})  


#Sección para Entrenador

@app.route("/entrenador")
def getEntrenador():
    conexion.conectar()
    entrenador = get_entrenador(conexion)
    return entrenador

@app.route("/entrenador/<id>", methods=['GET'])
def getOneEntrenador(id):
    conexion.conectar()
    entrenador = get_one_entrenador(id, conexion)
    return entrenador

@app.route("/entrenador/nuevo", methods= ['POST'])
def postEntrenador():
    try:
        conexion.conectar()
        entrenador = post_entrenador(request.json['idEntrenador'], request.json['medallas'], request.json['nombre'], conexion)
        return entrenador
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/entrenador/<id>", methods=['DELETE'])
def deleteEntrenador(id):
    try:
        conexion.conectar()   
        entrenador = delete_entrenador(id, conexion)
        return entrenador
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
    except mysql.connector.Error as error: 
        return jsonify({'Mensaje' : "Error al eliminar el entrenador"}) 

@app.route("/entrenador/<id>", methods=['PUT'])
def updateEntrenador(id):
    try:
        conexion.conectar()
        entrenador = update_entrenador(id, conexion)
        return entrenador
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 
    

# Sección para Gimnasio
@app.route("/gimnasio/")
def getGimnasio():
    try:
        conexion.conectar()
        entrenador = get_gimnasio(conexion)
        return entrenador
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/gimnasio/<id>", methods=['GET'])
def getOneGimasio(id):
    try:
        conexion.conectar()
        gimnasio = get_one_gimnasio(id, conexion)
        return gimnasio
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 


@app.route("/gimnasio/nuevo", methods=['POST'])
def postGimnasio():
    try:
        conexion.conectar()
        gimnasio = post_gimnasio(request.json['idGimnasio'], request.json['ubicacion'], request.json['lider_gym'],request.json['nombre'], conexion)
        return gimnasio
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/gimnasio/<id>", methods=['DELETE'])
def deleteGimnasio(id):
    try:
        conexion.conectar()   
        gimansio = delete_gimnasio(id, conexion)
        return gimansio
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/gimnasio/<id>", methods=['PUT'])
def updateGimnasio(id):
    try:
        conexion.conectar()
        gimansio = update_gimnasio(id, conexion)
        return gimansio
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

#Sección para Equipo
@app.route("/equipo/")
def getEquipo():
    try:
        conexion.conectar()
        equipo = get_equipo(conexion)
        return equipo
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/equipo/<id>", methods=['GET'])
def getOneEquipo(id):
    try:
        conexion.conectar()
        equipo = get_one_equipo(id, conexion)
        return equipo
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except KeyError as error:
        return jsonify({'Mensaje' : "Valide información ingresada"}) 

@app.route("/equipo/nuevo", methods=['POST'])
def postEquipo():
    try:
        conexion.conectar()
        equipo = post_equipo(request.json['idEquipo'], request.json['idPokemon'], request.json['idEntrenador'],request.json['equipo'], conexion)
        return equipo
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al conectarse a la Base de Datos"}) 

@app.route("/equipo/<id>", methods=['DELETE'])
def deleteEquipo(id):
    try:
        conexion.conectar()   
        equipo = delete_equipo(id, conexion)
        return equipo
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
    except mysql.connector.Error as error: 
        return jsonify({'Mensaje' : "Error al eliminar el Equipo"}) 

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



