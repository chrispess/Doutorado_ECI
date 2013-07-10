# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.composition.content.entry.ISM_TRANSITION import ISM_TRANSITION
from openehr.rm.composition.content.entry.INSTRUCTION_DETAILS import INSTRUCTION_DETAILS
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.composition.content.entry.CARE_ENTRY import CARE_ENTRY

#usada para recordar uma aão clínica que pode ter sido adhoc, ou ter ocorrido
#em paralelo com uma ACTIVITY num workflow do tipo INSTRUCTION.


class ACTION(CARE_ENTRY):

    #ponto no tempo em quea ação foi completada
    time = DV_DATE_TIME

    #descrição da atividade axecutada na forma  de uma estrutura do tipo arquétipo
    description = ITEM_STRUCTURE

    #detalhes da transição na máquina de estados "INSTRUCTION" causada por esta ação
    ism_transition = ISM_TRANSITION

    #detalhes da instrução que fez com que ocorresse essa ACTION, caso haja
    instruction_details = INSTRUCTION_DETAILS


    #construtor
    def __init__(self, *args):
        if(len(args)==3):
            self.time = args[0]
            self.description = args[1]
            self.ism_transition = args[2]
        elif(len(args)==4):
            self.time = args[0]
            self.description = args[1]
            self.ism_transition = args[2]
            self.instruction_details = args[3]