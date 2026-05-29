import pandas as pd
import networkx as nx

def cargar_grafo():

    nodes = pd.read_csv(
        "data/processed/nodes.csv"
    )

    edges = pd.read_csv(
        "data/processed/edges.csv"
    )

    G = nx.DiGraph()

    for _, row in nodes.iterrows():

        G.add_node(
            row["node_id"],
            lat=row["lat"],
            lon=row["lon"]
        )

    for _, row in edges.iterrows():

        G.add_edge(
            row["from_id"],
            row["to_id"],
            weight=row["distance_m"]
        )

    return G