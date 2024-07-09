from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def update_tipo(id: int, conexion):
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and resultado <=18:
            try:
                sql = "UPDATE dbpoke.tipo SET nombre = '{0}', idTipo = '{1}' WHERE idTipo = '{2}'".format(request.json['nombre'], request.json['idTipo'], id)
                conexion.query_actualizar(sql)
                return jsonify({"Mensaje": "Tipo de Pokemon actualizado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro actualizar Tipo solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})