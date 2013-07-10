# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.BASIC_TYPES import typeStr

class GENERIC_ID(OBJECT_ID):


    value = typeStr

    scheme = typeStr


    #construtor
    def __init__(self, value, scheme):
        self.value = value
        self.scheme = scheme


    #retorna scheme
    def Scheme(self):
        return self.scheme


    #verifica se GENERIC_ID é igual
    def equals(self, other):
        if(self == other):
            return True
        else:return False
