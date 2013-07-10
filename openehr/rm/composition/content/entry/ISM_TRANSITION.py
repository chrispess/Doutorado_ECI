# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.common.archetyped.PATHABLE import PATHABLE
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr



#Instruction State Machine
class ISM_TRANSITION(PATHABLE):

    #[1..1]O estado ISM (Instruction State Machine) corrente
    current_state = DV_CODED_TEXT(CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))

    #[0..1] A transião ISM que ocorreu para
    #chegar ao estado corrente.
    #Codificado pelo openEHR terminoly group "instruction transitions"
    transitions = DV_CODED_TEXT(CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))

    #[0..1] o passo no processo de cuidade que ocorreu como parte da geração da ação
    # ex: "dispense", "start_administration". Este atributo representa
    # o label clínico para a atividade
    careflow_step = DV_CODED_TEXT(CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))


    #construtor
    def __init__(self, *args):
        if(len(args)==1):
            self.current_state =args[0]
        elif(len(args)>1):
            self.current_state =args[0]
            self.transitions = args[1]
            self.careflow_step = args[2]

