# Importing the libs
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd

# Importing test csv file with pd
# dataset = pd.read_csv('TestData.csv')
# Data = dataset.iloc[:, [1,2]].values

# Test-Data
Data = [[1, 2],
 [2, 2],
 [3, 4],
 [2, 3],
 [1, 1],
 [4, 5],
 [5, 6],
 [4, 7],
 [3, 2],
 [6, 3]]


# Creating a scatter plot
x,y = list(zip(*Data))
plt.scatter(x, y)
plt.show()


# Creating a dendrogram
from scipy.spatial.distance import pdist
import scipy.cluster.hierarchy as hier
dendrogram = hier.dendrogram(hier.linkage(Data, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Index')
plt.ylabel('Distance')
plt.show()


# Cutting the dendrogram
distanceMatrix = pdist(Data)
Z = hier.linkage(distanceMatrix, method='complete')

# cut dendrogram at distance = 2
fc = hier.fcluster(Z, 3.5 , criterion='distance')

# print the clusters 
for k in range(1,max(fc)):
    print(np.where(fc == k))


import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.cuts import conductance

# Create a networkx graph object
my_graph = nx.Graph() 
 
# Add edges to to the graph object
# Each tuple represents an edge between two nodes
my_graph.add_edges_from([
                        (1,2), 
                        (1,3), 
                        (3,4), 
                        (1,5), 
                        (3,5),
                        (4,2),
                        (2,3),
                        (3,0)])
 
# Draw the resulting graph
nx.draw(my_graph, with_labels=True, font_weight='bold')

# Modularity
c = list(greedy_modularity_communities(my_graph))

# print sets of nodes, one for each community.
sorted(c[0])

# edge_betweenness_centrality
nx.edge_betweenness_centrality(my_graph)

# Conductance
# S (sequence) – A sequence of nodes in my_graph.
# T (sequence) – A sequence of nodes in my_graph.
S = [0,5]
T = [3,4]
conductance(my_graph, S, T)




