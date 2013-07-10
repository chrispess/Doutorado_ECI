 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


#classe criada para definir o conceito de valores ordenados

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.quantity.DV_INTERVAL import DV_INTERVAL
#TODO: Matheus, Importando REFERENCE_RANGE uma classe que
from openehr.rm.datatypes.quantity.REFERENCE_RANGE import REFERENCE_RANGE
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeFloat


#classe abstrata que define o conceito de valores ordenados
class DV_ORDERED(DATA_VALUE):
   # #valor opcional para um range normal
   normal_range = DV_INTERVAL(typeFloat,typeFloat)

  # #lista de ranges opcionais para este valor neste contexto, em particular
   otherReferenceRanges = REFERENCE_RANGE()

  # #opcional. indicador normal de status do valorcom respeito ao range normal
  # # ver OpenEHR terminology group "normal status"
   normal_status = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(), code_string = typeStr)



   #construtor normal_range, otherReferenceRanges, normal_status
   def __init__(self, *args):
      if(len(args)==3):
       self.normal_range = args[0]
       self.otherReferenceRanges = args[1]
       self.normal_status = args[2]
      elif(len(args)==1):
       self.normal_range = args[0]
      else:pass




  # #retorna true se o valor esta no range normal
   def isNormal(self, value):
       if(self.normal_range.has(value)==True):
           return True

   #retorna normal_range
   def getNormalRange(self):
       return self.normal_range

  # #retorna normal status
   def getNormalStatus(self):
       return self.normal_status

  # #retorna otherReferenceRanges
   def getOtherReferenceRanges(self):
       return self.otherReferenceRanges

  # #retorna true se a quantidade não possui range de referência
   def isSimple(self):
       if(self.otherReferenceRange == None):
           return True

  # #verifica se duas instâncias são estritamente comparáveis
   def isStrictlyComparableTo(self, DV_ORDERED):
       pass