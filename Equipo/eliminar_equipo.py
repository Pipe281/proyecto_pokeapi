from flask import jsonify
import mysql.connector
from conexion import conexion_bd

def delete_equipo(id: int, conexion):
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.equipo WHERE idEquipo = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and resultado <=18:
            try:
                sql = "DELETE FROM dbpoke.equipo WHERE idEquipo = '{0}'".format(id)
                conexion.query_delete(sql)
                return jsonify({"Mensaje": "Se elimina Equipo ingresado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro eliminar el Equipo solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})
   