import networkx as nx
import matplotlib

G = nx.DiGraph()
G.add_node(0)
G.add_edges_from([
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (4, 5)
])

nx.draw_networkx(G)
matplotlib.pyplot.show()

nodes = nx.descendants(G, 2)
nodes.add(2)
H = G.subgraph(nodes)
nx.draw_networkx(H)
matplotlib.pyplot.show()
