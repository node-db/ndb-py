# coding=utf-8


import types

import node_locate

class NodeDelete(node_locate.NodeLocate):
    '''
    #节点删除：从ndb中删除某个指定节点
    #删除时可以指定删除指定的条目或者整块内容删除
    '''
    
    def __init__(self):
        self.columns = []
        self.clear = False
    
    def delete(self, node, path, value, action):
        if value != None:
            if value.startswith('[') and value.endswith(']'):
                self.columns = value[1:len(value) - 1].split(',')
            elif value == 'block':
                self.clear = True
                
        self.action = action
        
        super(NodeDelete, self).locate(node, path);
        
        return node
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        else:
            if node != None and type(node) == types.DictionaryType:
                if self.clear is True:
                    node.clear()
                elif self.columns != None and len(self.columns) > 0:
                    for column in self.columns:
                        column = column.strip()
                        if node.has_key(column):
                            del node[column]
        
