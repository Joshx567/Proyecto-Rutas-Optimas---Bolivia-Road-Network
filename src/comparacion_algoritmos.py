import networkx as nx
import time

def comparar_dijkstra_bellmanford(G, origen, destino):

    print("\n===== DIJKSTRA VS BELLMAN-FORD =====")

    # DIJKSTRA
    inicio = time.time()

    distancia_d = nx.dijkstra_path_length(
        G,
        origen,
        destino,
        weight="weight"
    )

    fin = time.time()

    tiempo_d = fin - inicio

    # BELLMAN FORD
    inicio = time.time()

    distancia_b = nx.bellman_ford_path_length(
        G,
        origen,
        destino,
        weight="weight"
    )

    fin = time.time()

    tiempo_b = fin - inicio

    print(
        f"Dijkstra: {round(distancia_d/1000,2)} km"
    )

    print(
        f"Tiempo Dijkstra: {round(tiempo_d,4)} s"
    )

    print()

    print(
        f"Bellman-Ford: {round(distancia_b/1000,2)} km"
    )

    print(
        f"Tiempo Bellman-Ford: {round(tiempo_b,4)} s"
    )

    mejora = tiempo_b / tiempo_d

    print(
        f"Dijkstra fue {round(mejora,2)} veces más rápido"
    )