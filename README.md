# Modelos del Metro de la Ciudad de México con NetworkX

Este repositorio contiene dos programas que representan la red del Metro de la CDMX mediante grafos.

## Archivos

- `linea3_metro.py`: representa la Línea 3, desde Indios Verdes hasta Universidad.
- `red_metro_cdmx.py`: representa las 12 líneas del Metro como una sola red. Las estaciones compartidas se representan como nodos de transbordo.
- `requirements.txt`: bibliotecas necesarias.

## Conceptos utilizados

- **Nodo:** representa una estación.
- **Arista:** representa la conexión entre dos estaciones consecutivas.
- **Grafo no dirigido:** permite representar el recorrido en ambos sentidos.
- **Atributos:** almacenan información adicional de las estaciones y conexiones.
- **Grado:** indica cuántas conexiones directas tiene una estación.

## Ejecución en Google Colab

El proyecto puede ejecutarse directamente desde Google Colab, sin necesidad de instalar Python ni configurar un entorno local.

[**Abrir notebook en Google Colab**](https://colab.research.google.com/drive/1S5vljgVhUu6Wg2yJKitBaVvCpqvCKdmj?usp=sharing)

## Grafo de la Línea 3

![Grafo de la Línea 3](assets/img/linea3.png)

## Red completa del Metro CDMX

![Red completa del Metro CDMX](assets/img/red_metro.png)

Cada programa muestra información del grafo y genera una visualización. Las imágenes se guardan en la misma carpeta donde se ejecuta el programa.

## Nota
Las coordenadas y los colores de la visualización son aproximados y se utilizan para representar gráficamente la distribución de las estaciones. No es un sistema oficial de navegación ni de información en tiempo real.

## Uso de inteligencia artificial
La IA ayudó a organizar y depurar el código, ajustar las coordenadas y los estilos de las gráficas, y revisar posibles inconsistencias en las estructuras de datos.
