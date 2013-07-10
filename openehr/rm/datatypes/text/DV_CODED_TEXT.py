# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.BASIC_TYPES import typeStr
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE

#um item de texto cujo valor pode ser uma rubrica de uma terminologia controlada,
# em suma um DV_CODED_TEXT é a combinaão de uma CODE_PHRASE (um código) e a rubrica do termo,
# de um serviço de terminologias na linguagem em que foi autorado.

class DV_CODED_TEXT(DV_TEXT):


 defining_code = CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr) #a rubrica associada ao  'value'

 #construtor
 def __init__(self,defining_code = CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)):

  #   if(len(args)==1):
      self.defining_code = defining_code  #args[0]  #este self valora o atributo defining_code definido acima

 #  elif(len(args)>=1):
 #     self.defining_code=args[0]
 #     super(DV_CODED_TEXT, self).__init__()
 #     self.value = args[1]  #este self chama o atributo 'value' da superclasse DV_TEXT
                            #demais atributos da super classe DV_TEXT
 #     self.mappings = args[2]
 #     self.formatting = args[3]
 #     self.hyperlink = args[4]
 #     self.language = args[5]
 #     self.encoding = args[6]
 #     self.language = args[7]


  #retorna defining_code
 def getDefining_code(self):
     return self.defining_code

 #seta value e defining_code
 def setDefining_code(self,value, defining_code):
  self.defining_code = defining_code
  super(DV_CODED_TEXT,self).__init__()
  self.value= value

  #seta defining_code
 def setDefining_code(self, defining_code):
   self.defining_code = defining_code



  #retorna string value,defining_code
 def toString(self):
  return super(DV_CODED_TEXT,self).__init__().getValue()+self.defining_code

 #retorna code_string do atributo "defining_code"
 def getCode_string(self):
  return self.getDefining_code().getCodeString()


