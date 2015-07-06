#coding=utf-8

'''

@author: Huiyugeng
'''

import types
import operate

class Statement:
    '''
    ndb语句执行器
    '''

    def __init__(self):
        pass
    

    def execute(self, node, query, action):
        '''
        Execute ndb query
 
        @param query 需要执行的ndb语句
        @param ndb ndb信息
        @param action 自定义行为,如果使用自定义行为，则仅进行定位不执行值变更
      
        @return 执行结果
        '''
        command = query
        
        if ':' in query:
            command = query[0 : query.find(':')].strip()
            query = query[query.find(':') + 1 : len(query)].strip()
        
        query_items = query.split('!!');
        
        if query_items != None and len(query_items) > 0:
            
            path = query_items[0].strip()
            value = ''
            
            if len(query_items) > 1:
                value = query_items[1].strip()

            if action != None:
                return self.__execute(node, command, path, None, action)
            else:
                return self.__execute(node, command, path, value, None)

        return None

    def __execute(self, node, command, path, value, action):

        result = None
        
        if command != None:
            command = command.lower()
            if command == 'select' or command == 'one' or command == 'exist':
                if action != None:
                    result = operate.select(node, path, action)
                else:
                    result = operate.select(node, path)

                if command == 'one':
                    if result != None and type(result) == types.ListType:
                        if len(result) > 0:
                            result = result[0]
                elif command == 'exist':
                    if result != None and type(result) == types.ListType and len(result) > 0:
                        result = True
                    else:
                        result = False
            
            elif command == 'update':
                if action != None:
                    result = operate.update(node, path, value, action)
                else:
                    result = operate.update(node, path, value)
                    
            elif command == 'delete':
                if action != None:
                    result = operate.delete(node, path, value, action)
                else:
                    result = operate.delete(node, path, value)
            
            elif command == 'insert':
                if action != None:
                    result = operate.insert(node, path, value, action)
                else:
                    result = operate.insert(node, path, value)
        return result;
