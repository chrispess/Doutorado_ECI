# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr

#classe que constroi uma codephrase utilizando umaterminologyID e ums codeString

#léxico: terminology_id = snomed-ct
#        code_string = nnnnnnnnn

class CODE_PHRASE(DATA_VALUE):

    #identificador da terminologia de onde o code_string foi extraido
    #TODO: Matheus: Coloquei parametros dummyes em TERMINOLOGY_ID para passar na execucao

    terminologyID = TERMINOLOGY_ID(name=typeStr, version_id=typeStr)


    #chave utilizada pelo serviço de terminologia para identificar um conceito
    codeString = typeStr


    #construtor
    #TODO: Matheus, Dummie default values, olhar se é cabível
    def __init__(self, teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr):
        self.terminologyID = teminology_id
        self.codeString = code_string

    # retorna o string associado à codephrase
    def toString(self):
        return self.terminologyID + "," + self.codeString


    # retorna terminologyID
    def getTerminologyID(self):
        return self.terminologyID

    #retorna codeString
    def getCodeString(self):
        return self.codeString


    #seta terminologyID
    def setTerminologyID(self, terminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr)):
        self.terminologyID = terminology_id


    #seta codeString
    def setCodeString(self, code_string):
        self.codeString = code_string



