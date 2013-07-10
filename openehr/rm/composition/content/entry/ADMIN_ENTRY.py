# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.composition.content.entry.ENTRY import ENTRY
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.support.identification.OBJECT_REF import OBJECT_REF

class ADMIN_ENTRY(ENTRY):

    #[0..1] descrição do método, como a informação na entry foi obtida
    protocol = ITEM_STRUCTURE

    #[0..1] identificador externo do padrão deonde provém tal action, caso exista
    guideline_id = OBJECT_REF

    #construtor
    def __init__(self,*args):
        if(len(args)==0):
            pass
        elif(len(args)==1):
            self.protocol = args[0]
        elif(len(args)==2):
            self.protocol = args[0]
            self.guideline_id = args[1]

