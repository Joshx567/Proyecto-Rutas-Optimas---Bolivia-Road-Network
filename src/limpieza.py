import pandas as pd

#Problema	                    Solución
#velocidades faltantes	  imputación por tipo de vía
#distancias inválidas	        eliminación
#nodos inexistentes	            validación
#duplicados	                    eliminación


def limpiar_datasets():

    print("Cargando datasets...")

    nodes = pd.read_csv(
        "data/processed/nodes.csv"
    )

    edges = pd.read_csv(
        "data/processed/edges.csv"
    )

    print("Nodes originales:", len(nodes))
    print("Edges originales:", len(edges))

    # =========================
    # LIMPIAR NODES
    # =========================

    nodes = nodes.dropna()

    nodes = nodes.drop_duplicates(
        subset=["node_id"]
    )

    # =========================
    # LIMPIAR EDGES
    # =========================

    edges = edges.dropna(
        subset=["from_id", "to_id", "distance_m"]
    )

    # eliminar distancias inválidas
    edges = edges[
        edges["distance_m"] > 0
    ]

    # eliminar duplicados
    edges = edges.drop_duplicates()

    # =========================
    # CORREGIR MAXSPEED
    # =========================

    velocidades = {
        "motorway": 80,
        "trunk": 70,
        "primary": 60,
        "secondary": 50,
        "tertiary": 40,
        "residential": 30,
        "service": 20,
        "footway": 5,
        "path": 5,
        "steps": 3
    }

    def corregir_velocidad(row):

        v = row["maxspeed"]

        if pd.isna(v) or v == 0:

            return velocidades.get(
                row["fclass"],
                30
            )

        return v

    edges["maxspeed"] = edges.apply(
        corregir_velocidad,
        axis=1
    )

    # =========================
    # VALIDAR NODOS EXISTENTES
    # =========================

    nodos_validos = set(
        nodes["node_id"]
    )

    edges = edges[
        edges["from_id"].isin(nodos_validos)
    ]

    edges = edges[
        edges["to_id"].isin(nodos_validos)
    ]

    # =========================
    # GUARDAR
    # =========================

    nodes.to_csv(
        "data/clean/nodes_clean.csv",
        index=False
    )

    edges.to_csv(
        "data/clean/edges_clean.csv",
        index=False
    )

    print("Limpieza completada")
    print("Nodes finales:", len(nodes))
    print("Edges finales:", len(edges))