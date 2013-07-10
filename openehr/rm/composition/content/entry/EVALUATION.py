# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE


class EVALUATION(ITEM_STRUCTURE):

 #dados da avaliação na forma de uma estrutura de dados
 data = ITEM_STRUCTURE

 #construtor
 def __init__(self, data = ITEM_STRUCTURE):
     self.data = data


 #retorna data
 def getData(self):
     return self.data

 #seta data
 def setData(self, data = ITEM_STRUCTURE):
     self.data = data




