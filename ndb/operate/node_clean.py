# coding=utf-8

import types

class NodeClean():
    '''
    #节点清理, 当Dictionary节点中没有数据的时候删除节点
    '''
    def __init__(self):
        pass
    
    def clean(self, node):
        '''
        #清理节点
        @param node: ndb节点
         
        @return 清理后的节点
        '''
        if type(node) == types.ListType:
            result = []
            for row in node:
                if row != None and len(row) > 0:
                    result.append(row)
        elif type(node) == types.DictionaryType:
            result = {}
            for key in node:
                value = node.get(key)
                cleaned_value = self.clean(value)
                if cleaned_value != None and len(cleaned_value) > 0:
                    result[key] = cleaned_value
        else:
            if node != None:
                result = node
            
        return result
