import mysql.connector
from conexion import conexion_bd

def eliminar_Poke(id: int, conexion):
    if id != 0:
        try:
            sql = "DELETE FROM dbpoke.pokemon WHERE idPokemon = '{0}'".format(id)
            conexion.query_delete(sql)
            return "eliminado"
        except Exception as ex:
            return False
    else:
        return ("Error")    
