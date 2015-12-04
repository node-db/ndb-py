# coding=utf-8

import types

class NodeWriter():

    def write_node(self, filename, node_name, node, indent_flag):
        '''
        #将节点数据信息写入文件
        '''
        output = open(filename, 'w')
        output.write(self.print_node(node_name, node, indent_flag))
        output.close()
    
    def print_node(self, node_name, node, indent_flag):
        return self.__print_node(0, node_name, node, indent_flag)
    
    def print_xml(self, node_name, node, indent_flag):
        return self.__print_xml(0, node_name, node, indent_flag)

    def __print_node(self, indent, node_name, node, indent_flag):
        '''
        #将节点数据内容输出为ndb格式的字符串
        
        @param indent: 缩进量
        @param node_name: 根节点名称
        @param node: 节点数据
        @param indent_flag: 缩进标识符, 默认\t 
        
        @return: 节点数据字符串
        '''
        if type(node) != types.DictionaryType:
            raise 'Node is NOT DictionaryType'
        
        result = []
        
        next_indent = indent + 1;
        
        if node_name != None and node_name != '':
            result.append(indent_flag * indent + node_name + '{\n')
        else:
            next_indent = indent
            
        for key in node.keys():
            value = node[key]
            if type(value) == types.ListType and len(value) != 0:
                for item in value:
                    if type(item) == types.DictionaryType:
                        result.append(self.__print_node(next_indent, key, item, indent_flag))
                    if type(item) == types.StringType:
                        result.append(indent_flag * next_indent + '{0}:{1}\n'.format(key, item))
                        
            if type(value) == types.DictionaryType and len(value.keys()) != 0:
                result.append(self.__print_node(next_indent, str(key), value, indent_flag))
                
            if (type(value) == types.StringType or type(value) == types.UnicodeType) and value != '':
                result.append(indent_flag * next_indent + '{0}:{1}\n'.format(key, value))
                
            if type(value) == types.IntType or type(value) == types.LongType or type(value) == types.BooleanType:
                result.append(indent_flag * next_indent + '{0}:{1}\n'.format(key, str(value)))
        
        if node_name != None and node_name != '':
            result.append(indent_flag * indent + indent_flag * indent + '}\n')
            
        return ''.join(result)


    def __print_xml(self, indent, node_name, node, indent_flag):
        '''
        #将节点数据内容输出为XML格式的字符串
        
        @param node_name: 根节点名称
        @param node: 节点数据
        
        @return: 节点数据XML字符串
        '''
        result = []
    
        next_indent = indent + 1;
        
        if node_name != None:
            node_name = str(node_name).split()
            
        if node_name != None and node_name != '':
            result.append(indent_flag * indent + '<{0}>\n'.format(node_name))
        else:
            next_indent = indent
            
        for key in node.keys():
            value = node[key]
            if type(value) == types.ListType and len(value) != 0:
                for item in value:
                    if type(item) == types.DictionaryType:
                        result.append(self.__print_xml(next_indent, key, item, indent_flag))
                    if type(item) == types.StringType:
                        result.append(indent_flag * next_indent + '<{0}>{1}</{0}>\n'.format(key, item))
                        
            if type(value) == types.DictionaryType and len(value.keys()) != 0:
                result.append(self.__print_xml(next_indent, key, value, indent_flag))
                
            if (type(value) == types.StringType or type(value) == types.UnicodeType) and value != '':
                result.append(indent_flag * next_indent + '<{0}>{1}</{0}>\n'.format(key, value))
                
            if type(value) == types.IntType or type(value) == types.LongType or type(value) == types.BooleanType:
                result.append(indent_flag * next_indent + '<{0}>{1}</{0}>\n'.format(key, str(value)))
                
        if node_name != None and node_name != '':   
            result.append('<{0}>\n'.format(node_name))
        
        return ''.join(result)
