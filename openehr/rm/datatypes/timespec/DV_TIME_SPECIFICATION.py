# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.encapsulated.DV_PARSABLE import DV_PARSABLE
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr

#classe abstrata da qual toda especificaão de tempo são especializações
class DV_TIME_SPECIFICATION(DATA_VALUE):

 #especificação na sintaxe HL7v3
 value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)

 #construtor
 def __init__(self, value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)):
     self.value = value


 #indica qual o ponto do calendário ao qual a
 # especificação está alinhada. retirado do atributo 'value'
 def calendar_alignment(self):
     pass

 #indica a qual evento do "mundo real" a especificação está alinhada.
 # Se estiver. extraído do atributo 'value'
 def event_alignment(self):
     pass

 #indica se a especificação está alinhada com algum 'institution schedules'
 # extraído do atributo 'value'

 def institution_specified(self):
     pass