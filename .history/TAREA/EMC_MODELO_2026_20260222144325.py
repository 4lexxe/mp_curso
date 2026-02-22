"""
================================================================================
CONSIGNA DEL EJERCICIO - EXAMEN PARCIAL 2026 (PRACTICA)
================================================================================

Un videoclub proporciona un archivo de texto llamado alquileres.txt que contiene
todos los registros de películas alquiladas. Cada línea del archivo sigue el 
siguiente formato:

fecha;pelicula;director;cliente;estado

Donde:
• fecha: fecha del alquiler (formato YYYY-MM-DD)
• pelicula: nombre de la película
• director: nombre del director de la película
• cliente: nombre del cliente que alquiló
• estado: "devuelto", "pendiente" o "vencido"

NOTA: Para aprobar debe tener al menos dos consignas hechas más el punto obligatorio.
"""
================================================================================
CONSIGNA DEL EJERCICIO - EXAMEN PARCIAL 2026 (PRACTICA)
================================================================================

Un videoclub proporciona un archivo de texto llamado alquileres.txt que contiene
todos los registros de películas alquiladas. Cada línea del archivo sigue el 
siguiente formato:

fecha;pelicula;director;cliente;estado

Donde:
• fecha: fecha del alquiler (formato YYYY-MM-DD)
• pelicula: nombre de la película
• director: nombre del director de la película
• cliente: nombre del cliente que alquiló
• estado: "devuelto", "pendiente" o "vencido"

NOTA: Para aprobar debe tener al menos dos consignas hechas más el punto obligatorio.

CONSIGNAS:

1) Implementar la lectura del archivo alquileres.txt y devolver los registros
   en forma de lista. Si hay error debe crear el archivo con datos de ejemplo.

2) Listar las películas alquiladas en un determinado año y mes, excluyendo
   los alquileres del cliente "gerente".

3) Determinar la cantidad de veces que una película de un director dado fue
   alquilada.

4) Enlistar las películas que no hayan sido devueltas (estado distinto a 
   "devuelto") mostrando cliente y estado.

5) Listar los 3 clientes con más alquileres realizados.

6) (PUNTO OBLIGATORIO) Para cada director crear un archivo con nombre
   informe_[director].txt con la siguiente estructura:
   • Director
   • Total de películas alquiladas
   • Total de películas devueltas
   • Total de películas pendientes
   • Total de películas vencidas
   • Película más alquilada

Ejemplo:
Director: Steven Spielberg
Total de películas alquiladas: 20
Total de películas devueltas: 12
Total de películas pendientes: 5
Total de películas vencidas: 3
Película más alquilada: Jurassic Park

================================================================================
SOLUCIÓN DEL EJERCICIO
================================================================================

EXPLICACIÓN GENERAL:
--------------------
Este programa gestiona alquileres de películas en un videoclub. Utiliza listas
para almacenar la información y funciones modulares para cada tarea específica.

ESTRUCTURA DE DATOS:
-------------------
- Cada alquiler es una lista: [fecha, pelicula, director, cliente, estado]
- lista_alquileres: lista de listas con todos los alquileres
- usuarios_lista: lista de listas [cliente, contador] para contar alquileres
- peliculas_lista: lista de listas [pelicula, contador] para contar películas

TÉCNICAS UTILIZADAS:
-------------------
1. Lectura y escritura de archivos de texto
2. Manejo de excepciones (try-except)
3. Búsqueda secuencial en listas
4. Uso de banderas (funciones booleanas)
5. Ordenamiento burbuja
6. Modularización con funciones auxiliares
"""
CONSIGNAS:

1) Implementar la lectura del archivo alquileres.txt y devolver los registros
   en forma de lista. Si hay error debe crear el archivo con datos de ejemplo.

2) Listar las películas alquiladas en un determinado año y mes, excluyendo
   los alquileres del cliente "gerente".

3) Determinar la cantidad de veces que una película de un director dado fue
   alquilada.

4) Enlistar las películas que no hayan sido devueltas (estado distinto a 
   "devuelto") mostrando cliente y estado.

5) Listar los 3 clientes con más alquileres realizados.

6) (PUNTO OBLIGATORIO) Para cada director crear un archivo con nombre
   informe_[director].txt con la siguiente estructura:
   • Director
   • Total de películas alquiladas
   • Total de películas devueltas
   • Total de películas pendientes
   • Total de películas vencidas
   • Película más alquilada

Ejemplo:
Director: Steven Spielberg
Total de películas alquiladas: 20
Total de películas devueltas: 12
Total de películas pendientes: 5
Total de películas vencidas: 3
Película más alquilada: Jurassic Park

================================================================================
SOLUCIÓN DEL EJERCICIO
================================================================================

EXPLICACIÓN GENERAL:
--------------------
Este programa gestiona alquileres de películas en un videoclub. Utiliza listas
para almacenar la información y funciones modulares para cada tarea específica.

ESTRUCTURA DE DATOS:
-------------------
- Cada alquiler es una lista: [fecha, pelicula, director, cliente, estado]
- lista_alquileres: lista de listas con todos los alquileres
- usuarios_lista: lista de listas [cliente, contador] para contar alquileres
- peliculas_lista: lista de listas [pelicula, contador] para contar películas

TÉCNICAS UTILIZADAS:
-------------------
1. Lectura y escritura de archivos de texto
2. Manejo de excepciones (try-except)
3. Búsqueda secuencial en listas
4. Uso de banderas (funciones booleanas)
5. Ordenamiento burbuja
6. Modularización con funciones auxiliares
"""