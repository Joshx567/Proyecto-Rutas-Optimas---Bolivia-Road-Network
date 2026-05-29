from construir_grafo import cargar_grafo
from analisis import analizar_componentes
from algoritmos import alcance_vehicular

G = cargar_grafo()

origen = list(G.nodes())[0]

alcance_vehicular(G, origen)

print("Nodo origen:", origen)
