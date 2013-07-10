# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ITEM import ITEM
from openehr.BASIC_TYPES import typeInt

#lista ordenada de itens, que podem ser ELEMENTS ou CLUSTERS
class CLUSTER(ITEM):

    #lista ordenada de items:clusters ou elements
    items = []


    #construtor
    def __init__(self):
       pass

    #retorna a lista de  items
    def getCluster(self):
        return self.items

    #seta a lista de items
    def setItems(self,items = []):
        self.items = items

    #retorna o tamanho do cluster
    def getSize(self):
        return self.items.len()

    #insere um elemento no fim da lista
    def append(self,x = ITEM):
        self.items.append(x)

    #retorna um item da posição dada e o remove da lista
    # se não for digitado nenhum indice o último  elemento é removido
    def pop(self, i = typeInt):
      
        self.items.pop(i)

    #insere um elemento num lugar do cluster especificado por um indice
    def insert(self,i = typeInt, x = ITEM):
        self.items.insert(i, x)

    #retorna um elemento do cluster num indice dado
    def getItem(self,i = typeInt):
        return self.items[i]




