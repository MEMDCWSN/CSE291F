import scipy.io
import scipy.sparse
import numpy as np
mat = scipy.io.loadmat('/home/duong/Downloads/Homo_sapiens.mat')
print mat
A = mat['network']
B = A.toarray()
print len(B)
fo = open("ppi.edgelist", "w")
for i in range(len(B)):
    for j in range(len(B[i])):
        if (B[i][j] > 0.0):
            fo.write(str(i) + ' ' + str(j) + '\n')
fo.close()
A = mat['group']
B = A.toarray()
print len(B)
fo = open("group-edges.csv", "w")
for i in range(len(B)):
    for j in range(len(B[i])):
        if (B[i][j] > 0.0):
            fo.write(str(i) + ',' + str(j) + '\n')
fo.close()            
"""
print B

print len(B)
for i in range(len(B)):
    C = list(B[i])
    print C
    print len(C)
"""
