from flask import jsonify
import mysql.connector

def get_entrenador(conexion):
    try:
        query="SELECT * FROM entrenador"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
         return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
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
            return jsonify({'idEntrenador': resultado[0], 'Nombre': resultado[1], 'Medallas': resultado[2]})
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar entrenador solicitado, 'Estado': 'Fallido' "})