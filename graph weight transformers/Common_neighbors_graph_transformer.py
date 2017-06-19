import networkx as nx
from sets import Set
import math
#eps = 0.0000001
DEPTH = 1
# NOTE THIS VERSION IS FOR UNDIRECTED GRAPHS

#dG = nx.read_edgelist("citation.edgelist", create_using=nx.DiGraph(), nodetype=int)
dG = nx.read_edgelist("karate.edgelist", create_using=nx.Graph(), nodetype=int)
G = dG.to_undirected()
print G.edges()[:100]
Nb = {}
for u in G.nodes():
    #print u
    Nb[u] = Set(nx.neighbors(G, u))

#print Nb[4613]

#wG = nx.DiGraph()
wG = nx.Graph()
for (u, v) in dG.edges():
    com_neigh = len(Nb[u].intersection(Nb[v]))
    wG.add_edge(u, v, weight=com_neigh+1)
    
#nx.write_weighted_edgelist(wG, "weighted_citation.edgelist")
nx.write_weighted_edgelist(wG, "c_karate.edgelist")
