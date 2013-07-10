# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.rm.support.identification.OBJECT_VERSION_ID import OBJECT_VERSION_ID
from openehr.rm.support.identification.UID import UID
from openehr.rm.support.identification.VERSION_TREE_ID import VERSION_TREE_ID
from openehr.BASIC_TYPES import typeStr

class LOCATABLE_REF(OBJECT_REF):

    #identificador da versão
    id = OBJECT_VERSION_ID(objectID = UID(value = typeStr), creatingSystemID = UID(value = typeStr), versionTreeID = VERSION_TREE_ID(value = typeStr))

    path = typeStr

    # uri criada pela concatenação de "ehr://" + id.value + "/" + path
    as_uri =[]


    type = typeStr


    namespace = typeStr


    #construtor full
    def __init__(self, id, namespace, type, path):
        self.id = id
        self.namespace = namespace
        self.type = type
        self.path = path


    #constrói e retorna as_uri na forma
    # "ehr://" +id.value + "/" + path
    def as_uri(self):
        self.as_uri.append("ehr://")
        self.as_uri.append(self.id.getValue())
        self.as_uri.append("/")
        self.as_uri.append(self.path)

    #retorna path
    def getPath(self):
        return self.path


    #seta o path
    def setPath(self, path):
        self.path = path


