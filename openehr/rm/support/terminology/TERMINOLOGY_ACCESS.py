# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeBool
#no  original da especificação OpenEHR trata-se de uma interface
#define um  objeto que provê um acesso proxy a uma terminologia

class TERMINOLOGY_ACCESS():

    #construtor
    def __init__(self):
        pass


    #identificador externo a uma terminologia
    id = typeStr

    #identificador externo de uma terminologia
    def id(self, id = typeStr):
        self.id = id

    #retorna todos os códigos da terminologia
    def all_codes(self):

        all_codes = []
        return  all_codes


    #retorna todos os códigos  da terminologia agrupados sob "group_id"
    def codes_for_group_id(self, group_id =typeStr):
        codes_group_id = []
        return  codes_group_id


    #retorna "True" se "a_code " consta sob "group_id" na terminologia
    def has_code_for_group_id(self, a_code = typeStr):
        code_group_id = typeBool
        return code_group_id

    #retorna todos os códigos agrupados sob "lang" cujo  nome é "name" na terminologia
    def codes_for_group_name(self, name = typeStr, lang = typeStr):
        codes_group_name = []
        return codes_group_name


    #retorna todas as  rubricas sob o código "code" na linguagem "lang"
    def rubric_for_code(self, code = typeStr, lang = typeStr):
        rubrica = typeStr
        return rubrica


