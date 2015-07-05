# coding=utf-8

import node_locate

class NodeSelect(node_locate.NodeLocate):
    '''
    #节点查询：采用locate中描述的查询表达式
    #表达式格式为：A->B->C:value
    '''
    def __init__(self):
        self.result = []
    
    def select(self, node, path, action):
        self.action = action
        
        super(NodeSelect, self).locate(node, path);
        
        return self.result
    
    def do_action(self, node):
        if self.action != None:
            self.action(node)
        
        if node != None:
            self.result.append(node)
