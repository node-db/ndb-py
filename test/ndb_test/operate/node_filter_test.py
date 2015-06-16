# coding=utf-8

import unittest
import ndb


class ListFilterTest(unittest.TestCase):
    '''
    ListFilter单元测试
    '''

    def test_filter(self):
        _list = [
                {'id':'1', 'name':'huihui', 'type':'h'},
                {'id':'2', 'name':'zhuzhu', 'type':'m'},
                {'id':'3', 'name':'zhutou', 'type':'h'},
                {'id':'4', 'name':'zhutou', 'type':'h'},
                ]
        
        _list = ndb.filter_list(_list, query={'name':{'type':'like', 'value':'zhu'}, 'type':{'type':'eq', 'value':'h'}})
        print _list
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
