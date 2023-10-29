from flask import Flask, json

app = Flask(__name__)

# Diccionario de música
canciones = {
    "cancion1": {
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "año": 1975
    },
    "cancion2": {
        "titulo": "Space Oddity",
        "artista": "David Bowie",
        "año": 1971
    },
    "cancion3": {
        "titulo": "Five Years",
        "artista": "David Bowie",
        "año": 1976
    },
    "cancion4": {
        "titulo": "Yesterday",
        "artista": "The Beatles",
        "año": 1965
    }
}

#Diccionario secundario de musica
canciones2 = {
    "cancion5": {
        "titulo": "Crystals",
        "artista": "Moon",
        "año": 2012
    },
    "cancion6": {
        "titulo": "Mr Crowley",
        "artista": "Ozzy",
        "año": 1889
    }
}

# Crear conjuntos de canciones de David Bowie y Pink Floyd
conjunto_david_bowie = {"Space Oddity", "Life on Mars", "Heroes","Starman"}
conjunto_pink_floyd = {"Comfortably Numb", "Wish You Were Here", "Time"}

# Tupla inicial
mi_tupla = ("Space Oddity", "Life on Mars", "Heroes")
mi_tupla2 = ("Crystals", "Knock Knock")





#Metodos------------------------------------------------------

# Mostrar todas las canciones
@app.route("/canciones_diccionario")
def show_canciones():
    formatted_canciones = []
    for clave, valor in canciones.items():
        formatted_cancion = f"Clave: {clave} Titulo: {valor['titulo']}, Artista: {valor['artista']}, Año: {valor['año']}"
        formatted_canciones.append(formatted_cancion)
    return "<br>".join(formatted_canciones)

# Mostrar una canción de un diccionario en específico: ejemplo, la canción 1 del diccionario canciones se accede con la URL /canciones/cancion1
@app.route("/canciones_diccionario/<path:diccionario>")
def show_diccionario(diccionario):
    if diccionario not in canciones:
        return "Canción no encontrada", 404
    
    cancion = canciones[diccionario]
    formatted_cancion = [f"Clave: {diccionario}, Titulo: {cancion['titulo']}, Artista: {cancion['artista']}, Año: {cancion['año']}"]
    return "<br>".join(formatted_cancion)

# Ruta para agregar una nueva canción al diccionario
@app.route("/agregar_cancion_diccionario/<string:clave>/<string:titulo>/<string:artista>/<int:anio>")
def agregar_cancion(clave, titulo, artista, anio):
    nueva_cancion = {
        "titulo": titulo,
        "artista": artista,
        "año": anio
    }
    canciones[clave] = nueva_cancion
    return "Canción agregada exitosamente"


# Ruta para eliminar una canción específica
@app.route("/eliminar_cancion_diccionario/<clave>")
def eliminar_cancion(clave):
    if clave in canciones:
        del canciones[clave]
        return "Canción eliminada exitosamente"
    else:
        return "Canción no encontrada"

