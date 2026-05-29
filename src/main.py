from limpieza import limpiar_datasets
from construir_grafo import cargar_grafo
from algoritmos import alcance_vehicular
from analisis import analizar_componentes 
from analisis import diametro_aproximado
from analisis import mst_emergencia

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

# =========================
# ISLAS VIALES
# =========================

gigante = analizar_componentes(G)

# =========================
# Diámetro vial
# =========================

diametro_aproximado(G)

# =========================
# Red de emergencia mínima (MST)
# =========================

mst_emergencia(G)

# BONUS: Ruta por tipo de horario. 

