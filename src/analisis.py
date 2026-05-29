import networkx as nx

def analizar_componentes(G):

    componentes = list(
        nx.weakly_connected_components(G)
    )

    print("Número de islas:", len(componentes))

    gigante = max(componentes, key=len)

    print("Componente gigante:", len(gigante))