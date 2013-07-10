# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.composition.content.CONTENT_ITEM import CONTENT_ITEM
from openehr.BASIC_TYPES import typeInt

class SECTION (CONTENT_ITEM):

    #lista ordenada de itens que pode conter, outras sections ou ENTRYs
    ##TODO Matheus: troca [] por ()
    items = CONTENT_ITEM()

    #construtor
    ###TODO Matheus: troca [] por ()
    def __init__(self,items = CONTENT_ITEM()):
        self.items = items

    #adiciona algum item na lista
    def appendItens(self,item = CONTENT_ITEM):
        self.items.append(item)


    #retorna a lista de  items
    def getCluster(self):
        return self.items

    #seta a lista de items
    def setItems(self,items = []):
        self.items = items

    #retorna o tamanho da section
    def getSize(self):
        return self.items.len()

    #insere um elemento no fim da section
    def append(self,item = CONTENT_ITEM):
        self.items.append(item)

    #retorna um item da posição dada e o remove da lista
    # se não for digitado nenhum indice o último  elemento é removido
    def pop(self, i = typeInt):

        self.items.pop(i)

    #insere um elemento num lugar do section especificado por um indice
    def insert(self,i = typeInt, x = CONTENT_ITEM):
        self.items.insert(i, x)

    #retorna um elemento da section num indice dado
    def getItem(self,i = typeInt):
        return self.items[i]


