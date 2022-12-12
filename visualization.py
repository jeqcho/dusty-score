import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv('adjacency_matrix.csv', header=None)
G = nx.from_pandas_adjacency(df)
print(G.nodes)
with open('dusty_score.txt', 'r') as f:
    node_intensity = f.readlines()

node_intensity = [int(x.strip()) for x in node_intensity]
shells = [[], [], [], [],[]]
for i in range(len(node_intensity)):
    shells[node_intensity[i]].append(i)
# nx.draw(G, node_size=1,width=.1)
# plt.show()
# nx.draw(G, pos=nx.shell_layout(G, shells), node_size=1, width=.01, node_color=node_intensity, vmin=0, vmax=4,
#         cmap='viridis')
nx.draw(G, pos=nx.kamada_kawai_layout(G), node_size=1, width=.01, node_color=node_intensity, vmin=0, vmax=4,
        cmap='viridis')
plt.show()
# nx.draw_kamada_kawai(G)
# plt.show()
# layouts = [x for x in nx.__dir__() if x.endswith('_layout')]
# for layout in layouts:
#     nx.draw(G, pos=nx[layout](G))
