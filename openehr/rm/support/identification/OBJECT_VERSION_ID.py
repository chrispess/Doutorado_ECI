# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.UID_BASED_ID import UID_BASED_ID
from openehr.rm.support.identification.UID import UID
from openehr.rm.support.identification.VERSION_TREE_ID import VERSION_TREE_ID

# classe para gerar um identificador unico para uma versão deum objeto versionado



from openehr.BASIC_TYPES import typeStr

class OBJECT_VERSION_ID(UID_BASED_ID):

    #identificador único para objetos
    objectID = UID(value = typeStr)

    #identificador do sistema que criou
    creatingSystemID = UID(value = typeStr)

    #identificador desta versão com respeito a outra
    # versão na mesma  árvore de versões. números separados
    # por pontos: "1", "2.1.4"
    versionTreeID = VERSION_TREE_ID(value =typeStr)

    # a forma da string de um OBJECT_VERSION_ID associada ao atributo value consiste
    # em três segmentos separados por duplo dois pontos (::)
    # value = objectID + '::'+ creatingSystemID + '::' + versionTreeID
    # Exemplo: F7C5C7B7-75DB-4b39-9A1E-C0BA9BFDBDEC::87284370-2D4B-4e3d-A3F3-F303D2F4F34B::2
    value = ""

    #construtor

    def __init__(self, objectID, creatingSystemID, versionTreeID):
        self.objectID = objectID
        self.creatingSystemID = creatingSystemID
        self.versionTreeID = versionTreeID

#TODO Matheus: troquei toString() para o cast str() e
#dado que str não tem append fiz uma concatenação normal
        self.value = self.value + str(self.objectID) #verificar se chamada de método
        self.value = self.value + "::" #está correta
        self.value = self.value + str(self.creatingSystemID)
        self.value = self.value + "::"
        self.value = self.value + str(self.versionTreeID)


    def __init__(self, objectID = str(), creatingSystemID = str(), versionTreeID = str()):
#TODO Matheus: troquei toString() para o cast str() e
#dado que str não tem append fiz uma concatenação normal
        self.value = self.value + str(self.objectID) #verificar se chamada de método
        self.value = self.value + "::"                #está correta
        self.value = self.value + str(self.creatingSystemID)
        self.value = self.value + "::"
        self.value = self.value + str(self.versionTreeID)

    #retorna objectID
    def ObjectID(self):
        return self.objectID

    #retorna creatingSystemID
    def  CreatingSystemID(self):
        return self.creatingSystemID

    #retorna VersionTreeID
    def VersionTreeID(self):
        return self.versionTreeID


    #retorna value
    def getValue(self):
        return self.value

    #seta o valor da string value
    def setValue(self, value):
        self.value = value


