from flask import jsonify

def post_entrenador(id: int, medallas: int, nombre: str, conexion):
    if isinstance(id, int) and isinstance(nombre, str) and len(nombre) <= 25 and (isinstance(medallas, int) or medallas is None):
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.entrenador WHERE idEntrenador = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if medallas is None: 
                medallas =  0
            if resultado == 0:
                sql = "INSERT INTO dbpoke.entrenador (idEntrenador, nombre, medallas)VALUES('{0}', '{1}', '{2}')".format(id, nombre, medallas)
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Entrenador Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})
        except Exception as ex:
            return jsonify({'Mensaje' : "Valide información ingresada"})
    else:
        return jsonify({"Mensaje": "No es posible ingresar la solicitud valide datos, 'Estado': 'Fallido' "})

