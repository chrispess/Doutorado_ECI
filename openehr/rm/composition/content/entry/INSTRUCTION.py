# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.composition.content.entry.CARE_ENTRY import CARE_ENTRY
from openehr.rm.composition.content.entry.ACTIVITY import ACTIVITY
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.support.identification.LOCATABLE_REF import LOCATABLE_REF
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.datatypes.encapsulated.DV_PARSABLE import DV_PARSABLE

#utilizada para especificar ações no futuro
class INSTRUCTION(CARE_ENTRY):

    #[1..1] A respeito do que é a instrução
    narrative = DV_TEXT

    #[0..1] Lista de todas as atividades numa instrução
    activities = ACTIVITY()

    #[0..1] date/time de quando a instrução pode serassumidacomo terminada
    expiry_time = DV_DATE_TIME

    #opcional. expressão executável da instrução numa máquina workflow
    wf_definition = DV_PARSABLE

    #construtor
    def __init__(self, *args):
        if(len(args)==1):
            self.narrative = args[0]
        elif(len(args)==2):
            self.narrative = args[0]
            self.activities = args[1]
        elif(len(args)==4):
            self.narrative = args[0]
            self.activities = args[1]
            self.expiry_time = args[2]
            self.wf_definition = args[3]


