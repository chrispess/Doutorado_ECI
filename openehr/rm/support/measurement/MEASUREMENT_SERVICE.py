# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeBool

##define um  objeto que provê um acesso proxy a um serviço de medida
class MEASUREMENT_SERVICE():

    #construtor
    def __init__(self):
        pass

    #retorna  True se "units" for válido de acordo com a HL7 UCUM
    def is_valid_units_string(self, units = typeStr):
        is_valid = typeBool
        #acesso à HL7 UCUM
        return  is_valid

    #retorna True se as unidades "units1" e "units2" corresponderem à mesma propriedade de medida
    def units_equivalent(self, units1 = typeStr, units2 = typeStr):
        is_equivalente = typeBool
        if units1 == units2:
            return True












