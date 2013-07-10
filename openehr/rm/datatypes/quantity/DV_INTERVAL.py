 # -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.support.basic.Interval import Interval
from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.BASIC_TYPES import typeFloat

#classe genérica para definião de um intervalo.
# Usada para definir intervalos de datas, tempo, quantidades

class DV_INTERVAL(DATA_VALUE):

 #define um intervalo
 interval = Interval(typeFloat,typeFloat)


 #construtor
 #TODO: Matheus Dummy values to compile, olhar se é cabivel
 def __init__(self, lower=0.0, upper=0.0):
     self.interval.set_inf(lower)
     self.interval.set_sup(upper)


 #retorna o intervalo
 def getInterval(self):
     return self.interval


 #verifica se value está no intervalo
 def has(self, value):
     if(self.interval.has(value)==True):
         return True
     else:return False