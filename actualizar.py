import mysql.connector
from flask import jsonify, request
from conexion import conexion_bd

def actualizar_poke(id: int, conexion):
    if id != 0:
        try:
            sql = "UPDATE dbpoke.pokemon SET nombre = '{0}', idTipo = '{1}' WHERE idPokemon = '{2}'".format(request.json['nombre'], request.json['idTipo'], id)
            conexion.query_actualizar(sql)
            return "Actualizado"
        except Exception as ex:
            return False
    else:
        return ("Error")    

