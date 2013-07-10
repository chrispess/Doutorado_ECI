# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.OBJECT_ID  import OBJECT_ID
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.composition.content.entry.ENTRY import ENTRY
from openehr.BASIC_TYPES import typeStr


class CARE_ENTRY(ENTRY):

     #Descrição do método, ou seja, como a informação desta ENTRY foi obtida.
     #ex: para uma OBSERVATION, descreve o método ou instrumento usado
     #para EVALUATION como a avaliação foi feita.
     #para INSTRUCTION como executar a  instrução
     protocol = ITEM_STRUCTURE

     #opcional. identificador externo da norma utilizada, se relevante.
     ##TODO Matheus: OBJECT id não recebe este parametro passado.
     guideline_id = OBJECT_REF(id = OBJECT_ID(value =typeStr), namespace = typeStr, type = typeStr)

     #construtor
     ###TODO Matheus: OBJECT id não recebe este parametro passado.
     def __init__(self, protocol = ITEM_STRUCTURE, guideline_id = OBJECT_REF(id = OBJECT_ID(value =typeStr), namespace = typeStr, type = typeStr)):
         self.protocol = protocol
         self.guideline_id = guideline_id


