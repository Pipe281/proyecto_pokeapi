from flask import jsonify

def post_gimnasio(id: int, ubicacion: str, lider_gym: str, nombre: str, conexion):
    if isinstance(id, int) and id > 0 and ubicacion.isalpha() and isinstance(ubicacion, str) and len(ubicacion) <= 10 and lider_gym.isalpha() and isinstance(lider_gym, str) and len(lider_gym) <= 10 and nombre.isalpha() and isinstance(nombre, str) and len(nombre) <= 10:
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.gimnasio WHERE idGimnasio = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.gimnasio (idGimnasio, ubicacion, lider_gym, nombre)VALUES('{0}', '{1}', '{2}', '{3}')".format(id, ubicacion, lider_gym, nombre)
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Gimnasio Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})
        except Exception as ex:
            return jsonify({'Mensaje' : "Valide información ingresada"})
    else:
        return jsonify({"Mensaje": "No es posible ingresar la solicitud valide datos, 'Estado': 'Fallido' "})