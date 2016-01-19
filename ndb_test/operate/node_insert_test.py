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
    
    def test_insert_str_val(self):
        result = operate.insert(self.node, 'root->group-1', 'id=7, name=bobo, age=23, sex=male, address=China')
        select_result = operate.select(result, 'root->group-1->name:bobo')
        self.assertEqual(len(select_result), 1)
        self.assertEqual(select_result[0].get('address'), 'China')
    
    def test_insert_map_val(self):
        value = {'id' : '8', 'name' : 'tim', 'sex' : 'male', 'address' : 'Guangzhou'}
        result = operate.insert(self.node, 'root->group-1', value)
        select_result = operate.select(result, 'root->group-1->name:tim')
        self.assertEqual(len(select_result), 1)
        self.assertEqual(select_result[0].get('address'), 'Guangzhou')
    
    def test_insert_none(self):
        result = operate.insert(self.node, 'root->group-1', None)
        select_result = operate.select(result, 'root->group-1')
        self.assertEqual(len(select_result), 5)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()