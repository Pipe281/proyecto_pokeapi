from flask import jsonify
import mysql.connector

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
        resultado = conexion.query_fetchone(sql)
        print(resultado)
        if resultado > 0 :
            query = "SELECT pokemon.nombre, entrenador.nombre, idEquipo FROM equipo INNER JOIN pokemon on equipo.idPokemon = pokemon.idPokemon INNER JOIN entrenador on equipo.idEntrenador  = entrenador.idEntrenador WHERE equipo = '{0}'".format(id)
            resultado=conexion.query_select(query)
            equipos = []
            for rest in resultado:
                equipos.append( {'Pokemon': rest[0], 'Entrenador': rest[1],'ID equipo': rest[2]})
            return jsonify(equipos)
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar el Equipo solicitado, 'Estado': 'Fallido' "})