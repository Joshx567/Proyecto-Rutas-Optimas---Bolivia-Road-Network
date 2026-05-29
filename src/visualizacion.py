import matplotlib.pyplot as plt
import networkx as nx

def dibujar_grafo(G):

    plt.figure(figsize=(10,10))

    nx.draw(G, node_size=1)

    plt.show()