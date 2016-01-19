# coding=utf-8

import types

import node_clean
import node_locate

class NodeUpdate(node_locate.NodeLocate):
    '''
    #节点修改：修改ndb中的数据
    #查询条件使用ndb路径查询，并更新查询路径上的数据
    '''    
    def __init__(self):
        self.update_value = None
    
    def update(self, node, path, value, action):
        if type(value) == types.StringType or type(value) == types.UnicodeType:
            self.update_value = super(NodeUpdate, self)._convert_value_map(value)
        elif type(value) == types.DictionaryType:
            self.update_value = value
            
        self.action = action
        
        super(NodeUpdate, self).locate(node, path);
        
        return node_clean.NodeClean().clean(node)
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        else:
            if self.update_value != None and type(node) == types.DictionaryType and self.update_value != None:
                for key in self.update_value:
                    node[key] = self.update_value.get(key)
        
