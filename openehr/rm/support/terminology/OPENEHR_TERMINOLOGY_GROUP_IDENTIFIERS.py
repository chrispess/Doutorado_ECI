# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr

#lista de identificadores de grupos de terminologias
# do "OpenEHR terminology"


class OPENEHR_TERMINOLOGY_GROUP_IDENTIFIERS():

    #construtor
    def __init__(self):
        pass


    #constante igual a "OpenEHR"
    Terminology_id = typeStr
    Terminology_id = "OpenEHR"

    #constante igual a “audit change type”
    Group_id_audit_change_type = typeStr
    Group_id_audit_change_type = "audit change type"

    #constante igual a “attestation reason”
    Group_id_attestation_reason = typeStr
    Group_id_attestation_reason = "attestation reason"

    #constante igual a “composition category”
    Group_id_composition_category =  typeStr
    Group_id_composition_category = "composition category"

    #constante igual a “event math function”
    Group_id_event_math_function = typeStr
    Group_id_event_math_function = "event math function"

    #constante igual a “instruction states”
    Group_id_instruction_states = typeStr
    Group_id_instruction_states = "instruction states"

    #constante igual a “instruction transitions”
    Group_id_instruction_transitions = typeStr
    Group_id_instruction_transitions = "instruction transitions"

    #constante igual a “null flavours”
    Group_id_null_flavours = typeStr
    Group_id_null_flavours = "null flavours"

    #constante igual a “property”
    Group_id_property = typeStr
    Group_id_property = "property"

    #constante igual a “participation function”
    Group_id_participation_function = typeStr
    Group_id_participation_function = "participation function"

    #constante igual a “participation mode”
    Group_id_participation_mode = typeStr
    Group_id_participation_mode = "participation mode"

    #constante igual a “subject relationship”
    Group_id_subject_relationship = typeStr
    Group_id_subject_relationship = "subject relationship"

    #constante igual a “setting”
    Group_id_setting = typeStr
    Group_id_setting = "setting"

    #constante igual a “term mapping purpose”
    Group_id_term_mapping_purpose = typeStr
    Group_id_term_mapping_purpose = "term mapping purpose"

    #constante igual a “version lifecycle state”
    Group_id_version_lifecycle_state = typeStr
    Group_id_version_lifecycle_state = "version lifecycle state"

    #função de validação que testa se um dado identificador
    #está no conjunto de identificadores definido na classe
    def valid_terminology_group_id(self,an_id = typeStr):
        list_constants = ["OpenEHR", "audit change type", "attestation reason","composition category", "event math function", "instruction states", "instruction transitions", "null flavours", "property", "participation function", "participation mode", "subject relationship", "setting", "term mapping purpose", "version lifecycle state"]
        if an_id is list_constants:
            return True