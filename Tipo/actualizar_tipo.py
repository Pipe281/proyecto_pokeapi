from flask import request, jsonify

def update_tipo(id: int, conexion):
    try:
        id = int(id)
        nombre = str(request.json['nombre'])
        tipo = int(request.json['idTipo'])
        sql = "SELECT COUNT(*) FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and nombre.isalpha() and len(nombre) <= 25:
            try:
                sql = "UPDATE dbpoke.tipo SET nombre = '{0}', idTipo = '{1}' WHERE idTipo = '{2}'".format(nombre, tipo, id)
                conexion.query_actualizar(sql)
                return jsonify({"Mensaje": "Tipo de Pokemon actualizado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro actualizar Tipo solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})