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
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
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
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})    

@app.route("/pokemon/<id>", methods=['PUT'])
def actualizarPoke(id):
    conexion.conectar()
    try:      
        poke = actualizar_poke(id, conexion)
        print(poke)
        return jsonify({"Mensaje": "Pokemon Actualizado correctamente, 'Estado': 'Actualizado' "})
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})    

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
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al conectarse a la Base de Datos"}) 

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
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al conectarse a la Base de Datos"}) 

@app.route("/gimnasio/<id>", methods=['DELETE'])
def deleteGimnasio(id):
    try:
        conexion.conectar()   
        gimansio = delete_gimnasio(id, conexion)
        return gimansio
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
    except mysql.connector.Error as error: 
        return jsonify({'Mensaje' : "Error al eliminar el gimasio"}) 

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
        equipo = post_equipo(request.json['idEquipo'], request.json['idPokemon'], request.json['idEntrenador'], conexion)
        return equipo
    except KeyError as error:
        return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})  
    except mysql.connector.Error as error: 
            return jsonify({'Mensaje' : "Error al conectarse a la Base de Datos"}) 

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    



