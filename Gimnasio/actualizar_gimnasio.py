from flask import request, jsonify

def update_gimnasio(id: int, conexion):
    try:
        id = int(id)
        ubicacion = str(request.json['ubicacion'])
        lider_gym = str(request.json['lider_gym'])
        nombre = str(request.json['nombre'])
        sql = "SELECT COUNT(*) FROM dbpoke.gimnasio WHERE idGimnasio = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and lider_gym.isalpha() and len(lider_gym) <= 10 and ubicacion.isalpha() and len(ubicacion) <= 10 and nombre.isalpha() and len(nombre) <= 10:
            try:
                sql = "UPDATE dbpoke.gimnasio SET idGimnasio = '{0}', ubicacion = '{1}', lider_gym = '{2}', nombre = '{3}' WHERE idGimnasio = '{4}'".format(request.json['idGimnasio'], ubicacion, lider_gym, nombre, id)  
                conexion.query_actualizar(sql)
                return jsonify({"Mensaje": "Gimnasio actualizado, 'Estado': 'Exitoso' "})
            except Exception as ex:
                return jsonify({"Mensaje": "No se logro actualizar el Gimnasio solicitado, 'Estado': 'Fallido' "})
        else:
            return jsonify({"Mensaje": "Datos no validos, verificar 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "El ID ingresado no es valido, 'Estado': 'Fallido' "})
    aa