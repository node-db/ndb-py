# coding=utf-8

import types

class NodeTravel():
    '''
    #遍历整个ndb对象, 并针对每一个ndb节点执行action的方法
    '''
    
    def __init__(self):
        pass

    def travel(self, node, action):
        '''
        #遍历节点
        @param node: ndb节点
         
        @return 遍历结果
        '''
        if type(node) == types.ListType:
            for item in node:
                self.travel(item, action)
        elif type(node) == types.DictionaryType:
            for key in node:
                value = node.get(key)
                self.travel(value, action)
            action(node)
        
        return node