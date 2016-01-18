# coding=utf-8

import unittest
import types
import datetime
import test_data
from ndb import operate

class NodeTravelTest(unittest.TestCase):
    
    def test_travel(self):
        def action(node):
            if type(node) == types.DictionaryType:
                if node.has_key('age'):
                    today = datetime.datetime.now()
                    node['birthday'] = str(today.year - int(node.get('age')))
        
        node = test_data.node
        
        result = operate.travel(node, action)
        select_result = operate.select(result, 'root->group-1->birthday:[1991, 1995]')
        self.assertEqual(len(select_result), 2)
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()