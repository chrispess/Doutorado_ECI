# -*- coding: utf-8 -*-
__author__ = 'chrispess'

#especifica pontos periódicos no tempo, linkados a um calendário ou a um evento repetitivo como "caféda manhã"
#baseado no tipo de dado HL7v3 PIVL<T> e EIVL<T>

from openehr.rm.datatypes.timespec.DV_TIME_SPECIFICATION import DV_TIME_SPECIFICATION
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.encapsulated.DV_PARSABLE import DV_PARSABLE
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr

class DV_PERIODIC_TIME_ESPECIFICATION(DV_TIME_SPECIFICATION):

#especificação na sintaxe HL7v3
 value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)

 def __init__(self, value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)):
     self.value = value

 #o periodo de duração. extraído de value
 def period(self):
     pass

 # alinhamento do  calendário. extraído de value
def calendar_alignment(self):
     pass

 #alinhamennto de evento. extraído de value

def event_alignment(self):
     pass

  #extraído de value
def institution_specified(self):
     pass
