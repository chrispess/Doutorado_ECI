# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.BASIC_TYPES import typeBool



class DV_STATE(DATA_VALUE):

 #nome do estado. determinados pela tabela'state/event'
 # codificada utilizando terminologia OpenEHR
 value = DV_CODED_TEXT() #value != vazio

 #indica quando é um estado terminal, como "aborted","completed", etc
 is_terminal = typeBool # is_terminal != vazio


 #construtor
 def __init__(self, value, is_terminal):
     self.value = value
     self.is_terminal = is_terminal

 #retorna is_terminal
 def isTerminal(self):
     return self.is_terminal

 #retorna o estado (value)
 def getValue(self):
     return self.value


 #seta is_terminal
 def setIs_terminal(self,is_terminal):
     self.is_terminal = is_terminal

 #seta value
 def setValue(self, value):
     self.value = value



