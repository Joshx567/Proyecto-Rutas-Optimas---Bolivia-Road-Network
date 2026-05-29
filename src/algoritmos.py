import networkx as nx

#Alcance vehicular

def alcance_vehicular(G, origen, max_dist=5000):

    distancias = nx.single_source_dijkstra_path_length(
        G,
        origen,
        cutoff=max_dist,
        weight="weight"
    )

    cantidad = len(distancias)

    print(f"Nodos alcanzables: {cantidad}")

    return distancias

def ejecutar_dijkstra(G, origen, destino):

    ruta = nx.dijkstra_path(
        G,
        origen,
        destino,
        weight="weight"
    )

    distancia = nx.dijkstra_path_length(
        G,
        origen,
        destino,
        weight="weight"
    )

    return ruta, distancia