from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def update_entrenador(id: int, conexion):
    try:
        id = int(id)
        medallas = int(request.json['medallas'])
        nombre = str(request.json['nombre'])
        sql = "SELECT COUNT(*) FROM dbpoke.entrenador WHERE idEntrenador = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and medallas >= 0 and medallas <= 8 and len(nombre) <= 20:
            try:
                sql = "UPDATE dbpoke.entrenador SET idEntrenador = '{0}', nombre = '{1}', medallas = '{2}' WHERE idEntrenador = '{3}'".format(request.json['idEntrenador'], nombre, medallas, id)  
                conexion.query_actualizar(sql)
                return jsonify({"Mensaje": "Entrenador actualizado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro actualizar el entrenador solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "Datos no validos, verificar 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})