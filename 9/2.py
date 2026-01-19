import networkx as nx
import nx_altair as nxa

G = nx.Graph()
G.add_nodes_from([(x, {"name": x}) for x in "A;B;C;D;E".split(";")])
G.add_edges_from([(x[0], x[1]) for x in "AB;AC;BC;BD;CE;DE".split(";")])

nxa.draw_networkx(G, node_label="name").save("nxa.pdf")