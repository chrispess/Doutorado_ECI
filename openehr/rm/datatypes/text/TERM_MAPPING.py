 # -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeChar
from openehr.BASIC_TYPES import typeStr


class TERM_MAPPING():

  # [1..1] o termo alvo do mapeamento
  target = CODE_PHRASE("teminology_id", "code_string")

  #[1..1] correspondência relativa do termo alvo com respeito ao item de texto mapeado.
  # os resultados podem ter os seguintes significados:
  # '>': o mapeamento é mais amplo. ex: texto original = "arbovirus infection"
  # e o target = 'viral infection'
  # '=': mapeamento éequivalente ao termo original
  # '<': o mapeamento é menos amplo. ex: textooriginal = 'diabetes'
  # e o target = 'diabetes mellitus'
  #'?': desconhecido
  match = typeChar

  #[1..1] proposito do mapeamento. ex: "interoperabilidade", "automação de data mining"...
  purpose =  DV_CODED_TEXT(defining_code = CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))


  #construtor
  def __init__(self,target,match,purpose):
      self.target =target
      self.match = match
      self.purpose = purpose

  #retorna target
  def getTarget(self):
      return self.target


  #retorna Match
  def getMatch(self):
      return self.match


  #retorna purpose
  def getPurpose(self):
      return self.purpose

  #verifica se match == "<"
  def narrower(self,match):
      if(self.match.narrower(match)==True):
          return True
      else:return False

  #verifica se match == ">"
  def broader(self,match):
      if(self.match.broader(match)==True):
          return True
      else:return False

  #verifica se match == "="
  def equivalent(self,match):
      if(self.match.equivalent(match)==True):
          return True
      else:return False

  #verifica se match == "?"
  def unknown(self,match):
      if(self.match.unknown(match)==True):
          return True
      else:return False

