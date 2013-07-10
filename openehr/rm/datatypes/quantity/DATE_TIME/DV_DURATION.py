# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from datetime import datetime
from openehr.rm.datatypes.quantity.DV_ABSOLUTE_QUANTITY import DV_ABSOLUTE_QUANTITY
from openehr.BASIC_TYPES import typeInt, INITIAL_DAY
#representa um período com respeito a um ponto no tempo não especificado
#não deve ser utilizado para representar pontos no tempo ou intervalos de tempo
class DV_DURATION(DV_ABSOLUTE_QUANTITY):

    #optou-se por adotar o 'ISO precise format', que não utiliza meses ou anos
    value = datetime

    #construtor
    ##TODO Matheus: dia nao pode ser 0 (typeInt), mudei para 1 (INITIAL_DAY) definindo-o em BASIC_TYPES.py
    def __init__(self,dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt):
        #define o objeto datetime, value
        #o valor '1' para mês e ano não deve ser levado em conta no cálculo
        # da duração, valores dumyes colocados devido à exigência do método
        # construtor 'datetime'

        self.value = datetime(1,1, dia, hora, minuto,segundo)


        #retorna a string referente à duração
    def getString(self):
        return str(self.value.day),':',str(self.value.hour),\
               ':',str(self.value.min),':',str(self.value.second)


    #retorna value
    def getDuration(self):
        return self.value

