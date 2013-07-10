# -*- coding: utf-8 -*-

__author__ = 'chrispess'

from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from urlparse import urlparse
from openehr.BASIC_TYPES import typeStr

    #referência objeto conforme Universal Resource Identifier (URI) standardt

class DV_URI(DATA_VALUE):

 #string representando o valor da URI
 value = typeStr

 #"espaço" em que a informação existe.
 # Simultaneamente especifica o espaço de
 # informação eo mecanismo para  acessar objetos nesse espaço.
 # ex: "ftp", "telnet", "mailto"
 scheme = typeStr

 path = typeStr

 fragment = typeStr

 query = typeStr

 #construtor
 def __init__(self, value):
#TODO: Matheus value nao pode ser um inteiro, para passar por enquanto estou
#fazendo um cast para string
     self.value = urlparse(str(value))

 #retorna scheme
 def scheme(self):
     return self.value.scheme

 #retorna path
 def path(self):
     return self.value.path


 #retorna fragment
 def fragment(self):
     return self.value.fragment


 #retorn query
 def query(self):
     return self.value.query

 #retorna value (full uri)
 def getValue(self):
     return self.value