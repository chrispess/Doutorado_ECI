 # -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_QUANTIFIED import DV_QUANTIFIED
from openehr.BASIC_TYPES import typeFloat
from openehr.BASIC_TYPES import typeBool


class DV_AMOUNT(DV_QUANTIFIED):


#atributos mandatórios

    #precisão da medida, expressa como percentagem. o valor zero (0) indica
    # que a precisão não foi registrada
    accuracy = typeFloat

    #se verdadeira indica que a precisão foi registrada.
    accuracy_is_percent = typeBool


#construtor
def __init__(self, accuracy, accuracy_is_percent):
    self.accuracy = accuracy
    self.accuracy_is_percent = accuracy_is_percent

#retorna accuracy
def getAccuracy(self):
    return self.accuracy


#retorna accuracyPercent
def getAccuracyIsPercent(self):
    return self.accuracy_is_percent


#true se a percentagem é válida
def valid_percentage(self, value =typeFloat):
    if(value >=0.0 and value <= 0.0):
        return True
    else:return False




