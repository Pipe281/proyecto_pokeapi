# Valida el idPokemon (si es numérico y de longitud 6).
def validar_idPokemon(id: int) -> bool:
    if isinstance(id, int) and id < 151:
        return id
    

def validar_idTipo(id: int) -> bool:
    if isinstance(id, int) and id < 9:
        return id
    
def validar_pokeName(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 25)