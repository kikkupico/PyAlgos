import unittest
import random
import string
from dictgraph import *
import math

class TestDictGraph(unittest.TestCase):
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
        return g
        
    def test_random_create(self):
        g = self.helper_generate_random_graph(5,3)
        print(g)
    
    def test_random_dfs(self):
        g = self.helper_generate_random_graph(6,4)
        self.helper_traversal_test(g, "a", "Depth First")
    
    def test_simple_create(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["c"],"c":[]})
        print(g)
    
    def test_link_without_node_def(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["c"]})
        print(g)
    
    def helper_traversal_test(self, g, start, how):
        print(g)
        order = []
        visited = {}
        
        if how == "Depth First" :
            g.depth_first_traverse(start, order)
        elif how == "Breadth First":
            g.breadth_first_traverse(start, order)
        else:
            print("Unsupported traversal method")
            raise NotImplemented
            
        print(order)
        
        #check for presence of all nodes
        for node in g.nodes:
           self.assertTrue(node in order)
        
        #check for presence of duplicates
        uniques = set(order)
        self.assertEqual(len(order),len(uniques))
        
    
    def test_depth_first_traverse_simple(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["d"],"c":["e"]})
        self.helper_traversal_test(g, "a", "Depth First")
    
    def test_depth_first_traverse_looped(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["d"],"c":["b"]})
        self.helper_traversal_test(g, "a", "Depth First")
        
    def test_breadth_first_traverse_simple(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["d"],"c":["e"]})
        self.helper_traversal_test(g, "a", "Breadth First")
    
    def test_breadth_first_traverse_looped(self):
        g = DictGraph()
        g.create_from_dict({"a":["b","c"],"b":["d"],"c":["b"]})
        self.helper_traversal_test(g, "a", "Breadth First")

    
if __name__ == '__main__':
    unittest.main(verbosity=3)
