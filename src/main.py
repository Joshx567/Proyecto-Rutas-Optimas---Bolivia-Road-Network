import time
from limpieza import limpiar_datasets
from construir_grafo import cargar_grafo
from comparacion_algoritmos import comparar_dijkstra_bellmanford
from algoritmos import alcance_vehicular

from analisis import (
    analizar_componentes,
    diametro_aproximado,
    mst_emergencia,
    comparar_distancia_tiempo
)

# =========================
# LIMPIEZA
# =========================

#limpiar_datasets()

# =========================
# CONSTRUIR GRAFO
# =========================

inicio = time.time()

G = cargar_grafo()

fin = time.time()

print(
    "Tiempo construcción grafo:",
    round(fin - inicio, 2),
    "segundos"
)

# =========================
# NODO ORIGEN
# =========================

origen = list(G.nodes())[0]

# =========================
# ALCANCE VEHICULAR (5 KM)
# =========================

inicio = time.time()

alcance_vehicular(G, origen)

fin = time.time()

print("Nodo origen:", origen)

print(
    "Tiempo alcance vehicular:",
    round(fin - inicio, 2),
    "segundos"
)

# =========================
# ISLAS VIALES (Debilmente conectadas y la red conectada mas grande..) / (2241.58 km) Pando → Tarija
# =========================

inicio = time.time()

gigante = analizar_componentes(G)

fin = time.time()

print(
    "Tiempo análisis componentes:",
    round(fin - inicio, 2),
    "segundos"
)

# componente gigante
SG = G.subgraph(gigante).copy()

# ========================= 
# Diámetro vial (Muestra de 1000)
# =========================

origen_d, destino_d, diametro = diametro_aproximado(SG)

# =========================
# Red de emergencia mínima (MST) (Toda la red conectada)
# =========================

mst_emergencia(SG)

# BONUS: Ruta por tipo de horario. 

inicio = time.time()

comparar_distancia_tiempo(
    SG,
    origen_d,
    destino_d
)

fin = time.time()

print(
    "Tiempo bonus:",
    round(fin - inicio, 2),
    "segundos"
)

#BELLMAN-FORD VS DIJKSTRA

comparar_dijkstra_bellmanford(
    SG,
    origen_d,
    destino_d
)
