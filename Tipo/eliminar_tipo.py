from flask import jsonify

def delete_tipo(id: int, conexion):
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0:
            try:
                sql = "DELETE FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
                conexion.query_delete(sql)
                return jsonify({"Mensaje": "Se elimina Tipo de Pokemon ingresado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro eliminar Tipo solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})
   