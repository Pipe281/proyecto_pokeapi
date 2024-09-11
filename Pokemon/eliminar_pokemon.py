from flask import jsonify

def delete_pokemon(id: int, conexion):
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.pokemon WHERE idPokemon = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0:
            try:
                sql = "DELETE FROM dbpoke.pokemon WHERE idPokemon = '{0}'".format(id)
                conexion.query_delete(sql)
                return jsonify({"Mensaje": "Se eliminó el Pokemon ingresado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro eliminar el Pokemon ingresado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})
    