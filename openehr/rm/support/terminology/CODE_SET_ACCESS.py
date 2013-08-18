# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr

#no  original da especificação OpenEHR trata-se de uma interface
#define um  objeto que provê um acesso proxy a um "code_set"

class CODE_SET_ACCESS():

    #construtor
    def __init__(self):
        pass

    #identificador externo a um code_set
    id = typeStr

    #identificador externo de um code_set
    def id(self, id = typeStr):
        self.id = id

    #retorna todos ops códigos do code_set
    def all_codes(self):
        pass

    #retorna True se o code_set contém "a_lang"
    def has_lang(self):
        pass

    # retorna True se o code_set contém "a_code"
    def has_code(self):
        pass








