# coding=utf-8
import types

import ndb

class NodeScript():
    
    def __init__(self):
        pass
    
    def run(self, node, script):
        if type(node) == types.StringType:
            node = ndb.read(node)
        
        query_list = []
        if type(script) == types.StringType or type(script) == types.UnicodeType:
            try:
                query_list = [line for line in open(script, 'r').readlines()]
            except:
                pass
        if type(script) == types.ListType:
            query_list = script
            
        for query in query_list:
            node = ndb.execute(node, query)
            
        return node
            