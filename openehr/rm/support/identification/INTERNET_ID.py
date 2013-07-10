# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.UID import UID
from openehr.BASIC_TYPES import typeStr
#usado como identificador único de um domínio de internet

class INTERNET_ID(UID):

    value = typeStr

    # construtor
    def __init__(self, value):
       self.value = value
