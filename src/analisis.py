import networkx as nx
import networkx as nx
import random
import time

#Islas viales

def analizar_componentes(G):

    componentes = list(
        nx.weakly_connected_components(G)
    )

    num_componentes = len(componentes)

    gigante = max(componentes, key=len)

    print("Número de componentes:", num_componentes)

    print(
        "Tamaño componente gigante:",
        len(gigante)
    )

    return gigante

#Diámetro vial

def diametro_aproximado(G, muestra=1000):

    print("Calculando diámetro aproximado...")

    inicio = time.time()

    nodos = list(G.nodes())

    # tomar muestra aleatoria
    muestra_nodos = random.sample(
        nodos,
        min(muestra, len(nodos))
    )

    max_distancia = 0

    nodo_origen = None
    nodo_destino = None

    for origen in muestra_nodos:

        try:

            distancias = nx.single_source_dijkstra_path_length(
                G,
                origen,
                weight="weight"
            )

            destino = max(
                distancias,
                key=distancias.get
            )

            distancia = distancias[destino]

            if distancia > max_distancia:

                max_distancia = distancia
                nodo_origen = origen
                nodo_destino = destino

        except:

            pass

    fin = time.time()

    print("Diámetro aproximado:", round(max_distancia, 2), "m")

    print(
        "Entre nodos:",
        nodo_origen,
        "->",
        nodo_destino
    )

    print(
        "Tiempo:",
        round(fin - inicio, 2),
        "segundos"
    )

    return (
        nodo_origen,
        nodo_destino,
        max_distancia
    )

#MST

def mst_emergencia(G):

    print("Calculando MST...")

    inicio = time.time()

    # convertir a no dirigido
    UG = G.to_undirected()

    # componente gigante
    gigante = max(
        nx.connected_components(UG),
        key=len
    )

    SG = UG.subgraph(gigante).copy()

    # MST
    mst = nx.minimum_spanning_tree(
        SG,
        weight="weight"
    )

    # distancia total
    distancia_total = sum(
        data["weight"]
        for _, _, data in mst.edges(data=True)
    )

    fin = time.time()

    print(
        "Nodos MST:",
        mst.number_of_nodes()
    )

    print(
        "Aristas MST:",
        mst.number_of_edges()
    )

    print(
        "Distancia total:",
        round(distancia_total / 1000, 2),
        "km"
    )

    print(
        "Tiempo:",
        round(fin - inicio, 2),
        "segundos"
    )

    return mst

