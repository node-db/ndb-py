# coding=utf-8

import unittest
import ndb


class NodeReaderTest(unittest.TestCase):
    '''
    NodeReader Unit Test
    '''

    def test_read(self):
        data = ndb.read('../example.ndb')
        self.assertIsNotNone(data.get('root'))
        
if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
