 # -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.quantity.DV_QUANTIFIED import DV_QUANTIFIED
from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT

#classe para definir o conceito de quantidades
# cujos valores são absolutos com respeito à origem...
# ex: datas e tempo

class DV_ABSOLUTE_QUANTITY(DV_QUANTIFIED):

 #precisão damedida
 accuracy = DV_AMOUNT

 #construtor
 def __init__(self, accuracy):
     self.accuracy = accuracy

 #adição de uma quantidade
 def add(self, a = DV_AMOUNT):
     pass


 #subtração de uma quantidade
 def subtract(self, a = DV_AMOUNT):
     pass

 #diferença de duas quantidades
 def diff(self, other):
     pass