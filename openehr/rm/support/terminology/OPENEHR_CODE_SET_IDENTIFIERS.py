# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr

#lista de identificadores para conjunto de códigos do "OpenEHR terminology"
class OPENEHR_CODE_SET_IDENTIFIERS():

    #construtor
    def __init__(self):
        pass

    #constante igual a “character sets”
    Code_set_id_character_sets = typeStr
    Code_set_id_character_sets = "character sets"

    #constante igual a "compression algorithms"
    Code_set_id_compression_algorithms = typeStr
    Code_set_id_compression_algorithms = "compression algorithms"


    #constante igual a “countries”
    Code_set_id_countries = typeStr
    Code_set_id_countries = "countries"

    #constante igual a “integrity check algorithms”
    Code_set_id_integrity_check_algorithms = typeStr
    Code_set_id_integrity_check_algorithms = "integrity check algorithms"


    #constante igual a “languages”
    Code_set_id_languages = typeStr
    Code_set_id_languages = "languages"

    #constante igual a “media types”
    Code_set_id_media_types = typeStr
    Code_set_id_media_types = "media types"

    #constante igual a “normal statuses”
    Code_set_id_normal_statuses = typeStr
    Code_set_id_normal_statuses = "normal statuses"

    #função de validação que testa se um dado identificador
    #está no conjunto de identificadores definido na classe
    def valid_terminology_group_id(self,an_id = typeStr):
        list_constants = ["character sets", "compression algorithms","countries", "integrity check algorithms", "languages", "media types", "normal statuses"]
        if an_id is list_constants:
            return True