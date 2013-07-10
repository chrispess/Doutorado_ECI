# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.BASIC_TYPES import typeInt


class DV_ENCAPSULATED(DATA_VALUE):

 #esquema de caracteres em que é encodado (default: unicode com UTF-8)
 charset = CODE_PHRASE
 # (opcional) indicador opcional da linguagem em que os dados são  escritos.
 language = CODE_PHRASE
 #tamanho original em bytes
 size = typeInt

 #construtor
 def __init__(self,charset,language):
     self.charset = charset
     self.language = language


 #retorna charset
 def getcharset(self):
     return self.charset

 #retorna language
 def getLanguage(self):
     return self.language


 #retorna string charset
 def getcharset(self):
     return self.charset.tostring()

 #retorna language
 def getLanguage(self):
     return self.language.tostring()

 #result = alternate_text(uri) /?????verificar sentido do método
 def as_string(self):
     pass