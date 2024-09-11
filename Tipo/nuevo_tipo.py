from flask import jsonify

def post_tipo(id: int, nombre: str, conexion):
    if isinstance(id, int) and id <= 18 and id >= 1 and nombre.isalpha() and len(nombre) <= 25:
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.tipo WHERE idTipo = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.tipo (nombre, idTipo)VALUES('{0}', '{1}')".format(nombre, id)    
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Tipo de Pokemon Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})  # El dato ya existe en la base de datos
        except Exception as ex:
            return jsonify({'Mensaje' : "Valide información ingresada"})
    else:
        return jsonify({"Mensaje": "No es posible ingresar el Tipo valide datos, 'Estado': 'Fallido' "})