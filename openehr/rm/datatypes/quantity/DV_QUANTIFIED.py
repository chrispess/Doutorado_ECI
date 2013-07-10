 # -*- coding: utf-8 -*-
__author__ = 'chrispess'

#superclasse abstrata que define o conceito de valores quantificáveis, ordenados e com precisão na magnitude

from openehr.rm.datatypes.quantity.DV_ORDERED import DV_ORDERED
from openehr.BASIC_TYPES import typeStr


class DV_QUANTIFIED(DV_ORDERED):



#atributos mandatórios

 magnitude_status = typeStr


#construtor
 def __init__(self, *args):
     #construtor com magnitude_status
     if(len(args)==1):

         self.magnitude_status = args[0]

     #construtor vazio
     else:pass



#retorna magnitude_status
def getMagnitudeStatus(self):
    return self.magnitude_status


#verifica o atributo magnitude_status
def valid_magnitud_status(self, result=False):
    if (self.magnitude_status == "=" or self.magnitude_status == "<"
        or self.magnitude_status == ">" or self.magnitude_status == "<="
        or self.magnitude_status == ">=" or self.magnitude_status == "~"):

        result =True
        return result


