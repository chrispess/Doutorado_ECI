# -*- coding: utf-8 -*-

__author__ = 'chrispess'


from openehr.rm.datatypes.basic.DATA_VALUE import DATA_VALUE
from openehr.rm.datatypes.uri.DV_URI import DV_URI
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID

from openehr.BASIC_TYPES import typeStr

#classe para representar qualquer
# tipo de item de texto atômico, codificado ou não codificado

class DV_TEXT(DATA_VALUE):

  #um item de texto que pode conter um arranjo de caracteres como palavras,
  # sentenças (um  DV_TEXT pode conter mais de uma palavra) com hyprlinks, inclusive.
  value = typeStr

  #termos de outras terminologias que mais se aproximam do termo expresso
  mappings = []

  #string formatado na forma "name:value;name:value...",
  # por exemplo "font-weight:bold; font-family:Arial; font "
  formatting = typeStr

  #link opcional
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  hyperlink = DV_URI(value = typeStr)

  #indicador opcional da linguagem em que 'value' é escreto
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  language = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)

  #nome do eschema de caracteres em que 'value' é encodado
  #TODO Matheus: Dummie value attribute, setar Default ou adicionar aqui
  encoding = CODE_PHRASE(teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr)



#construtor
  def __init__(self, *args):
      if(len(args)==1):
       self.value = args[0]
      elif(len(args)>1):
       self.value = args[0]
       self.mappings = args[1]
       self.formatting = args[2]
       self.hyperlink = args[3]
       self.language = args[4]
       self.encoding = args[5]


  #retorna string associada ao 'value'
  def getValue(self):
      return self.value


  #retorna mappings
  def getMappings(self):
      return self.mappings


  #retorna formatting
  def getFormatting(self):
      return self.formatting


  #retorna hiperlink
  def getHyperlink(self):
      return self.hyperlink


  #retorna language
  def getLanguage(self):
      return self.language


  #retorna encoding
  def getEncoding(self):
      return self.encoding


   #verifica se são iguais
   #value,mapping,formatting,hyperlink, language, encoding
  def equals(self, other):
      if(self.value == other.getValue() & self.mapping == other.getMapping() & self.formatting == other.getFormatting() & self.hyperlink == other.getHyperlink() & self.language == other.getLanguage()& self.encoding == other.getEncoding()):
          return True
      else:return False



  #seta value
  def setValue(self, value):
      self.value = value

  #seta mapping
  def setMappings(self, mappings):
      self.mappings = mappings


  #seta formatting
  def setFormatting(self, formatting):
      self.formatting = formatting

  #seta hyperlink
  def setHyperlink(self, hyperlink):
      self.hyperlink = hyperlink


  #seta language
  def setLanguage(self,language):
      self.language = language


  #seta encoding
  def setEncoding(self, encoding):
      self.encoding = encoding

