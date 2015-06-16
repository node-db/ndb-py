# coding=utf-8

import unittest
import ndb

class NodeSelectTest(unittest.TestCase):
    
    '''
    Node Locate Unit Test
    '''
    def test_select(self):
        node = {}
        node['firewall'] = {'state':[
                                    {'id':'1', 'cpu':'80', 'memory':'40', 'state':'startup'},
                                    {'id':'2', 'cpu':'30', 'memory':'20', 'state':'startup'},
                                    {'id':'3', 'cpu':'30', 'memory':'20', 'state':'unknown'},
                                    {'id':'4', 'cpu':'30', 'memory':'20', 'state':'unknown'},
                                    {'id':'5', 'cpu':'50', 'memory':'50', 'state':'startup'},
                                    {'id':'6', 'cpu':'10', 'memory':'50', 'state':'startup'}
                                    ],
                            'state1':[
                                    {'id':'1', 'cpu':'80', 'memory':'40', 'state':'startup'},
                                    {'id':'2', 'cpu':'30', 'memory':'20', 'state':'startup'},
                                    {'id':'3', 'cpu':'70', 'memory':'20', 'state':'unknown'},
                                    {'id':'4', 'cpu':'30', 'memory':'20', 'state':'unknown'}
                                    ]
                           }
        
        result = ndb.select(node, 'firewall->state->cpu:[20,80]')
        self.assertEqual(len(result), 5)
        
        result = ndb.select(node, 'firewall->state->state:/shutdown|startup/')
        self.assertEqual(len(result), 4)
        
        result = ndb.select(node, 'firewall->state->cpu:^3')
        self.assertEqual(len(result), 3)
        
        result = ndb.select(node, 'firewall->state->id:3$')
        self.assertEqual(len(result), 1)
        
        result = ndb.select(node, 'firewall->:/state*/->id:3$')
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
