# coding=utf-8

import copy
import unittest
import test_data
from ndb import operate

class NodeUpdateTest(unittest.TestCase):
    
    '''
    Node Delete Unit Test
    '''
    def setUp(self):  
        self.node = copy.deepcopy(test_data.node)
    
    def test_update_str_val(self):
        result = operate.update(self.node, 'root->group-1->name:lily', 'school=Center-School, class=3')
        select_result = operate.select(result, 'root->group-1->name:lily')
        self.assertEqual(len(select_result), 1)
        self.assertEqual(select_result[0].get('school'), 'Center-School')
        self.assertEqual(select_result[0].get('class'), '3')
    
    def test_update_map_val(self):
        value = {'country' : 'US', 'city' : 'New York'}
        result = operate.update(self.node, 'root->group-1->name:john', value)
        select_result = operate.select(result, 'root->group-1->name:john')
        self.assertEqual(len(select_result), 1)
        self.assertEqual(select_result[0].get('country'), 'US')
        self.assertEqual(select_result[0].get('city'), 'New York')
    
    def test_update_none(self):
        result = operate.update(self.node, 'root->group-1', None)
        select_result = operate.select(result, 'root->group-1')
        self.assertEqual(len(select_result), 5)