ndb-py
============================================

py-task is a light node database for Python.

- Flexible Data Model
- Expressive Query Language
- Easy to use in Python

Installation
--------------

The lastest stable is ndb-py-1.1.tar.gz

.. code-block:: shell

    python setup.py install
    
Getting Start
--------------

demo for ndb-py:

.. code-block:: python

    import ndb
    
    self.node = ndb.read('example.ndb')
    reslt = ndb.execute(self.node, 'select:root->parent->child->name:/.*m/')
    print("First Record : " + result[0].get('name') + '\n')
    print("Second Record : " + result[1].get('name') + '\n')
    

Documentation
--------------

Basic documentation is hosted on README.md

License
--------------

ndb-py is licensed under the Apache License, Version 2.0. See LICENSE for full license text