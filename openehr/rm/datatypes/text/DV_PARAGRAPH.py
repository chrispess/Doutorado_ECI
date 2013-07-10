# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from  openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from  openehr.rm.datatypes.text.DV_TEXT import DV_TEXT


#classe que representa um composto de uma série de DV_TEXTs com
# o propósito de compor um parágrafo
class DV_PARAGRAPH(DATA_VALUE):


  items = DV_TEXT()


  #construtor

  def __init__(self,items = DV_TEXT()):
      self.items = items
      #exceção lançada para lista nula ou size()==0


  #retorna listade items
  def getItems(self):
      return self.items


  #seta lista de items
  def setItems(self,items = DV_TEXT()):
      self.items = items



