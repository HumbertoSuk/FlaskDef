# Práctica de Flask: Manejo de Datos

En esta práctica de Flask, hemos creado una aplicación web que utiliza diferentes estructuras de datos y métodos para manipular información sobre canciones, conjuntos y tuplas. A continuación, se describen los métodos implementados:

## Manejo de Diccionarios

### Mostrar todas las canciones
- Ruta: `/canciones_diccionario`
- Descripción: Muestra todas las canciones almacenadas en un diccionario. Cada canción incluye su título, artista y año.

### Mostrar una canción específica
- Ruta: `/canciones_diccionario/<clave>`
- Descripción: Muestra los detalles de una canción específica identificada por su clave en el diccionario.

### Agregar una nueva canción
- Ruta: `/agregar_cancion_diccionario/<clave>/<titulo>/<artista>/<anio>`
- Descripción: Permite agregar una nueva canción al diccionario proporcionando su clave, título, artista y año.

### Eliminar una canción
- Ruta: `/eliminar_cancion_diccionario/<clave>`
- Descripción: Permite eliminar una canción específica del diccionario según su clave.

### Modificar una canción
- Ruta: `/modificar_cancion_diccionario/<clave>/<nuevo_titulo>/<nuevo_artista>/<nuevo_anio>`
- Descripción: Permite modificar el título, artista y año de una canción en el diccionario.

### Combinar dos diccionarios
- Ruta: `/combinardiccionario/<diccionario1>/<diccionario2>`
- Descripción: Combina dos diccionarios especificados en la URL y muestra las canciones combinadas.

## Manejo de Conjuntos

### Mostrar canciones de un artista
- Ruta: `/conjuntos/<artista>`
- Descripción: Muestra las canciones de un artista específico utilizando conjuntos.

### Agregar canción a un conjunto
- Ruta: `/agregar_conjunto/<artista>/<cancion>`
- Descripción: Permite agregar una canción al conjunto de un artista. Si la canción ya existe, se muestra un mensaje.

### Eliminar canción de un conjunto
- Ruta: `/eliminar_cancion_conjunto/<artista>/<cancion>`
- Descripción: Permite eliminar una canción del conjunto de un artista.

### Combinar dos conjuntos
- Ruta: `/combinar_conjuntos/<nombre_conjunto1>/<nombre_conjunto2>`
- Descripción: Combina dos conjuntos especificados en la URL y muestra las canciones combinadas.

### Diferencia entre dos conjuntos
- Ruta: `/diferencia_de_conjuntos/<nombre_conjunto1>/<nombre_conjunto2>`
- Descripción: Muestra la diferencia entre dos conjuntos especificados en la URL.

## Manejo de Tuplas

### Mostrar una tupla
- Ruta: `/imprimir_tupla`
- Descripción: Muestra los elementos de una tupla en formato de lista.

### Agregar elemento a una tupla
- Ruta: `/agregar_a_tupla/<elemento>`
- Descripción: Permite agregar un elemento a una tupla existente.

### Eliminar elemento de una tupla
- Ruta: `/eliminar_de_tupla/<elemento>`
- Descripción: Permite eliminar un elemento de una tupla existente.

### Concatenar dos tuplas
- Ruta: `/concatenar_tuplas/<nombre_tupla1>/<nombre_tupla2>`
- Descripción: Combina dos tuplas especificadas en la URL y muestra los elementos concatenados.

### Revertir una tupla
- Ruta: `/revertir_tupla/<nombre_tupla>`
- Descripción: Revierte los elementos de una tupla especificada en la URL y muestra la tupla revertida.
