# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.quantity.DV_ORDERED import DV_ORDERED

class DV_ORDINAL(DV_ORDERED):

 #valor numa enumeração de valores. Qualquer inteiro pode ser usado
 value = typeInt

 #representação textual do value na enumeração. ex: "1", "2', "3'
 symbol = DV_CODED_TEXT(typeStr)


 #construtor
 def __init__(self, value, symbol):
     self.value = value
     self.symbol = symbol


 #seta value
 def setValue(self, value):
     self.value = value

 #seta symbol
 def setSymbol(self,symbol):
     self.symbol = symbol


 #retorna true se os símbolos provêm do mesmo vocabulário
 def isStrictlyComparableTo(self,DV_ORDINAL):
     if((self.symbol.getDefining_code().getTerminologyID().name() == DV_ORDINAL.symbol.getDefinig_code().getTerminologyID().name()) and
        (self.symbol.getDefining_code_code().getTerminologyID().version_id() == DV_ORDINAL.symbol.getDefining_code().getTerminologyID().version_id())):
      return True
     else:return False


 #retorna  os limites da enumeração para possíveis comparações
 def limits(self):

     super(DV_ORDINAL, self).__init__()
     return self.getNormalRange()


 #retorna true se os types são os mesmos e os valores são comparáveis
 def infix(self, other):
     pass