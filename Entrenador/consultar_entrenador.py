from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def get_entrenador(conexion):
    try:
        conexion.conectar()
        query="SELECT * FROM entrenador"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

    return resultado


def get_one_entrenador(id: int, conexion):   
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.entrenador WHERE idEntrenador = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0:
            query="SELECT * FROM entrenador WHERE idEntrenador = '{0}'".format(id)
            resultado=conexion.query_select_one(query)
            return jsonify({'idPokemon': resultado[0], 'idTipo': resultado[1], 'Nombre': resultado[2]})
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar entrenador solicitado, 'Estado': 'Fallido' "})