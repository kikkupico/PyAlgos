from dictgraph import *
import copy

def floyd_warshall_algo(adjacency_matrix):
    
    g = copy.deepcopy(adjacency_matrix)
    
    n = len(g)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if g[i][j] != 0:
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])
    
    return g
