# -*- coding: utf-8 -*-
__author__ = 'chrispess'


# classe que especifica pontosno tempo numa  sintaxe geral

from openehr.rm.datatypes.timespec.DV_TIME_SPECIFICATION import DV_TIME_SPECIFICATION
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.encapsulated.DV_PARSABLE import DV_PARSABLE
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr

class DV_GENERAL_TIME_SPECIFICATION(DV_TIME_SPECIFICATION):

#especificação na sintaxe HL7v3
    value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)

    def __init__(self, value = DV_PARSABLE(size = typeInt, value = typeStr, formalism = typeStr)):
        self.value = value

        #indica qual o ponto do calendário ao qual a
    # especificação está alinhada. retirado do atributo 'value'
    def calendar_alignment(self):
     pass

     #alinhamennto de evento. extraído de value

    def event_alignment(self):
     pass

     #extraído de value
    def institution_specified(self):
     pass