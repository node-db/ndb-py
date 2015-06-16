# coding=utf-8

import unittest
import ndb


class NodeReaderTest(unittest.TestCase):
    '''
    NodeReader Unit Test
    '''

    def test_read(self):
        ndb = ndb.read('../../resource/example_1.txt')
        print ndb
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
