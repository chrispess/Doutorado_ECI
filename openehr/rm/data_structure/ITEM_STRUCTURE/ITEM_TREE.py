# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.DATA_STRUCTURE import DATA_STRUCTURE
from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ITEM import ITEM

#estrutura de dados do tipo tree.
# utilizada para representar
class ITEM_TREE(DATA_STRUCTURE):

    items = []

    #construtor
    def __init__(self):
        pass


    #insre um ITEM na ITEM_TREE
    def appendItem(self, item = ITEM):
        self.items.append(ITEM)

