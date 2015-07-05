# coding=utf-8

import node_locate
import node_filter

import node_select
import node_update
import node_delete
import node_insert

def select(node, path, action=None):
    return node_select.NodeSelect().select(node, path, action)

def update(node, path, value, action=None):
    return node_update.NodeUpdate().update(node, path, value, action)

def delete(node, path, value, action=None):
    return node_delete.NodeDelete().delete(node, path, value, action)

def insert(node, path, value, action=None):
    return node_insert.NodeInsert().insert(node, path, value, action)
    
def locate(node, query, multi, is_create=False):
    return node_locate.NodeLocate().locate(node, query, multi, is_create)

def filte(table, query=None, union=False, sort_key=None):
    return node_filter.NodeFilter().filte(table, query, union, sort_key)
