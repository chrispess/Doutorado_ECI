# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeInt
from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.rm.datatypes.quantity.PROPORTION_KIND import PROPORTION_KIND


class DV_PROPORTION(DV_AMOUNT):

   #numerador da razão
   numerator = typeFloat

   #denominador da razão
   denominator = typeFloat

   #indica o tipo da proporção
   type = PROPORTION_KIND

   #expressa a precisão em termos decasas decimais. 0 -> integral,
   # -1 -> qualquer número decasas decimais
   precision = typeInt


   #construtor
   def __init__(self, numerator, denominator, type, precision):
       self.numerator = numerator
       self.denominator = denominator
       self.type = type
       self.precision = precision



   #retorna numerator
   def getNumerator(self):
       return self.numerator

   #retorna denominator
   def getDenominator(self):
       return self.denominator

   #retorna type
   def getType(self):
       return self.type

   #retorna precision
   def getPrecision(self):
       return self.precision


   #seta numerator
   def setNumerator(self,numerator):
       self.numerator = numerator

   #seta denominator
   def setDenominator(self, denominator):
       self.denominator = denominator

   #seta type
   def setType(self, type):
       self.type = type

   #seta precision
   def setPrecision(self, precision):
       self.precision = precision

   #true se numerator e denominator são inteiros (preciion = 0)
   def is_integral(self):
       if (float(self.numerator) - int(self.numerator)==0 and float(self.denominator) - int(self.denominator)==0 ):
           return True
       else:return False

   #retorna magnitude representada pela razão
   def magnitude(self):
       return self.numerator/self.denominator


