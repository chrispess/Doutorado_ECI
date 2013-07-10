# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeInt

class PROPORTION_KIND(object):


    #classe de constantes definindo tipos de proporções para a classe DV_PROPORTION
    value = typeInt

    #value
    def __init__(self, value):
        self.value = value


    #retorna value
    def getValue(self):
        return self.value


    #true se n é um dos tipos pré-definidos
    def valid_proportion_kind(self, n = typeInt):
        if(n == 0 or n == 1 or n == 2 or n == 3 or n == 4):
            return True
        else:return False


    #retorna o tipo de proporção (PROPORTION_KIND) de um valor inteiro
    def valueOff(self, value = typeInt):
        if value == 0:
          return "pk_ratio"
        elif value == 1:
          return "pk_unitary"
        elif value == 2:
          return "pk_percent"
        elif value == 3:
          return "pk_fraction"
        elif value == 4:
          return "pk_integer_fraction"
        else:raise




