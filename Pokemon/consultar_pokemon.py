from flask import jsonify
import mysql.connector

def get_pokemon(conexion):
    try:
        query="SELECT * FROM pokemon"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
         return jsonify({'Mensaje' : "Error al consultar la Base de Datos"})
    finally:
        conexion.desconectar()

    return resultado


def get_one_pokemon(id: int, conexion):   
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.pokemon WHERE idPokemon = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if (isinstance(id, int) and id > 0) and id <= 151:
            query="select pokemon.nombre, tipo.nombre, idPokemon from pokemon inner join tipo on pokemon.idTipo  = tipo.idTipo where idPokemon = '{0}'".format(id)
            resultado=conexion.query_select_one(query)
            resultado = {'Nombre': resultado[0], 'Tipo': resultado[1], 'Número': resultado[2]}
            return resultado
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar Pokemon solicitado, 'Estado': 'Fallido' "})