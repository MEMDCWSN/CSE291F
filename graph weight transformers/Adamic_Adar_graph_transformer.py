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

#print Nb[4613]

#wG = nx.DiGraph()
wG = nx.Graph()
for (u, v) in dG.edges():
    summ = 0.0
    for w in Nb[u].intersection(Nb[v]):
        summ = summ + 1/math.log(len(Nb[w]))
    wG.add_edge(u, v, weight=summ)
    
#nx.write_weighted_edgelist(wG, "weighted_citation.edgelist")
nx.write_weighted_edgelist(wG, "a_karate.edgelist")
