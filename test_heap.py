import unittest
import random
from heap import *

class TestHeap(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_max_heap_create_simple(self):
        l = [35,33,42,10,14,19,27,44,26,31]
        h = Heap("max")
        h.create_from_list(l)
        print(h)

if __name__ == '__main__':
    unittest.main(verbosity=3)
