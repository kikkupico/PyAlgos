import unittest
import random
import string
from dictgraph import *
from floyd_warshall_algo import *

class TestFloydWarshallAlgo(unittest.TestCase):
    def setUp(self):
        pass
    
    def helper_generate_random_graph(self, max_nodes, max_links):
        d = {}
        for i in range(0, max_nodes):
            d[string.ascii_lowercase[i]] = []
        
        for item in d:
            d[item] = random.sample(d.keys(), random.randint(0,max_links))
            
        g = DictGraph()
        g.create_from_dict(d)
        
        print(g)
        return g
    
    def test_floyd_warshall_algo(self):
        g = self.helper_generate_random_graph(5,2)
        adj = g.get_adjacency_matrix()
        print(str(adj).replace('inf','-'))
        print(str(floyd_warshall_algo(adj)).replace('inf','-'))
    

if __name__ == '__main__':
    unittest.main(verbosity=3)
