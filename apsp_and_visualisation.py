import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def booleanize(a):
    if a > 0:
        return 1
    return 0


df = pd.read_csv('membership.csv')
matrix = df.drop(['index'], axis=1).to_numpy()
adj_matrix = np.matmul(matrix, np.transpose(matrix))
adj_matrix = np.vectorize(booleanize)(adj_matrix)
np.fill_diagonal(adj_matrix, 0)
pd.DataFrame(adj_matrix).to_csv('adjacency_matrix.csv', index=False, header=False)
G = nx.from_numpy_matrix(adj_matrix)
print(len(list(nx.connected_components(G))))
degrees = sorted(d for n, d in G.degree())
with open('degrees.txt', 'w') as f:
    f.write('\n'.join([str(deg) for deg in degrees]))
sp = dict(nx.all_pairs_shortest_path_length(G))
pd.DataFrame(sp).to_csv('distance_matrix.csv')
dusty_scores = dict(sorted(sp[len(df) - 1].items())).values()
random_student_scores = dict(sorted(sp[63].items())).values()
with open('dusty_score.txt', 'w') as f:
    f.write('\n'.join([str(dusty_score) for dusty_score in dusty_scores]))
with open('random_student_score.txt', 'w') as f:
    f.write('\n'.join([str(student_score) for student_score in random_student_scores]))