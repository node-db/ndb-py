# coding=utf-8

import node_reader
import node_writer

def read(filename):
    return node_reader.NodeReader().read(filename)

def read_string(data):
    return node_reader.NodeReader().read_string(data)

def write_node(filename, name, node, indent_flag):
    node_writer.NodeWriter().write_node(filename, name, node)

def print_node(name, node, indent_flag):
    return node_writer.NodeWriter().print_node(name, node, indent_flag)

def print_xml(name, node, indent_flag):
    return node_writer.NodeWriter().print_xml(name, node, indent_flag)