# Función para modificar un valor en el diccionario
def modificar_valor(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    else:
        return False

# Ruta para modificar un valor en el diccionario
@app.route("/modificar_cancion_diccionario/<clave>/<nuevo_titulo>/<nuevo_artista>/<int:nuevo_anio>")
def modificar_cancion(clave, nuevo_titulo, nuevo_artista, nuevo_anio):
    try:
        nuevo_anio = int(nuevo_anio)
        nueva_cancion = {
            "titulo": nuevo_titulo,
            "artista": nuevo_artista,
            "año": nuevo_anio
        }
        if modificar_valor(canciones, clave, nueva_cancion):
            return "Canción modificada exitosamente"
        else:
            return "Canción no encontrada"
    except ValueError:
        return "El nuevo año debe ser un número entero"

# Ruta para combinar dos diccionarios
@app.route("/combinardiccionario/<diccionario1>/<diccionario2>")
def combinar_diccionarios(diccionario1, diccionario2):
    # Verifica si los nombres de los diccionarios pasados en la URL existen en el espacio global
    if diccionario1 not in globals() or diccionario2 not in globals():
        return "Uno o ambos diccionarios no existen", 400

    # Accede a los diccionarios reales utilizando los nombres y asigna a dicc1 y dicc2
    dicc1 = globals()[diccionario1]
    dicc2 = globals()[diccionario2]

    # Combina los diccionarios dicc1 y dicc2 en un nuevo diccionario llamado resultado
    resultado = {}
    resultado.update(dicc1)
    resultado.update(dicc2)

    formatted_diccionarios = []
    for clave, valor in resultado.items():
        # Formatea la información de cada canción en el diccionario combinado
        formatted_diccionario = f"Clave: {clave} Titulo: {valor['titulo']}, Artista: {valor['artista']}, Año: {valor['año']}"
        formatted_diccionarios.append(formatted_diccionario)
    
    # Devuelve una respuesta HTML que muestra las canciones combinadas
    return "<br>".join(formatted_diccionarios)








#Conjuntos

# Ruta para mostrar el conjunto de canciones de un artista
@app.route("/conjuntos/<artista>")
def conjutoPrint(artista):
    if artista == "david_bowie":
        return 
    elif artista == "pink_floyd":
        return "<br>".join(conjunto_pink_floyd)
    else:
        return "Artista no encontrado", 404


# Función para agregar una canción a un conjunto de un artista
@app.route("/agregar_conjunto/<artista>/<cancion>")
def agregar_cancion_route(artista, cancion):
    if artista == "david_bowie":
        conjunto = conjunto_david_bowie
    elif artista == "pink_floyd":
        conjunto = conjunto_pink_floyd
    else:
        return "Artista no encontrado", 404

    if cancion not in conjunto:
        conjunto.add(cancion)
        return f"Canción '{cancion}' agregada a las canciones de {artista}"
    else:
        return f"Canción '{cancion}' ya existe en las canciones de {artista}"


#Funcion para eliminar
def eliminar_elemento(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    else:
        return False

#Implementacion de la ruta para eliminar
@app.route("/eliminar_cancion_conjunto/<artista>/<cancion>")
def eliminar_cancionConjunto(artista, cancion):
    if artista == "david_bowie":
        conjunto = conjunto_david_bowie
    elif artista == "pink_floyd":
        conjunto = conjunto_pink_floyd
    else:
        return "Artista no encontrado", 404

    if eliminar_elemento(conjunto, cancion):
        return f"Canción '{cancion}' eliminada del conjunto de {artista}"
    else:
        return f"Canción '{cancion}' no encontrada en el conjunto de {artista}"


#Combinar conjuntos

def combinar_conjuntos(nombre_conjunto1, nombre_conjunto2):
    # Utiliza globals().get para obtener los conjuntos por nombre
    conjunto1 = globals().get(nombre_conjunto1, set())
    conjunto2 = globals().get(nombre_conjunto2, set())
    resultado = conjunto1 | conjunto2
    return resultado

@app.route("/combinar_conjuntos/<nombre_conjunto1>/<nombre_conjunto2>")
def mostrar_conjunto_combinado(nombre_conjunto1, nombre_conjunto2):
    conjunto_combinado = combinar_conjuntos(nombre_conjunto1, nombre_conjunto2)
    return "<br>".join(conjunto_combinado)

#diferencia de conjuntos

def diferencia_de_conjuntos(nombre_conjunto1, nombre_conjunto2):
    # Utiliza globals().get para obtener los conjuntos por nombre
    conjunto1 = globals().get(nombre_conjunto1, set())
    conjunto2 = globals().get(nombre_conjunto2, set())
    resultado = conjunto1 - conjunto2
    return resultado

@app.route("/diferencia_de_conjuntos/<nombre_conjunto1>/<nombre_conjunto2>")
def mostrar_diferencia_de_conjuntos(nombre_conjunto1, nombre_conjunto2):
    diferencia = diferencia_de_conjuntos(nombre_conjunto1, nombre_conjunto2)
    return "<br>".join(diferencia)





#Tuplas

#Mostrar tupla
def print_format(tupla):
    formatted = "\n".join([f"- {elemento}" for elemento in tupla])
    return formatted

@app.route("/imprimir_tupla")
def imprimir_tupla():
    return print_format(mi_tupla)

#Agregar
def agregar_elemento_a_tupla(tupla, elemento):
    nueva_tupla = tupla + (elemento,)
    return nueva_tupla

@app.route("/agregar_a_tupla/<elemento>")
def agregar_a_tupla(elemento):
    global mi_tupla
    mi_tupla = agregar_elemento_a_tupla(mi_tupla, elemento)
    return f"Elemento '{elemento}' agregado a la tupla"


#Eliminar
def eliminar_item(tupla, elemento_a_eliminar):
    nueva_tupla = tuple(item for item in tupla if item != elemento_a_eliminar)
    return nueva_tupla

@app.route("/eliminar_de_tupla/<elemento>")
def eliminar_de_tupla(elemento):
    global mi_tupla
    mi_tupla = eliminar_item(mi_tupla, elemento)
    return f"Elemento '{elemento}' eliminado de la tupla"


#Concatenar
def concatenar_tuplas(tupla1, tupla2):
    nueva_tupla = tupla1 + tupla2
    return nueva_tupla

@app.route("/concatenar_tuplas/<nombre_tupla1>/<nombre_tupla2>")
def concatenar_y_mostrar(nombre_tupla1, nombre_tupla2):
    tupla1 = globals().get(nombre_tupla1, ())
    tupla2 = globals().get(nombre_tupla2, ())
    
    tupla_concatenada = concatenar_tuplas(tupla1, tupla2)
    return print_format(tupla_concatenada)

#Revertir
def revertir_tupla(tupla):
    nueva_tupla = tuple(reversed(tupla))
    return nueva_tupla


@app.route("/revertir_tupla/<nombre_tupla>")
def revertir_la_tupla(nombre_tupla):
    tupla = globals().get(nombre_tupla, ())
    if isinstance(tupla, tuple):
        nueva_tupla = revertir_tupla(tupla)
        globals()[nombre_tupla] = nueva_tupla
        return f"Tupla '{nombre_tupla}' revertida:\n{print_format(nueva_tupla)}"
    else:
        return f"Tupla '{nombre_tupla}' no encontrada", 404

if __name__ == '__main__':
    app.run()
