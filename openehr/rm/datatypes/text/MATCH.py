 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


#classe com as informaões de match para ser usada em conjunto
# com a classe TERM_MAPPING

from openehr.BASIC_TYPES import typeStr

class MATCH(object):

 NARROWER= "<"
 EQUIVALENT = "="
 BROADER = ">"
 UNKNOWN = "?"

 value = typeStr

 #construtor
 def __init__(self, value):
     self.value = value


 #metodo que verifica a igualdade
 #def equals(self, match):


 #verifica se match equivale a narrow

 def narrower(self, match):
     if(self.NARROWER == match):
         return True
     else:return False

 #verifica se match equivale a equivalent
 def equivalent(self, match):
     if(self.EQUIVALENT == match):
         return True
     else:return False


 #verifica se match equivale a broader
 def broader(self, match):
     if(self.BROADER == match):
         return True
     else:return False


 #verifica se match equivale a unknown
 def unknown(self, match):
     if(self.UNKNOWN == match):
         return True
     else:return False

 #verifica se match é um caracter válido
 def is_valid_match_code(self,c):
     if(c == ">" or c == "<" or c == "=" or c == "?"):
         return True
     else:return False


