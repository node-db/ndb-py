# coding=utf-8
import types

import ndb

class NodeScript():
    
    def __init__(self):
        pass
    
    def run(self, node, script_filename):
        if type(node) == types.StringType:
            node = ndb.read(node)
        try:
            script = [line for line in open(script_filename, 'r').readlines()]
        except:
            script = []
        for query in script:
            node = ndb.execute(node, query)
        return node
            