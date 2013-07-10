# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.HISTORY.HISTORY import HISTORY
from openehr.rm.composition.content.entry.CARE_ENTRY import CARE_ENTRY
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DATE_TIME import DV_DATE_TIME
from openehr.BASIC_TYPES import typeInt
from openehr.BASIC_TYPES import INITIAL_DAY


class OBSERVATION(CARE_ENTRY):

 #Mandatório. os dados da  observação, na forma de um
 # histórico de valores de complexidade variável
 ###TODO MATHEUS-11-04-13: Retirei o origin = do parâmetro, a classe HISTORY não espera este parâmetro
 data = HISTORY(DV_DATE_TIME(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt))

 #opcional. Salva o estado do sujeito
 #da observação duranto processo da observação
 #na forma de um histórico separado de valores
 #que podem ser de qualquer complexidade
 ###TODO MATHEUS-11-04-13: Retirei o origin = do parâmetro, a classe HISTORY não espera este parâmetro
 state = HISTORY(DV_DATE_TIME(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt))

 #construtor
 def __init__(self, *args):
     if(len(args)==1):
      self.data = args[0]
     elif(len(args)==2):
      self.data = args[0]
      self.state = args[1]


