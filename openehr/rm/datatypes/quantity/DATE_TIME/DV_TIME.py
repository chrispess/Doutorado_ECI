# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from  openehr.rm.datatypes.quantity.DATE_TIME.DV_TEMPORAL import Dv_TEMPORAL
from  openehr.BASIC_TYPES import typeStr
import datetime

class DvTime(Dv_TEMPORAL):

    #ISO 8601 time string
    #value = typeStr

    #objeto datetime.time
    time = datetime

    #construtor com value representando: hh:mm:ss
    def __init__(self, hora, minuto, segundo):
        self.time = datetime.time(hora, minuto, segundo)

    #retorna o string no formato hh:mm:ss
    def getValue(self):
       return self.time.strftime('%H:%M:%S')


    #retorna valor numérico do tempo em segundos desde o início do dia
    def magnitude(self):
        k = self.getValue()
        x = self.time.strftime(k.split(',')[0], '%H:%M:%S')
        z = datetime.timedelta(hora=x.tm_hour, minutos=x.tm_min,segundos=x.tm_sec).total_seconds()
        return z

    #retorna string associada à time
    def getString(self):
        return str(self.time.hour),':',str(self.time.min),':',str(self.time.second)