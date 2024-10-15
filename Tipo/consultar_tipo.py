from flask import request, jsonify
import mysql.connector

def get_tipo(conexion):
    try:
        query="SELECT * FROM tipo"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
         return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
    finally:
        conexion.desconectar()

    return resultado