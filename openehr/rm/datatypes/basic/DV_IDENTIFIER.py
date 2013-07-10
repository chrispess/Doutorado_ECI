# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE

# classe para criação de um identificador

#atributos

issuer = str()

assigner = str()

id = str()

type = str()



class DV_IDENTIFIER(DATA_VALUE):

    #construtor

    def __init__(self, issuer, assigner, id, type):

        self.issuer = issuer
        self.assigner = assigner
        self.id = id
        self.type = type

    # metodos get
    def getIssuer(self):
        return self.issuer

    def getAssigner(self):
        return self.assigner

    def getId(self):
        return self.id

    def getType(self):
        return self.type


    # metodos set

    def setIssuer(self, issuer):
         self.issuer = issuer

    def setAssigner(self, assigner):
        self.assigner = assigner

    def setId(self, id):
        self.id = id

    def setType(self, type):
        self.type = type


    #verifica se dois identifiers possuem os mosmos valores
    #issuer,assigner,id, type
    def equals(self, other):
        if(self.issuer == other.getIssuer() & self.assigner == other.getAssigner() & self.id == other.getId() & self.type == other.getType()):
            return True
        else:return False