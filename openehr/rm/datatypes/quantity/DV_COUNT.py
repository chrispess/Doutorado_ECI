# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.datatypes.quantity.DV_AMOUNT import DV_AMOUNT
from openehr.BASIC_TYPES import typeInt

#classe usada para representar coisas contáveis, como número de coigarros fumados um dia,
# passos, etc
class DV_COUNT(DV_AMOUNT):

    #representa a magnitude numérica da quantidade
    magnitude = typeInt

    #construtor
    def __init__(self, magnitude):
        self.magnitude = magnitude



    #retorna magnitude
    def getMagnitude(self):
        return  self.magnitude


    #seta magnitude
    def setMagnitude(self):
        return self.magnitude





