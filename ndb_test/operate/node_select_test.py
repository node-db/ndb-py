# coding=utf-8

import copy
import unittest
import test_data
from ndb import operate

class NodeSelectTest(unittest.TestCase):
    
    '''
    Node Select Unit Test
    '''
    def setUp(self):  
        self.node = copy.deepcopy(test_data.node)
    
    def test_select(self):
        
        result = operate.select(self.node, 'root->group-1->age:[11,16]')
        self.assertEqual(len(result), 3)
        
        result = operate.select(self.node, 'root->group-1->sex:/male|female/')
        self.assertEqual(len(result), 4)
        
        result = operate.select(self.node, 'root->group-1->age:^1')
        self.assertEqual(len(result), 3)
        
        result = operate.select(self.node, 'root->group-1->age:1$')
        self.assertEqual(len(result), 2)
        
        result = operate.select(self.node, 'root->:/group*/->id:^3')
        self.assertEqual(len(result), 2)
        
        result = operate.select(self.node, 'root->:/group*/->name:^j')
        self.assertEqual(len(result), 4)
        
        result = operate.select(self.node, 'root->:/group*/->sex:male')
        self.assertEqual(len(result), 6)

if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
