import pandas as pd
import networkx as nx

def cargar_grafo():

    # =========================
    # CARGAR CSV LIMPIOS
    # =========================

    nodes = pd.read_csv(
        "data/clean/nodes_clean.csv"
    )

    edges = pd.read_csv(
        "data/clean/edges_clean.csv"
    )

    # =========================
    # CREAR GRAFO
    # =========================

    G = nx.DiGraph()

    # =========================
    # AGREGAR NODOS
    # =========================

    for _, row in nodes.iterrows():

        G.add_node(
            row["node_id"],
            lat=row["lat"],
            lon=row["lon"]
        )

    # =========================
    # AGREGAR ARISTAS
    # =========================

    for _, row in edges.iterrows():

        G.add_edge(
            row["from_id"],
            row["to_id"],
            weight=row["distance_m"],
            maxspeed=row["maxspeed"],
            fclass=row["fclass"]
        )

        # si no es one way
        # agregar regreso
        #si no es oneway   aumento de ida y vuelta... aumento de nodos.... 
        
        if row["oneway"] == 0:

            G.add_edge(
                row["to_id"],
                row["from_id"],
                weight=row["distance_m"],
                maxspeed=row["maxspeed"],
                fclass=row["fclass"]
            )

    print("Grafo construido")
    print("Nodos:", G.number_of_nodes())
    print("Aristas:", G.number_of_edges())

    return G