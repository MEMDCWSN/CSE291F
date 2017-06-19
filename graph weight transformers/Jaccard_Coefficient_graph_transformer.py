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
    neighb_hood = nx.single_source_shortest_path_length(G, u, cutoff=DEPTH)
    temp = []
    for v in neighb_hood.keys():
        temp.append(v)
    Nb[u] = Set(temp)

#print Nb[9306117]

#wG = nx.DiGraph()
wG = nx.Graph()
for (u, v) in dG.edges():
    A = len(Nb[u].intersection(Nb[v]))
    B = len(Nb[u].union(Nb[v]))
    #wG.add_edge(u, v, weight=1/(-math.log(float(A)/B, 2)+eps))
    wG.add_edge(u, v, weight=float(A)/B)
    
#nx.write_weighted_edgelist(wG, "weighted_citation.edgelist")
nx.write_weighted_edgelist(wG, "j_karate.edgelist")
