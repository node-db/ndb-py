#coding=utf-8

import statement
import common
import operate

__version__ = "1.0"

'''
# 从文件中加载ndb对象
'''
def read(filename):
    return common.read(filename)

'''
# 从字符串中加载ndb对象
'''
def read_string(data):
    return common.read_string(data)

'''
# 向文件中写入ndb对象
'''
def write_node(filename, name, node, indent_flag = '\t'):
    common.write_node(filename, name, node, indent_flag)

'''
# 打印ndb对象, 默认缩进符为tab
'''
def print_node(name, node, indent_flag = '\t'):
    return common.print_node(name, node, indent_flag)

'''
# 打印ndb对象, 输出为XML格式, 默认缩进符为tab
'''
def print_xml(name, node, indent_flag = '\t'):
    return common.print_xml(name, node, indent_flag)

'''
# 执行ndb语句
'''
def execute(node, query, action = None):
    return statement.Statement().execute(node, query, action)
