from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def get_equipo(conexion):
    try:
        conexion.conectar()
        query="SELECT pokemon.nombre, entrenador.nombre, idEquipo FROM equipo INNER JOIN pokemon on equipo.idPokemon = pokemon.idPokemon INNER JOIN entrenador on equipo.idEntrenador  = entrenador.idEntrenador"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

    return resultado


def get_one_equipo(id: int, conexion):   
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.equipo WHERE idEquipo = '{0}'".format(id)
        resultado = conexion.query_select_one(sql)
        if resultado != 0 and id <= 8:
            query = "SELECT pokemon.nombre, entrenador.nombre, idEquipo FROM equipo INNER JOIN pokemon on equipo.idPokemon = pokemon.idPokemon INNER JOIN entrenador on equipo.idEntrenador  = entrenador.idEntrenador WHERE idEquipo = '{0}'".format(id)
            resultado=conexion.query_select(query)
            return jsonify({'Pokemon': resultado[0], 'Entrenador': resultado[1],'Número equipo': resultado[2]})
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar el Equipo solicitado, 'Estado': 'Fallido' "})