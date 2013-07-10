 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeStr

class DV_QUANTITY(DV_AMOUNT):

    #atributos

    #grandeza
    magnitude = typeFloat

    #precisão em termos de valores decimais.
    # 0 implica quantidade integral e -1 implioca nenhum limite
    precision = typeInt

    # String expressando unidades como kg/m2, mm[Hg], km/h,...
    units = typeStr


    #construtor

    def __init__(self, magnitude, units, precision):

     self.magnitude = magnitude
     self.units = units
     self.precision = precision


    #métodos

    #retorna magnitude
    def getMagnitude(self):
     return self.magnitude


    #retorna units
    def getUnits(self):
     return self.units


    #retorna precisão
    def getPrecision(self):
     return self.precision

    #seta precisão
    def setPrecision(self, precision):
     self.precision = precision

    #seta magnitude
    def setMagnitude(self, magnitude):
     self.magnitude = magnitude



    #verifica se a precisão = 0
    def is_integral(self):
        if self.precision == 0:
         return True
        else:return False

    #


