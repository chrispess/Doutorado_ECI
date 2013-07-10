# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ELEMENT import ELEMENT
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr

#estrutura de dados do tipo lista, onde cada itempossui um valor e pode
# ser por um nome e um indice

class ITEM_LIST(ITEM_STRUCTURE):

    #representação de uma lista de elementos
    items = []

    #consturtor
    def __init__(self, items = []):
        self.items = items


    #retorna a lista de items
    def getItems(self):
        return self.items


    #retorna o numero de elementos da  lista
    def item_count(self):
        return self.items.len()

    #retorna um elemento da lista
    def getIthItem(self, i = typeInt):
        return self.items[i]

    #retorna uma lista dos nomes dos elementos da ITEM_LIST
    def names(self):
        listNames = []
        for ELEMENT in self.items:
            listNames.append(ELEMENT.getName())
        return listNames

    #retorna o ELEMENT cujo nome é "a_name"
    def named_item(self, a_name = typeStr):
        for ELEMENT in self.items:
            if ELEMENT.getName() == a_name:
                return ELEMENT


        #gera um item  compatível com oISO 13606
    def as_hierarchy(self):
        pass