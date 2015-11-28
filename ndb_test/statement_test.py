# coding=utf-8

import os

import unittest
import ndb

class StatementTest(unittest.TestCase):
    '''
    node database statement unit test
    '''
    def setUp(self):  
        self.node = ndb.read('example.ndb')
    
    def test_exits(self):
        '''exits test'''
        result = ndb.execute(self.node, 'exist:root->parent->child->name:jim')
        self.assertEqual(result, True)
        
        result = ndb.execute(self.node, 'exist:root->parent->child->sex:male && name:m$')
        self.assertEqual(result, True)
        
        result = ndb.execute(self.node, 'exist:root->parent->child->sex:female && name:m$')
        self.assertEqual(result, False)
    
    def test_one(self):
        '''one test'''
        result = ndb.execute(self.node, 'one:root->parent->child->sex:male')
        self.assertEqual(result.get('name'), 'jim')
        self.assertEqual(result.get('age'), '20')
    
    def test_select(self):
        '''select test'''
        result = ndb.execute(self.node, 'select:root->parent->child->name:/.*m/')
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0].get('name'), 'jim')
        self.assertEquals(result[1].get('name'), 'tom')

        result = ndb.execute(self.node, 'select:root->parent->child->age:[15,25]')
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0].get('name'), 'jim')
        self.assertEquals(result[1].get('name'), 'lily')
        
        result = ndb.execute(self.node, 'select:root->parent->child->sex:^fe')
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].get('name'), 'lily')
        
        result = ndb.execute(self.node, 'select:root->parent->child->name:m$')
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0].get('name'), 'jim')
        self.assertEquals(result[1].get('name'), 'tom')
        
        result = ndb.execute(self.node, 'select:root->parent->child->sex:male && age:[15,25]')
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].get('name'), 'jim')
        
        result = ndb.execute(self.node, 'select:root->parent->child')
        self.assertEquals(len(result), 3)
        self.assertEquals(result[0].get('name'), 'jim')
        self.assertEquals(result[1].get('name'), 'lily')
        self.assertEquals(result[2].get('name'), 'tom')

        result = ndb.execute(self.node, 'select:root->parent->:/child|nephew/->sex:female')
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0].get('name'), 'lucy')
        self.assertEquals(result[1].get('name'), 'lily')

    def test_update(self):
        ''''update test'''
        result = ndb.execute(self.node, 'update:root->parent->child->name:jim !! age=21, address=China')
        result = ndb.execute(result, 'select:root->parent->child->name:jim')
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].get('age'), '21')
        self.assertEquals(result[0].get('address'), 'China')

        
    def test_delete(self):
        '''delete test'''
        result = ndb.execute(self.node, 'delete:root->parent->child->name:jim !! [sex, age]')
        result = ndb.execute( result, 'select:root->parent->child->name:jim')
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].get('name'), 'jim')
        self.assertEquals(result[0].get('sex'), None)
        self.assertEquals(result[0].get('age'), None)

        result = ndb.execute(self.node, 'delete:root->parent->child->name:jim !! block')
        result = ndb.execute(result, 'select:root->parent->child->name:jim')
        self.assertEquals(len(result), 0);
    
    def test_insert(self):
        '''insert test'''
        result = ndb.execute(self.node, 'insert:root->parent->child !! name=bill, sex=male, age=31')
        select_result = ndb.execute(result, 'select:root->parent->child->name:bill')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('sex'), 'male')
        self.assertEquals(select_result[0].get('age'), '31')
        
    
    def test_redirect(self):
        '''redirect test'''
        ndb.execute(self.node, 'select:root->parent->:/child|nephew/->sex:female >> select.ndb')
        node = ndb.read('select.ndb')
        select_result = ndb.execute(node, 'select:result->sex:female')
        self.assertEquals(len(select_result), 2)
        self.assertEquals(select_result[0].get('name'), 'lucy')
        self.assertEquals(select_result[1].get('name'), 'lily')
        
        ndb.execute(self.node, 'insert:root->parent->child !! name=bill, sex=male, age=31 >> insert.ndb')
        node = ndb.read('insert.ndb')
        select_result = ndb.execute(node, 'select:root->parent->child->name:bill')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'bill')
        self.assertEquals(select_result[0].get('sex'), "male")
        self.assertEquals(select_result[0].get('age'), "31")
            
        ndb.execute(self.node, 'update:root->parent->child->name:jim !! age=21, address=China >> update.ndb')
        node = ndb.read('update.ndb')
        select_result = ndb.execute(node, 'select:root->parent->child->name:jim')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'jim')
        self.assertEquals(select_result[0].get('address'), "China")
        self.assertEquals(select_result[0].get('age'), "21")
        
        # delete temp file
        files = ['select.ndb', 'insert.ndb', 'update.ndb']
        for filename in files:
            os.remove(filename)
    
    def test_script(self):
        '''script test'''
        result = ndb.execute(self.node, "script:example.script")
        
        select_result = ndb.execute(result, 'select:root->parent->child->name:bill')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'bill')
        self.assertEquals(select_result[0].get('sex'), "male")
        self.assertEquals(select_result[0].get('age'), "31")
        
        select_result = ndb.execute(result, 'select:root->parent->child->name:lily')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'lily')
        self.assertEquals(select_result[0].get('address'), 'China')
        self.assertEquals(select_result[0].get('age'), '21')
        
        select_result = ndb.execute(result, 'select:root->parent->child->name:jim')
        self.assertEquals(len(select_result), 1)
        self.assertEquals(select_result[0].get('name'), 'jim')
        self.assertEquals(select_result[0].get('sex'), None)
        self.assertEquals(select_result[0].get('age'), None)

if __name__ == '__main__':
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
