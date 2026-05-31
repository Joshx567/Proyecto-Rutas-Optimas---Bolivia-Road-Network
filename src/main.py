from limpieza import limpiar_datasets
from construir_grafo import cargar_grafo

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

G = cargar_grafo()

# =========================
# NODO ORIGEN
# =========================

origen = list(G.nodes())[0]

# =========================
# ALCANCE VEHICULAR (5 KM)
# =========================

alcance_vehicular(G, origen)

print("Nodo origen:", origen)

# =========================
# ISLAS VIALES (Debilmente conectadas y la red conectada mas grande..) / (2241.58 km) Pando → Tarija
# =========================

gigante = analizar_componentes(G)

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

comparar_distancia_tiempo(
    SG,
    origen_d,
    destino_d
)
