#Universidad del Valle de Guatemala
#Diseño de Lenguajes de Programación - Sección: 10
#Mario Antonio Guerra Morales - Carné: 21008
#Analizador Léxico por medio de lectura de un archivo .yal (YALex)

#Importación de módulos y librerías para mostrar gráficamente los autómatas finitos.
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from collections import deque
from collections import defaultdict
import sys

def leer_archivo_yal(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

nombre_archivo = 'slr-1.yal'  # Reemplaza 'archivo.yal' con el nombre de tu archivo .yal
contenido_archivo = leer_archivo_yal(nombre_archivo)
print(contenido_archivo)