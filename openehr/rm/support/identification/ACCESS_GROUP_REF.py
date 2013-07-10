# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.rm.support.identification.OBJECT_REF import OBJECT_ID

#referência para um access group num accessGroupRef


class ACCESS_GROUP_REF(OBJECT_REF):
	#TODO Matheus: Passando valor dumie
    id = OBJECT_ID(4)  #id unico de um objeto. != null



#construtor
    def __init__(self, id):
     self.id = id
