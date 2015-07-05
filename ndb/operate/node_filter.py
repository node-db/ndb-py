# coding=utf-8

class NodeFilter:
    '''
    #节点过滤：从ndb中进行数据过滤
    '''
    
    def filte(self, table, query=None, union=False, sort_key=None):
        '''
        List过滤
        
        @param table: 需要过滤的列表
        @param query: 查询条件，支持eq(相等),like（类似），例如['name':{'type': 'eq', 'value': 'wang'}],查找table中name属性为wang的信息
        @param union: 是否采用交叉结果
        @param sort_key: 进行排序的字段
        
        @return: 过滤后的List   
        '''
        if query == None:
            return table
        if table == None:
            return []
        
        _table = []
        if union == False:
            _table = self.filter_and(table, query)
        else:
            _table = self.filter_or(table, query)
            
        #列表排序
        if sort_key != None:
            try:
                _table = sorted(_table, key=lambda row: row.get(sort_key))
            except:
                pass
                
        return _table
    
    '''
    #条件间取与，query中全部条件满足，就加入列表
    '''
    def filter_and(self, table, query):
        _table = []
        
        for row in table:
            add_row = True
            
            for key in query:
                value = query[key]
                query_type = value.get('type')
                query_value = value.get('value')
                
                if value == None:
                    continue
                if query_value == None or query_value == '':
                    continue
                
                if row.has_key(key):
                    row_value = str(row[key]).strip()
                    if query_type == 'eq' and query_value != row_value:
                        add_row = False
                    elif query_type == 'like' and (query_value not in row_value):
                        add_row = False
                else:
                    add_row = False
                        
            if add_row == True:       
                _table.append(row)
        
        return _table
    
    '''
    #条件间取或，query中任意条件满足，就加入列表
    '''
    def filter_or(self, table, query):
        _table = []
        
        for row in table:
            add_row = False
            
            for key in query:
                value = query[key]
                query_type = value.get('type')
                query_value = value.get('value')
                
                if value == None:
                    add_row = True
                    continue
                if query_value == None or query_value == '':
                    add_row = True
                    continue
                
                if row.has_key(key):
                    row_value = str(row[key]).strip()
                    if query_type == 'eq' and query_value == row_value:
                        add_row = True
                    elif query_type == 'like' and (query_value in row_value):
                        add_row = True
                    
                    if add_row == True:
                        break    
                    
                else:
                    add_row = False
                
            if add_row == True:       
                _table.append(row)
        
        return _table
