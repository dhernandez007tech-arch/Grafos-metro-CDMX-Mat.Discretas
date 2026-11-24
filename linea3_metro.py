# MODELO DE LA LINEA 3 DEL METRO CDMX CON NETWORKX
# Codigo fuente extraido del notebook Grafos_de_la_linea_del_metro.ipynb
# Dependencias: networkx y matplotlib

import networkx as nx
import matplotlib.pyplot as plt
"""
PASO 1: DATOS
'estaciones' es una LISTA con los nombres en orden de norte a sur.
El orden importa porque más abajo conectamos cada estación con la siguiente.
"""
estaciones = [
    "Indios Verdes",
    "Deportivo 18 de Marzo",
    "Potrero",
    "La Raza",
    "Tlatelolco",
    "Guerrero",
    "Hidalgo",
    "Juárez",
    "Balderas",
    "Niños Héroes",
    "Hospital General",
    "Centro Médico",
    "Etiopía/Plaza de la Transparencia",
    "Eugenia",
    "División del Norte",
    "Zapata",
    "Coyoacán",
    "Viveros/Derechos Humanos",
    "Miguel Ángel de Quevedo",
    "Copilco",
    "Universidad",
]

"""
'transbordos' es un DICCIONARIO:
- La clave es el nombre de la estación.
- El valor es la lista de líneas a las que se puede cambiar ahí.
Las estaciones que no aparecen aquí no tienen transbordo.
"""
transbordos = {
    "Deportivo 18 de Marzo": ["6"],
    "La Raza": ["5"],
    "Guerrero": ["B"],
    "Hidalgo": ["2"],
    "Balderas": ["1"],
    "Centro Médico": ["9"],
    "Zapata": ["12"],
}

"""
'colores_lineas' asocia el identificador de cada línea con su color en
matplotlib para pintar los nodos de transbordo según la línea de conexión.
"""
colores_lineas = {
    "1": "hotpink",
    "2": "royalblue",
    "3": "olivedrab",
    "4": "turquoise",
    "5": "gold",
    "6": "red",
    "7": "darkorange",
    "8": "forestgreen",
    "9": "saddlebrown",
    "A": "purple",
    "B": "gray",
    "12": "goldenrod",
}


"""
PASO 2: CREAR EL GRAFO
1. nx.Graph() crea un grafo NO DIRIGIDO vacío (se puede viajar en ambos
sentidos, como en el metro).
2. 'name' solo le pone un nombre al grafo.
3. La variable G guarda el grafo para usarlo después.
"""
G = nx.Graph(name="Línea 3 del Metro CDMX")

"""
PASO 3: AGREGAR LOS NODOS
- enumerate(estaciones, start=1) devuelve parejas (número, nombre):
  (1, "Indios Verdes"), (2, "Deportivo 18 de Marzo"), ...

- G.add_node(nombre, ...) agrega la estación como nodo. Lo que va
  después del nombre son ATRIBUTOS (datos extra guardados en el nodo):
    linea       -> número de la línea (3)
    orden       -> posición de la estación en la línea
    transbordo  -> lista de líneas con las que conecta

- transbordos.get(nombre, []) busca la estación en el diccionario;
  si no está, devuelve una lista vacía [] (sin transbordo).
"""

for numero, nombre in enumerate(estaciones, start=1):
    G.add_node(
        nombre,
        linea=3,
        orden=numero,
        transbordo=transbordos.get(nombre, []),
    )

"""
PASO 4: AGREGAR LAS ARISTAS
- estaciones[1:] es la misma lista pero sin la primera estación.

- zip(estaciones, estaciones[1:]) forma parejas de estaciones vecinas:
  (Indios Verdes, Deportivo 18 de Marzo), (Deportivo 18 de Marzo, Potrero)...

- G.add_edge(origen, destino, weight=1) conecta las dos estaciones.
  'weight' es el PESO (costo) de la conexión. Usamos 1 = una parada.
"""
for origen, destino in zip(estaciones, estaciones[1:]):
    G.add_edge(origen, destino, weight=1)

"""
PASO 5: CONSULTAR INFORMACIÓN DEL GRAFO
- print(G)                    -> resumen (nombre, nodos y aristas).
- G.number_of_nodes()         -> cuántas estaciones hay (21).
- G.number_of_edges()         -> cuántas conexiones hay (20).
"""
print(G)
print("Número de estaciones:", G.number_of_nodes())
print("Número de conexiones:", G.number_of_edges())

"""
MOSTRAR LAS ESTACIONES CON TRANSBORDO
- G.nodes(data=True) recorre cada nodo junto con su diccionario de
  atributos (aquí llamado 'datos').
- 'if datos["transbordo"]' es verdadero solo si la lista NO está vacía.
- ', '.join(...) une los elementos de la lista con comas para imprimirlos.
"""
print("\nEstaciones con transbordo:")
for nombre, datos in G.nodes(data=True):
    if datos["transbordo"]:
        print(f"  {nombre}: Línea(s) {', '.join(datos['transbordo'])}")


"""
PASO 6: DIBUJAR EL GRAFO
"""
posiciones = {nombre: (0, -i) for i, nombre in enumerate(estaciones)}
"""
- 'posiciones' es un diccionario con las coordenadas (x, y) de cada nodo.
-  Con x = 0 y y = -i las estaciones quedan en una línea vertical, de norte (arriba) a sur (abajo).
"""

# Cada transbordo toma el color de la línea con la que conecta (primer elemento)
colores = [
    #- 'colores' es una lista con un color por nodo: si tiene transbordo
    colores_lineas.get(G.nodes[n]["transbordo"][0], "olivedrab")
    if G.nodes[n]["transbordo"] else "olivedrab"
    for n in G.nodes
]
"""
Toma el color de la primera línea de correspondencia en 'colores_lineas';
si no tiene transbordo, usa 'olivedrab' (color de la Línea 3).
"""

#- plt.figure(figsize=(7, 11)) crea un lienzo alto para que quepa los nombres.
plt.figure(figsize=(7, 11))
nx.draw(
    G,
    posiciones,
    with_labels=True,
    node_color=colores,
    node_size=300,
    font_size=8,
    edge_color="olivedrab",
    width=3,
)
"""
  - nx.draw(...) dibuja el grafo:
    `with_labels=True` -> muestra el nombre de cada estación
    `node_color`       -> color de los nodos
    `node_size`        -> tamaño de los nodos
    `edge_color/width` -> color y grosor de las conexiones
"""
plt.title("Metro CDMX - Línea 3 (transbordos = color de línea)")
plt.savefig("linea3.png", dpi=150, bbox_inches="tight")
plt.show()
