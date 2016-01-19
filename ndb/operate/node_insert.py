# coding=utf-8


import types

import node_clean
import node_locate

class NodeInsert(node_locate.NodeLocate):
    '''
    #节点插入：向ndb中插入数据
    #当遇到路径中没有的节点时，主动建立路径节点，并在末尾节点插入数据
    '''
    def __init__(self):
        self.insert_value = None
    
    def insert(self, node, path, value, action):
        if type(value) == types.StringType or type(value) == types.UnicodeType:
            self.insert_value = super(NodeInsert, self)._convert_value_map(value)
        elif type(value) == types.DictionaryType:
            self.insert_value = value
        
        self.action = action
        
        super(NodeInsert, self).locate(node, path, True);
        
        return node_clean.NodeClean().clean(node)
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        else:
            if node != None and type(node) == types.DictionaryType and self.insert_value != None:
                for key in self.insert_value:
                    node[key] = self.insert_value.get(key)
                                
                
        
