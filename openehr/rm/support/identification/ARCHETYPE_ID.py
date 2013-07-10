# -*- coding: utf-8 -*-
__author__ = 'chrispess'


''' léxico
archetype_id: qualified_rm_entity ‘.’ domain_concept ‘.’ version_id
qualified_rm_entity: rm_originator ‘-’ rm_name ‘-’ rm_entity
rm_originator: V_ALPHANUMERIC_NAME
rm_name: V_ALPHANUMERIC_NAME
rm_entity: V_ALPHANUMERIC_NAME
domain_concept: concept_name { ‘-’ specialisation }*
concept_name: V_ALPHANUMERIC_NAME
specialisation: V_ALPHANUMERIC_NAME
version_id: ‘v’ V_NONZERO_DIGIT [ V_NUMBER ]
# padrão léxico
V_ALPHANUMERIC_NAME: [a-zA-Z][a-zA-Z0-9_]+
V_NONZERO_DIGIT: [1-9]
V_NUMBER: [0-9]+   '''



from openehr.rm.support.identification.OBJECT_ID import OBJECT_ID
from openehr.BASIC_TYPES import typeStr


class ARCHETYPE_ID(OBJECT_ID):

    #referência, globalmente, uma entidade do modelo.
    # ex openehr-composition-OBSERVATION
    qualifiedRmEntity = typeStr

    #organizaão de onde se origina o modelo de referência base do arquétipo.
    #ex: "openehr", "cen", "hl7"
    rmOriginator = typeStr

    #nome do modelo de referência.
    # ex: "en13606", "ehr_rm"
    rmName = typeStr

    #nome do nível ontológico do modelo de referência do qual o arquétipo se origina.
    # ex: "section", "entry", "folder", "composition"
    rmEntity = typeStr

    #nomedoconceito representado pelo arquétipo, incluindo especializações.
    # ex: "biochemistry_result-cholesterol"
    domainConcept = typeStr

    #nome da especialização do conceito, se o arquétipo for a especialização
    # de outro arquétipo. ex: "cholesterol"
    specialization = typeStr

    #versão do arquétipo
    versionID = typeStr

    #construtor
    def __init__(self, rm_originator, rm_name, rm_entity, domain_concept, specialization, version_id):
        self.rmOriginator = rm_originator
        self.rmName = rm_name
        self.rmEntity = rm_entity
        self.domainConcept = domain_concept
        self.specialization = specialization
        self.versionID = version_id






