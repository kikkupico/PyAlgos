import unittest
import random
from merge_sort import *

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_combine_sorted(self):
        l1 = [1,2,5,6]
        l1.sort()
        l2 = [3,4,7,8]
        l2.sort()
        l = l1 + l2
        l.sort()
        self.assertEqual(combine_sorted(l1,l2), l)
    
    def test_merge_sort_odd_length(self):
        unsortedlist = [3,5,65,62,2,6,5,7,100]
        sortedlist = unsortedlist[:] # [:] creates copy of list
        sortedlist.sort()
        self.assertEqual(merge_sort(unsortedlist), sortedlist)
        
    def test_merge_sort_even_length(self):
        unsortedlist = [3,5,65,62,2,6,5,7]
        sortedlist = unsortedlist[:] # [:] creates copy of list
        sortedlist.sort()
        self.assertEqual(merge_sort(unsortedlist), sortedlist)
    
    def test_merge_sort_random(self):
        unsortedlist = [int(1000*random.random()) for i in range(100)]
        sortedlist = unsortedlist[:] # [:] creates copy of list
        sortedlist.sort()
        self.assertEqual(merge_sort(unsortedlist), sortedlist)

if __name__ == '__main__':
    unittest.main(verbosity=3)
