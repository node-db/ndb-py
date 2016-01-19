# coding=utf-8

import copy
import unittest
import test_data
from ndb import operate

class NodeScriptTest(unittest.TestCase):
    
    '''
    Node Delete Unit Test
    '''
    def setUp(self):  
        self.node = copy.deepcopy(test_data.node)
        self.script = [
                       'delete:root->group-2->name:jim !! [sex, age]',
                       'insert:root->group-1 !! name=bill,age=31, sex=male',
                       'update:root->group-1->name:lily !! address=China, age=21'
                       ]
    def test_script(self):
        result = operate.script(self.node, self.script)
        select_result = operate.select(result, 'root->group-1->name:bill')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'bill')
        self.assertEquals(select_result[0].get('sex'), "male")
        self.assertEquals(select_result[0].get('age'), "31")
        
        select_result = operate.select(result, 'root->group-1->name:lily')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'lily')
        self.assertEquals(select_result[0].get('address'), 'China')
        self.assertEquals(select_result[0].get('age'), '21')
        
        select_result = operate.select(result, 'root->:/group*/->name:jim')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'jim')
        self.assertEquals(select_result[0].get('sex'), None)
        self.assertEquals(select_result[0].get('age'), None)
    
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()