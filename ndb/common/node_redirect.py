# coding=utf-8

import node_writer
import types

class NodeRedirect():
    '''
    #ndb输出重定向
    '''
    def __init__(self):
        pass
    
    def redirect(self, target, ndb):
        writer = node_writer.NodeWriter()
        
        if type(ndb) != types.DictionaryType:
            ndb = {'result' : ndb}
        
        if str(target).upper() == 'PRINT':
            writer.print_node(None, ndb);
        else:
            writer.write_node(target, None, ndb)