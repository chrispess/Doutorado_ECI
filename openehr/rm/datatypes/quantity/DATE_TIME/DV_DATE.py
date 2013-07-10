# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from datetime import datetime
from datetime import date
from openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from openehr.BASIC_TYPES import typeInt

#representa um ponto absoluto no tempo, conforme ocalendário gregoriano
# e especificado como um dia. semântica dada por ISO 8601
class DV_DATE(Dv_TEMPORAL):

    #ISO 8601 data string
    value = datetime

    #TODO: Matheus mudei ano inicial de 0000 para 0001, pois este é o
    #ano inicial suportado pela biblioteca
    #TODO: date.fromordinal recebe um inteiro como parametro e não um date
    #time, ordinal deve ser >= 1
    pontoDeOrigem = date.fromordinal(1)

    #construtor
    def __init__(self,year = typeInt, month = typeInt, day = typeInt ):
        self.value = datetime(year, month, day)

    #retorna objeto date
    def getDate(self):
        return self.value

    #retorna a string associada à data no formato dd-mm-nn
    def getDateStr(self):
        return self.value.strftime('%d-%m-%Y')


    #valor numérico da data em dias desde a origem do calendário 1/1/0000
    def magnitude(self):
        return date.toordinal(self.getDate())

    #retorna string associada à data
    def getString(self):
        return str(self.value.day),'-',str(self.value.month),'-',str(self.value.year)

