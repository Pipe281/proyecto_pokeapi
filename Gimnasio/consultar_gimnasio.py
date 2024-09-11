from flask import jsonify
import mysql.connector

def get_gimnasio(conexion):
    try:
        conexion.conectar()
        query="SELECT * FROM gimnasio"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

    return resultado


def get_one_gimnasio(id: int, conexion):   
    try:
        id = int(id)
        sql = "SELECT COUNT(*) FROM dbpoke.gimnasio WHERE idGimnasio = '{0}'".format(id)
        resultado = conexion.query_fetchone(sql)
        if resultado != 0 and id <= 8:
            query="SELECT * FROM gimnasio WHERE idGimnasio = '{0}'".format(id)
            resultado=conexion.query_select_one(query)
            return jsonify({'IdGimnasio': resultado[0], 'Ubicación': resultado[1],'Lider de Gimnsio': resultado[2], 'Tipo Gimnasio': resultado[3]})
        else:
             return jsonify({"Mensaje": "ID no encontrado en Base de Datos, 'Estado': 'Fallido' "})
    except Exception as ex:
        return jsonify({"Mensaje": "No es posible encontrar Gimnasio solicitado, 'Estado': 'Fallido' "})