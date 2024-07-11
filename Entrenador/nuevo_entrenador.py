from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def post_entrenador(id: int, medallas: int, nombre: str, conexion):
    if isinstance(id, int) and isinstance(medallas, int) and isinstance(nombre, str) and len(nombre) <= 25:
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.entrenador WHERE idEntrenador = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.entrenador (idEntrenador, medallas, nombre)VALUES('{0}', '{1}', '{2}')".format(id, medallas, nombre)    
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Entrenador Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})  # El dato ya existe en la base de datos
        except Exception as ex:
            print("Error al validar dato:", ex)
            return False
    else:
        return jsonify({"Mensaje": "No es posible ingresar la solicitud valide datos, 'Estado': 'Fallido' "})

#entrenador no mayor a 25caracteres
#(request.json['idEntrenador'],request.json['medallas'],request.json['nombre'])