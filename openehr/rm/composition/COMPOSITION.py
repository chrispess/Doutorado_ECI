# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.composition.content.CONTENT_ITEM import CONTENT_ITEM
from openehr.rm.composition.EVENT_CONTEXT import EVENT_CONTEXT
from openehr.rm.common.generic.PARTY_PROXY import PARTY_PROXY
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.rm.support.identification.PARTY_REF import PARTY_REF
from openehr.BASIC_TYPES import typeStr


class COMPOSITION(object):


 # [0..1]. o conteúdo da composition
 # TODO Matheus: Troca de [] por ().
 content = CONTENT_ITEM()

 #[0..1]. contexto da sessão clínica da composition
 context = EVENT_CONTEXT

 #a pessoa primariamente responsável pelo conteúdo da composition
 #é o identificador que aparece na screen. Pode ser, ou não,
 # a pessoa que entrou com os dados.Se for o próprio paciente,
 # a instância "self" é usada
 ###TODO MATHEUS-11-04-13: Retirei o id = do parâmetro, a classe PARTY_REF não espera este parâmetro
 composer = PARTY_PROXY(external_ref = PARTY_REF(OBJECT_REF(typeStr,namespace = typeStr, type = typeStr)))

 #indica a categoria à qual a composition pertence. ex:"persistent",
 # "event", "process", etc
 category = DV_CODED_TEXT(CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))

 #linguagem em que a composition é escrita.
 # codificada por openEHR code set "languages"
 language = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)

 #nome do território em que a composition foi escrita.
 # codificado por openEHR "countries"
 territory = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)


 #construtor
 def __init__(self, *args):
     if(len(args)==4):
         self.composer = args[0]
         self.category = args[1]
         self.language = args[2]
         self.territory = args[3]
     elif(len(args)>4):
         self.content = args[0]
         self.context = args[1]
         self.composer = args[2]
         self.category = args[3]
         self.language = args[4]
         self.territory = args[5]

 #retorna TRUE se o atributo "category"
 # for do tipo "persistente"
 def is_persistent(self):
     if(self.category.getDefiningCode.getCode_string()=="persistent"):
         return True
     else:return False

 #retorna o conteúdo dacomposition
 def getContent(self):
     return self.content

 #retorna o contexto
 def getContext(self):
     return self.context

 #retorna o composer
 def getComposer(self):
     return self.composer

 #retorna categoria
 def getCategory(self):
     return self.category

 #retorna language
 def getLanguage(self):
     return self.language

 #retorna território
 def getTerritory(self):
     return self.territory


