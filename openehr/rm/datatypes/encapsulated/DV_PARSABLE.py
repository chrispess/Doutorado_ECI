# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeStr
from openehr.rm.datatypes.encapsulated.DV_ENCAPSULATED import DV_ENCAPSULATED

#data encapsulada na forma de um string parsable. plain text
# usada para representar valores que são representações textuais formais
class DV_PARSABLE(DV_ENCAPSULATED):

    #tamanho em bytes
    size = typeInt

    #string parsable
    value = typeStr

    #nome do formalismo. ex: GLIF 1.0, proforma
    formalism = typeStr

    #construtor
    def __init__(self, size = typeInt, value = typeStr, formalism = typeStr):
     self.size = size
     self.value = value
     self.formalism = formalism


     #retorna o tamanho da string value em bytes
     def size(self):
        return self.value.__sizeof__()

