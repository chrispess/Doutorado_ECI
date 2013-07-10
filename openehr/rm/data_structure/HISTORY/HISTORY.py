# -*- coding: utf-8 -*-
__author__ = 'chrispess'
from openehr.rm.data_structure.HISTORY.EVENT import EVENT
from openehr.rm.data_structure.DATA_STRUCTURE import DATA_STRUCTURE
from openehr.rm.data_structure.ITEM_STRUCTURE.ITEM_STRUCTURE import ITEM_STRUCTURE
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION
from openehr.BASIC_TYPES import typeInt, INITIAL_DAY

#objeto raiz de uma  história linear
class HISTORY(DATA_STRUCTURE):

 #tempo da origem desse evento do tipo history
 #TODO Matheus: dia nao pode ser 0 (typeInt), mudei para 1 (INITIAL_DAY) definindo-o em BASIC_TYPES.py
 origin = DV_DATE_TIME(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt)

 #os eventos dessa serie. lista de eventos
 events = []

 #periodo entre amostras neste segmento (SE for periódico)
 period = DV_DURATION

 #duração da história inteira
 duration = DV_DURATION


 #opcional. texto ou imagem que
 # sumariza a história inteira
 summary = ITEM_STRUCTURE

 #construtor
 def __init__(self,*args):
      if(len(args)==1):
          #origem
          self.origin = args[0]
      elif(len(args)==2):
          #origem
          self.origin = args[0]
          #eventos
          self.events = args[1]
      else:
      #origem
          self.origin = args[0]
          #eventos
          self.events = args[1]
          #periodo
          self.period = args[2]
          #duração
          self.duration = args[3]
          #sumário
          self.summary = args[4]



 #indica quando a history é periódica
 def is_periodic(self):
     if self.period == None:
         return True


#seta duração
##TODO Matheus: dia nao pode ser 0 (typeInt), mudei para 1 (INITIAL_DAY) definindo-o em BASIC_TYPES.py
def setDuration(self, duration = DV_DURATION(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt) ):
      self.duration = duration


  #seta período
  ##TODO Matheus: dia nao pode ser 0 (typeInt), mudei para 1 (INITIAL_DAY) definindo-o em BASIC_TYPES.py
def setPeriod(self,period = DV_DURATION(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt) ):
      self.period = period


#seta summary
def setSummary(self,summary = ITEM_STRUCTURE ):
    self.summary = summary


#adiciona eventos na lista
def appendEvents(self, event = EVENT):
    self.events.append(event)


