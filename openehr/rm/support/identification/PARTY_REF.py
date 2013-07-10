# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.BASIC_TYPES import typeStr


class PARTY_REF(OBJECT_REF):

 #id referenciando participante de um serviço identificado
 id = OBJECT_ID(typeStr)

 #namespace
 namespace = typeStr

 #tipo
 type = typeStr

 #construtor
 def __init__(self, *args):
     if(len(args)==1):
         self.id = args[0]
     elif(len(args)==3):
         self.id = args[0]
         self.namespace = args[1]
         self.type = args[2]


 #retorna type
 def getType(self):
     return self.type









