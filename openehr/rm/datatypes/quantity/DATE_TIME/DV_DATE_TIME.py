# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from datetime import datetime
from datetime import date
from openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from openehr.BASIC_TYPES import typeInt, INITIAL_DAY

#usado pararepresentar a duração em horas, minutos ou segundos. Não deveser
# utilizado para representar pontos ou intervalos de tempo
class DV_DATE_TIME(Dv_TEMPORAL):

    #data e tempo na forma YYYY-mm-dd  HH:mm:ss
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


    #retorna a duração em segundos
    def magnitude(self):
        strDuration = str(self.value.day),':',str(self.value.hour),\
                      ':',str(self.value.min),':',str(self.value.second)

        duram = [86400, 3600, 60, 1]

        return sum([a*b for a,b in zip(duram, map(int,strDuration.split(':') ))])



     #retorna a string referente à duração
    def getString(self):
        return str(self.value.day),':',str(self.value.hour),\
               ':',str(self.value.min),':',str(self.value.second)