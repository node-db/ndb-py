#coding=utf-8

import statement
import common
import operate

__version__ = "1.0"

def read(filename):
    return common.read(filename)

def read_string(data):
    return common.read_string(data)

def write_node(filename, name, node, indent_flag = '\t'):
    common.write_node(filename, name, node, indent_flag)

def print_node(name, node, indent_flag = '\t'):
    return common.print_node(name, node, indent_flag)

def print_xml(name, node, indent_flag = '\t'):
    return common.print_xml(name, node, indent_flag)

def execute(node, query, action = None):
    return statement.Statement().execute(node, query, action)
