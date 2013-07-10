# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.identification.ARCHETYPE_ID import ARCHETYPE_ID
from openehr.rm.support.identification.TEMPLATE_ID import TEMPLATE_ID
from openehr.BASIC_TYPES import typeStr

class ARCHETYPED(object):

 archetype_id = ARCHETYPE_ID(rm_originator = typeStr, rm_name = typeStr, rm_entity = typeStr, domain_concept = typeStr, specialization = typeStr, version_id = typeStr)

 template_id = TEMPLATE_ID

 rm_version = typeStr

 #construtor
 def __init__(self, *args):
     #constrói com archetype_id e rm_version
     if(len(args)==2):
         self.archetype_id = args[0]
         self.rm_version = args[1]
     #constrói com archetype_id, rm_version e template_id
     elif(len(args)==3):
         self.archetype_id = args[0]
         self.rm_version = args[1]
         self.template_id = args[2]


