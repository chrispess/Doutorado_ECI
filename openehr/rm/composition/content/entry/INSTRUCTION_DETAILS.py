# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.common.archetyped.PATHABLE import PATHABLE
from openehr.rm.support.identification.LOCATABLE_REF import LOCATABLE_REF
from openehr.BASIC_TYPES import typeStr
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE

class INSTRUCTION_DETAILS(PATHABLE):

    #referencia causadora da INSTRUCTION
    instruction_id = LOCATABLE_REF

    #identifica a atividade na instrução
    activity_id = typeStr

    #vários detalhes de workflow-engines incluindo:
    #condições que disparam a ACTION.
    # Lista de notificações que ocorrem
    wf_details = ITEM_STRUCTURE


    #construtor
    def __init__(self, *args):
        if(len(args)==2):
            self.instruction_id = args[0]
            self.activity_id = args[1]
        elif(len(args)==3):
            self.instruction_id = args[0]
            self.activity_id = args[1]
            self.wf_details=args[2]

