# coding=utf-8

import node_locate

import node_select
import node_update
import node_delete
import node_insert
import node_script
import node_clean
import node_travel

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

def clean(node):
    return node_clean.NodeClean().clean(node)

def travel(node, action):
    return node_travel.NodeTravel().travel(node, action)

def script(node, script_filename):
    return node_script.NodeScript().run(node, script_filename)

