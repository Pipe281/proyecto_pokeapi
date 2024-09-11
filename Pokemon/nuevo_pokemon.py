from flask import jsonify

def post_pokemon(id: int, tipo, pokemon: str, conexion):
    if isinstance(id, int) and id > 0 and isinstance(pokemon, str) and len(pokemon) <= 25 and pokemon.isalpha():
        try:
            sql = "SELECT COUNT(*) FROM dbpoke.pokemon WHERE idPokemon = '{0}'".format(id)
            resultado = conexion.query_fetchone(sql)
            if resultado == 0:
                sql = "INSERT INTO dbpoke.pokemon (idPokemon, idTipo, nombre)VALUES('{0}', '{1}', '{2}')".format(id, tipo, pokemon)
                conexion.query_insert(sql)
                return jsonify({"Mensaje": "Pokemon Ingresado correctamente, 'Estado': 'Exitoso' "})
            else:
                return jsonify({"Mensaje": "El ID se encuentra repetido, 'Estado': 'Fallido' "})
        except Exception as ex:
            return jsonify({'Mensaje' : "Valide información ingresada"})
    else:
        return jsonify({"Mensaje": "No es posible ingresar la solicitud valide datos, 'Estado': 'Fallido' "})