from flask import request, jsonify
import mysql.connector
from conexion import conexion_bd

def get_tipo(conexion):
    try:
        conexion.conectar()
        query="SELECT * FROM tipo"
        resultado=conexion.query_select(query)
        return resultado
    except mysql.connector.Error as error: 
        print("Error al conectarse a la base de datos", error)
    finally:
        conexion.desconectar()

    return resultado