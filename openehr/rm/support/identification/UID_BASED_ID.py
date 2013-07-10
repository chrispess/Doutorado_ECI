# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.rm.support.identification.UID import UID
from openehr.BASIC_TYPES import typeStr



# modelo para um identificador UID-based, consistindo de duas partes: 'root' e uma
# parte opcional 'extension'. forma lexica: root::extension


class UID_BASED_ID(OBJECT_ID):

    #value = root [::extension]
    value = []

    #TODO Matheus: Passando valor dumie
    root = UID(typeStr)

    extension = typeStr


    #construtor
    def __init__(self, *args):
        #construtor com root e extension
        if(len(args)==2):
         self.root = args[0]
         self.extension = args[1]
         #constrói a string value
         self.value.append(self.root)
         self.value.append("::")
         self.value.append(self.extension)
         #construtor com apenas root
        elif(len(args)==1):
         self.root = args[0]
         self.value.append(self.root)
        #construtor vazio
        else:pass


    #retorna true se extension não for vazio
    def hasExtension(self):
        if(self.extension != None):
            return True

    #retorna a parte root à esquerda do separador '::'
    def Root(self):
        return self.root

    #retorna a parte extension à direita do separador '::'
    def Extension(self):
        return self.extension

