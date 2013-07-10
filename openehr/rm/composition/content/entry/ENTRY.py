# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.common.generic.PARTY_PROXY import PARTY_REF
from openehr.rm.common.generic.PARTICIPATION import PARTICIPATION
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.BASIC_TYPES import typeBool
from openehr.BASIC_TYPES import typeStr
from openehr.rm.common.generic.PARTY_PROXY import PARTY_PROXY
from openehr.rm.composition.content.CONTENT_ITEM import CONTENT_ITEM
from openehr.rm.common.generic.PARTICIPATION import PARTICIPATION
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.rm.support.identification.OBJECT_ID  import OBJECT_ID



class ENTRY(CONTENT_ITEM):

    #linguagem em que a ENTRY é escrita. codificada pelo
    # openEHR code Set "languages"
    language = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)

    #conjunto de caracteres em que a ENTRY é codificada
    encoding = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)

    #Id da pessoa que é sujeito da ENTRY.
    # ex: doador de órgãos, feto, membro da família, etc
    ###TODO MATHEUS-11-04-13: Retirei o id = do parâmetro, a classe PARTY_REF não espera este parâmetro
    subject = PARTY_PROXY(external_ref = PARTY_REF(OBJECT_REF(typeStr,namespace = typeStr, type = typeStr)))

    #identificação opcional do provedor dasinformações da ENTRY.
    # ex: o paciente, parente ou guardião, o clínico, dispositivo ou software
    ###TODO MATHEUS-11-04-13: Retirei o id = do parâmetro, a classe PARTY_REF não espera este parâmetro
    provider = PARTY_PROXY(external_ref = PARTY_REF(OBJECT_REF(typeStr,namespace = typeStr, type = typeStr)))

    #outros participantes
    other_participations = PARTICIPATION()

    #identificador de workflow externo
    workflow_id = OBJECT_REF(id = OBJECT_ID(value = typeStr), namespace = typeStr, type = typeStr)

    #construtor
    def __init__(self, *args):
        if(len(args)==3):
            self.language = args[0]
            self.encoding = args[1]
            self.subject =args[2]
        elif(len(args)>3):
            self.language = args[0]
            self.encoding = args[1]
            self.subject =args[2]
            self.provider = args[3]
            self.other_participations = args[4]
            self.workflow_id = args[5]


    #retorna true se esta entry é a respeito do sujeito da EHR.
    # Em caso positivo, o atributo "subject" é do tipo "PARTY_SELF"
    def subject_is_self(self):
        if(self.subject.getExternalRef().getType()=="PARTY_SELF"):
            return True


