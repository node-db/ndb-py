#coding=utf-8

import statement
import common
import operate

__version__ = "1.0"

def read(filename):
    return common.read(filename)

def read_string(data):
    return common.read_string(data)

def write_node(filename, name, node):
    common.write_node(filename, name, node)

def print_node(name, node):
    return common.print_node(name, node)

def print_xml(name, node):
    return common.print_xml(name, node)

def execute(node, query, action = None):
    return statement.Statement().execute(node, query, action)

def filter_list(table, query=None, union=False, sort_key=None):
    return operate.filte(table, query, union, sort_key)