from limpieza import limpiar_datasets
from construir_grafo import cargar_grafo
from algoritmos import alcance_vehicular

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
# ALCANCE VEHICULAR
# =========================

alcance_vehicular(G, origen)

print("Nodo origen:", origen)