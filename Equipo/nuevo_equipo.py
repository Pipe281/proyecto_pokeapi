from flask import jsonify
import mysql.connector
from conexion import conexion_bd

def post_equipo(equipo: int, pokemon, entrenador, conexion):
    if isinstance(equipo, int) and equipo > 0 and isinstance(pokemon, int) and isinstance(entrenador, int):
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.equipo WHERE idEquipo = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.equipo (idEquipo, idPokemon, idEntrenador)VALUES('{0}', '{1}', '{2}')".format(equipo, pokemon, entrenador)
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Equipo Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})
        except Exception as ex:
            return jsonify({'Mensaje' : "Valide información ingresada"})
    else:
        return jsonify({"Mensaje": "No es posible ingresar la solicitud valide datos, 'Estado': 'Fallido' "})
