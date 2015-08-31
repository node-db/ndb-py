# coding=utf-8

import types

class NodeReader():
    '''
    #读取并解析ndb文件
    '''
    
    def __init__(self):
        self.linenum = 0
    
    def read(self, filename):
        '''
        #读取ndb文件中的内容并进行解析，生成一个ndb对象（Dictionary Object）
        
        @param filename: ndb文件名
        
        @return: 载入的ndb对象(Dictionary Object)
        '''
        try:
            _list = [line for line in open(filename, 'r').readlines()]
        except:
            _list = []
        return self.__parse(_list)
    

    def read_string(self, data):
        '''
        #从字符串中载入ndb数据，生成一个ndb对象（Dictionary Object）
        @param data: ndb格式的字符串
        
        @return: 载入的ndb对象(Dictionary Object)
        '''
        try:
            _list = data.split('\n')
        except:
            _list = []
        return self.__parse(_list)
    

    def __parse(self, _list):
        '''
        #解析Dictionary对象
        '''
        node = {}

        while self.linenum < len(_list):
            
            try:
                line = _list[self.linenum].strip()
        
                self.linenum = self.linenum + 1
                
                # 过滤注释信息，注释信息以#开头
                if line == None or line == '' or line.startswith('#'):
                    continue
                
                # 如果行中含有'{' 则将下面的内容进行递归
                if line.endswith('{'):
                    node_name = line[0: line.find('{')].strip()
                    node_value = self.__parse(_list)
                    sub_node = node.get(node_name)
                    
                    if sub_node == None:
                        node[node_name] = node_value
                    else:
                        node_list = sub_node if type(sub_node) == types.ListType else [sub_node]
                        node_list.append(node_value)
                        node[node_name] = node_list
                
                # 如果行中含有 '}' 则返回解析后的内容        
                elif line.endswith('}'):
                    return node
                
                else:    
                    if ':' in line:
                        node_name = line[0: line.find(':')].strip()
                        item_value = line[line.find(':') + 1: len(line)].strip()
                    
                        if node_name != None and node_name !="":
                            node_value = node.get(node_name) if node_name != None else None
                        
                        if node_value != None:
                            item_value_list = node_value if type(node_value) == types.ListType else [node_value]
                            item_value_list.append(item_value)   
                            node[node_name] = item_value_list
                        else:
                            node[node_name] = item_value
            except:
                pass
        
        return node
