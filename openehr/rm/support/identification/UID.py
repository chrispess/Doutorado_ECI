# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr

class UID():
    value = typeStr
    # cria um UID por valor. não pode ser nulo
    def __init__(self, value):

        self.value = value


    # retorna o valor da id
    def getValue(self):
        return self.value

    #retorna string representativo do valor
    def toString(self):
        uid = []
        uid.append(self.value)
        return uid

    # verifica se dois UID's possuem o mesmo valor
    def equals(self, other):
        if(self == other):
            return True
        else:return False






