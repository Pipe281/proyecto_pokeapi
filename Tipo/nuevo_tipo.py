from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd  

def insert_tipo(id: int, nombre: str, conexion):
    if isinstance(id, int) and id <= 18 and id >= 1 and isinstance(nombre, str) and len(nombre) <= 25:
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.tipo (nombre, idTipo)VALUES('{0}', '{1}')".format(request.json['nombre'],request.json['idTipo'])    
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Tipo de Pokemon Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})  # El dato ya existe en la base de datos
        except Exception as ex:
            print("Error al validar dato:", ex)
            return False
    else:
        return jsonify({"Mensaje": "No es posible ingresar el Tipo valide datos, 'Estado': 'Fallido' "})