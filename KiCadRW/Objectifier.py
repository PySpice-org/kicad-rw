####################################################################################################
#
# KiCad-RW — Python library to read/write KiCad Sexpr file format
# Copyright (C) 2021 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

__all__ = [
]

####################################################################################################

import logging

import sexpdata
from sexpdata import car, cdr, Symbol

####################################################################################################

_module_logger = logging.getLogger(__name__)

####################################################################################################

def car_value(_):
    return car(_).value()

####################################################################################################

class TreeMixin:

    ##############################################

    def __init__(self):
        self._childs = []

    ##############################################

    def __bool__(self):
        return bool(self._childs)

    def __len__(self):
        return len(self._childs)

    def __iter__(self):
        return iter(self._childs)

    ##############################################

    def append_child(self, child):
        self._childs.append(child)

    ##############################################

    def depth_first_search(self, on_node=None, on_leaf=None):
        if on_node:
            on_node(self)
        for child in self:
            if isinstance(child, Node):
                child.depth_first_search(on_node, on_leaf)
            elif on_leaf:
                on_leaf(child)

####################################################################################################

class Node(TreeMixin):

    ##############################################

    def __init__(self, path):
        super().__init__()
        self._path = path

    ##############################################

    @property
    def name(self):
        return self._path[-1]

    @property
    def path(self):
        return self._path

    @property
    def path_str(self):
        return '/'.join(self._path)

    @property
    def parent_str(self):
        _ = self._path[:-1]
        if _:
            return '/'.join(_)
        return '/'

####################################################################################################

class SchemaNode(TreeMixin):

    NODES = {}

    ##############################################

    @classmethod
    def get_node(cls, node):
        if not cls.NODES:
            cls.NODES['/'] = SchemaNode('/')
        path_str = node.path_str
        if path_str in cls.NODES:
            return cls.NODES[path_str]
        else:
            schema_node = SchemaNode(node.name)
            cls.NODES[path_str] = schema_node
            parent = cls.NODES[node.parent_str]
            parent.append_child(schema_node)

    ##############################################

    def __init__(self, name):
        super().__init__()
        self._name = name

    ##############################################

    @property
    def name(self):
        return self._name

    ##############################################

    def __repr__(self):
        return self._name

####################################################################################################

class Objectifier:

    _logger = _module_logger.getChild('Objectifier')

    ##############################################

    def __init__(self, path):

        self._logger.info(f"Load {path}")
        with open(path) as fh:
            sexpr = sexpdata.load(fh)

        self._root = self._walk_sexpr(sexpr)
        # self.dump()
        # self.get_paths()
        self.get_schema()
        print(SchemaNode.NODES)

    ##############################################

    def dump(self, root=None):
        if root is None:
            root = self._root
        def on_node(node):
            print(node.path_str)
        def on_leaf(leaf):
            print(f"    {leaf}")
        root.depth_first_search(on_node, on_leaf)

    ##############################################

    def get_paths(self, root=None):
        if root is None:
            root = self._root
        paths = set()
        def on_node(node):
            paths.add(node.path_str)
        root.depth_first_search(on_node)
        for _ in sorted(paths):
            print(_)

    ##############################################

    def get_schema(self, root=None):
        if root is None:
            root = self._root
        def on_node(node):
            SchemaNode.get_node(node)
        def on_leaf(leaf):
            pass
        root.depth_first_search(on_node, on_leaf)

    ##############################################

    def _walk_sexpr(self, sexpr, path=[]):
        """Perform a depth first search"""
        if isinstance(sexpr, (str, int, float)):
            return sexpr
        elif isinstance(sexpr, Symbol):
            return sexpr   # ??? .value()
        elif isinstance(sexpr, list):
            _car = car(sexpr).value()
            _cdr = cdr(sexpr)
            path = path.copy()
            path.append(_car)
            node = Node(path)
            for element in _cdr:
                child = self._walk_sexpr(element, path)
                node.append_child(child)
            return node
        else:
            raise ValueError()
