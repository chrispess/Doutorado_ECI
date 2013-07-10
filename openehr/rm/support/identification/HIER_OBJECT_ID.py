# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.support.identification.UID_BASED_ID import UID_BASED_ID
from openehr.BASIC_TYPES import typeStr

class HIER_OBJECT_ID(UID_BASED_ID):

    value = typeStr


    #construtor
    def __init__(self, value):
        self.value = value


