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

    print("Diámetro aproximado:", round(max_distancia/1000, 2), "Km")

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

def comparar_distancia_tiempo(G, origen, destino):

    print("\n===== BONUS =====")

    try:

        # Ruta optimizada por distancia
        ruta_d = nx.shortest_path(
            G,
            origen,
            destino,
            weight="weight"
        )

        distancia_d = nx.shortest_path_length(
            G,
            origen,
            destino,
            weight="weight"
        )

        tiempo_d = 0

        for u, v in zip(ruta_d[:-1], ruta_d[1:]):
            tiempo_d += G[u][v]["time"]

        # Ruta optimizada por tiempo
        ruta_t = nx.shortest_path(
            G,
            origen,
            destino,
            weight="time"
        )

        tiempo_t = nx.shortest_path_length(
            G,
            origen,
            destino,
            weight="time"
        )

        distancia_t = 0

        for u, v in zip(ruta_t[:-1], ruta_t[1:]):
            distancia_t += G[u][v]["weight"]

        print("\nRuta optimizada por DISTANCIA")
        print(
            f"Distancia: {round(distancia_d/1000,2)} km"
        )
        print(
            f"Tiempo: {round(tiempo_d/60,2)} min"
        )
        print(
            f"Nodos: {len(ruta_d)}"
        )

        print("\nRuta optimizada por TIEMPO")
        print(
            f"Distancia: {round(distancia_t/1000,2)} km"
        )
        print(
            f"Tiempo: {round(tiempo_t/60,2)} min"
        )
        print(
            f"Nodos: {len(ruta_t)}"
        )

    except nx.NetworkXNoPath:

        print(
            "No existe ruta entre los nodos seleccionados"
        )