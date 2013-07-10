# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.ITEM import ITEM
from openehr.BASIC_TYPES import typeStr

class ELEMENT (ITEM):

 # data value desse nodo
 value = DATA_VALUE

 #tipo do null value: "indeterminado", "não perguntado"
 null_flavour = DV_CODED_TEXT()

 #nome associado ao elemento
 name = typeStr


 #construtor
 def __init__(self,value, null_flavour ):
     self.value = value
     self.null_flavour= null_flavour


 #seta value
 def setValue(self, value = DATA_VALUE):
     self.value = value

 #seta null_flavour
 def setNull_flavour(self, null_flavour = DV_CODED_TEXT):
     self.null_flavour = null_flavour


 #seta name
 def setName(self, name = typeStr):
     self.name = name

 #retorna name
 def getName(self):
     return self.name


 #retorna value
 def getValue(self):
     return self.value

 #retorna null_flavour
 def getNullFlavour(self):
     return self.null_flavour


 #True se o valor é desconhecido.
 # ex: indeterminado, não questionado
 def is_null(self):
     if self.value == None:
          return True






