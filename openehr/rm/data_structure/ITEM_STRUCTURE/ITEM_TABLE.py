# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.data_structure.DATA_STRUCTURE import DATA_STRUCTURE
from openehr.rm.data_structure.ITEM_STRUCTURE.REPRESENTATION.CLUSTER import CLUSTER


#data structure do tipo table.
#No caso do OpenEHR, cria uma lista de Clusters

class ITEM_TABLE(DATA_STRUCTURE):

  #representação de uma tabela como uma lista de clusters
  table = []

  #construtor
  def __init__(self, table = []):
     self.table = table


  #insere uma linha (um CLUSTER) na tabela
  def appendRows(self, row = CLUSTER):
   self.table.append(row)

  #retorna o número de linhas
  def rowCount(self):
      return self.table.len()

  #retorna o número de  colunas
  def columnCount(self):
   self.table[0].getSize()

  #retorna um

  #retorna uma lista com o nome das linhas
  #def rowNames(self):

  #retorna umalista com o nome das colunas
  #def columnNames(self):

  #retorna a í-ésima linha
  #def ithRow(self):

