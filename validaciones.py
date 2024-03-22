import mysql.connector
from conexion import conexion_bd
#Globales
# Valida el idPokemon (si es numérico y de longitud 6).
def validar_idPokemon(id: int, conexion):
    if isinstance(id, int) and id < 151:
        try:
            sql = "SELECT COUNT(*) FROM pokemon WHERE idPokemon = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                print ("Todo bien")
                return resultado  # El dato no existe en la base de datos
            else:
                print ("Todo mal")
                return resultado  # El dato ya existe en la base de datos
        except Exception as ex:
            print("Error al validar dato:", ex)
            return False
    else:
        print ("Error")


'''
def validar_idTipo(id: int) -> bool:
    if isinstance(id, int) and id < 9:
        return id
    
def validar_pokeName(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 25)
'''