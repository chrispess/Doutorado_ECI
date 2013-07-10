# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE

class DV_BOOLEAN(DATA_VALUE):

    #atributos
    #valor booleano carregado pelo item
    value = bool()


    #construtor
    def __init__(self, value):
        self.value = value


    #retorna o valor booleano do item
    def getValue(self):
        return self.value

    #seta um valor booleano
    def setValue(self, value):
        self.value =value

    #compara o valor com outro booleano
    def equals(self, value):
        if(self.value == value):
         return True
        else:return False


