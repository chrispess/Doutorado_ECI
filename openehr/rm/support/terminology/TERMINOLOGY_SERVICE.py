# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeBool
from openehr.rm.support.terminology.OPENEHR_CODE_SET_IDENTIFIERS import OPENEHR_CODE_SET_IDENTIFIERS
from openehr.rm.support.terminology.OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS import OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS
from openehr.rm.support.terminology.TERMINOLOGY_ACCESS import TERMINOLOGY_ACCESS
from openehr.rm.support.terminology.CODE_SET_ACCESS import CODE_SET_ACCESS


class TERMINOLOGY_SERVICE(OPENEHR_CODE_SET_IDENTIFIERS, OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS):

    #construtor
    def __init__(self):
        pass

    #retorna uma interface para uma terminologia chamada "name"
    def terminology(self, name = typeStr):
        terminology_access = TERMINOLOGY_ACCESS
        return terminology_access


    #retorna uma interface para um "code_set"identificado por "name"
    def code_set(self, name =typeStr):
        code_set_access = CODE_SET_ACCESS
        return code_set_access

    #retorna uma interface para um code_set internamente identificado por  "id'
    def code_set_for_id(self,id = typeStr):
        code_set_access = CODE_SET_ACCESS
        return code_set_access

    #retorna True se a terminologia identificada  por "name" é conhecida
    def has_terminology(self, name = typeStr):
        has_terminology = typeBool
        return has_terminology

    #retorna True se  o code_set linkado por "name" está acessível
    def has_code_set(self, name = typeStr):
        has_code_set = typeBool
        return has_code_set

    #conjunto de todas as terminologias de um dado serviço
    #lista de meta dados em <http://www.nlm.nih.gov/research/umls/metaa1.html>
    def terminology_identifiers(self):
     terminologias = []
     return terminologias

    #lista  de todos os identificadores de code_sets de um dado serviço de terminologias
    def code_set_identifiers(self):
        identificadores = []
        return identificadores

    #conjunto de todos os identificadores para um code_set para os quais ha  um nome OpenEHR. retorna como um dicionário (hash) de  <id, nome interno>
    def openehr_code_sets(self):
        all_code_set = dict
        return all_code_set
