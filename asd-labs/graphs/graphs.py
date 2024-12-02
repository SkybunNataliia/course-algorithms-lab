import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random
import networkx as nx
from collections import deque

# Some constants
L_VISITED = 'visited'
L_VISIT_ORDER = 'visit_order'
L_ROOT = 'root'
L_COLOR = 'color'
L_PARENT = 'parent'
L_DIST = 'distance'

def char_range(start='a', end='z'):
    return map(chr,list(range(ord(start),ord(end)+1)))

def plot_basic_graph(G, pos = None, layout = nx.random_layout, seed = None):
    # Define positions for nodes
    if pos is None:
        pos = layout(G, seed = seed)
    # Create matplotlib figure
    fig, ax = plt.subplots(1, 1, figsize=(8,5))
    # Draw nodes and edges
    node_colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw(G, pos, ax = ax, with_labels=True, node_color=node_colors, edgecolors='#000', 
            linewidths=1, font_size=16, font_weight='bold', node_size=600)
    # Draw labels nearby nodes
    for n in G.nodes:
        x, y = pos[n]
        ax.text(x-0.2, y-0.1, f"{G.nodes[n]['label']}",ha='right', va='bottom', color='#00f', fontsize=14)
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # Show figure
    fig.set_facecolor("#ededed")
    plt.show()

# visita in ampiezza
def bfv(g, root, f):
    for n in g.nodes:
        g.nodes[n][L_VISITED] = False

    queue = deque([root])
    g.nodes[root][L_VISITED] = True
    
    while queue:
        current = queue.popleft()
        f(current)
        for neighbor in g.neighbors(current):
            if not g.nodes[neighbor][L_VISITED]:
                g.nodes[neighbor][L_VISITED] = True
                queue.append(neighbor)

# visita in profondità
def dfv(g, root, f):
    for n in g.nodes:
        g.nodes[n][L_VISITED] = False
    
    # Funzione ricorsiva per visitare i nodi
    def dfs_visit(node):
        g.nodes[node][L_VISITED] = True
        f(node)
        for neighbor in g.neighbors(node):
            if not g.nodes[neighbor][L_VISITED]:
                dfs_visit(neighbor)
    
    dfs_visit(root)

# annotazione grafo per cammini di costo minimo da un nodo sorgente
# The function should annotate the nodes with their parent and distance from source
def dijkstra(g, src):
    for n in g.nodes:
        g.nodes[n][L_VISITED] = False
        g.nodes[n][L_DIST] = float("inf")
        g.nodes[n][L_PARENT] = ''
    g.nodes[src][L_DIST] = 0
    
    unvisited_nodes = list(g.nodes)
    
    while unvisited_nodes:
        min_node = min(unvisited_nodes, key=lambda node: g.nodes[node][L_DIST])
        
        current_node = min_node
        current_dist = g.nodes[current_node][L_DIST]

        if current_dist == float("inf"):
            break
        
        unvisited_nodes.remove(current_node)
        
        for neighbor in g.neighbors(current_node):
            weight = g[current_node][neighbor]['weight']
            new_dist = current_dist + weight
            
            if new_dist < g.nodes[neighbor][L_DIST]:
                g.nodes[neighbor][L_DIST] = new_dist
                g.nodes[neighbor][L_PARENT] = current_node

# produzione del cammino di costo minimo da un grafo annotato con Dijkstra
def shortest_path(g, src, dest):
    path = []
    current_node = dest
    
    if g.nodes[dest][L_DIST] == float("inf"):
        return path

    while current_node is not None:
        path.append(current_node)
        parent = g.nodes[current_node][L_PARENT]
        current_node = parent if parent != '' else None

    path.reverse()
    return path

if __name__ == "__main__":
    g = nx.Graph()
    default_node_attributes = {'visited': False, 'parent': None, 'distance': float("inf"), 'label': '', 'color': '#ededed'}
    g.add_nodes_from(char_range('A','F'), **default_node_attributes)
    g.add_weighted_edges_from([('A','B',1), ('A','F',3), ('B','C',3), ('B','E',5), ('B','F',1), 
                            ('C','D',2), ('D','E',1), ('D','F',6), ('E','F',2)], )
    pos = { 'A': (0,0.5), 'B': (1,1), 'C': (2,1), 'D':(3,0.5), 'E':(2,0), 'F':(1,0) }

    print("*** BFV")
    bfv(g, 'A', print) # expected print order: ABFCED
    print("\n*** DFV")
    dfv(g, 'A', print) # expected print order: ABCDEF
    print("\n*** Dijkstra")
    dijkstra(g, 'A') # should annotate the nodes in the graph
    print(['A', 'B', 'F', 'E', 'D'] == shortest_path(g, 'A', 'D')) # should be True

    plot_basic_graph(g, pos)