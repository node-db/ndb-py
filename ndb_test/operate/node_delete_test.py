# coding=utf-8

import copy
import unittest
import test_data
from ndb import operate

class NodeDeleteTest(unittest.TestCase):
    
    '''
    Node Delete Unit Test
    '''
    def setUp(self):  
        self.node = copy.deepcopy(test_data.node)
    
    def test_delete_block(self):
        result = operate.delete(self.node, 'root->group-1->age:[11,16]', 'block')
        select_result = operate.select(result, 'root->group-1')
        select_result = operate.clean(select_result)
        self.assertEqual(len(select_result), 2)
    
    def test_delete_column(self):   
        result = operate.delete(self.node, 'root->group-1->age:[11,16]', '[name, sex]')
        select_result = operate.select(result, 'root->group-1->age:[11,16]')
        self.assertEqual(len(select_result), 3)
        for row in select_result:
            self.assertEqual(len(row), 2)

if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()