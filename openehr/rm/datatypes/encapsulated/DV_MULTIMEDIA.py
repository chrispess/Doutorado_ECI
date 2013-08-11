# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from  openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeInt
from openehr.rm.datatypes.uri.DV_URI import DV_URI
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.datatypes.encapsulated.DV_ENCAPSULATED import DV_ENCAPSULATED
from PIL import Image

#especializaão da classse DV_ENCAPSULATED para audiovisual e tipos de biosinais.

class DV_MULTIMEDIA(DV_ENCAPSULATED):

    #texto para ser apresentado na linha  do display de multimídia
    alternate_text = typeStr

    # tipo de dado media advindo do openEHR code set "media types"
    media_type = CODE_PHRASE

    #tipo comprimido, um valor codificado a partir do openEHR code set "integrity check". "Void" significa que não houve compressão.
    compression_algorithm = CODE_PHRASE

    #checksum de verificação de integridade criptográfica
    integrity_check = []

    #tipo de verificação de integridade. um código advindo do openEHR code set "integrity check"
    integrity_check_algorithm = CODE_PHRASE

    #thumbnail para este item, se existir
    #para evitarcircularidade da especificação OpenEHR, que define thumbnail = DV_MULTIMEDIA,optou-se por utilizar
    #o tipo "Image"  da "python image library" ou PIL
    thumbnail = Image

    # referencia do tipo uri para informações externas como arquivos, entrada de base de dados, etc
    uri = DV_URI

    #os dados atualmente encontrados na URI, se estiverem inline
    data = []

    #tamanho em bytes dos dados presentes ou referenciados pela uri
    size = typeInt

    #construtor
    def __init__(self, *args):
     if(len(args)==2):
      self.media_type = args[0]
      self.size = args[1]
     elif(len(args)>=2):
         self.media_type = args[0]
         self.size = args[1]
         #todo definir os atributos que interessam
     else:pass

    #computado a  partir do valor de uri_atribute. True se o dado estava serializado externamente.
    # Uma cópia pode estar serializada internamente, o que faria "is_expanded" = True

     def is_external(self):
      if(self.uri <> None):
          return True
      else:return False



      #computado a  partir do valor do atributo data. True se o dado estava serializado internamente no EHR.

      def is_inline(self):
       if(self.data <> None):
          return True
       else:return False

     #computada a partir do valor de compression_algorith_atribute. True, se os dados estão serializados em formato comprimido
     def is_compressed(self):
         if(self.compression_algoritm <> None):
             return True
         else:return False


     #computada a partir do atributo integrity_check_algorithm. True se uma checagem de integridade foi computada
      def has_integrity_check(self):
          if(self.integrity_check_algorithm <> None):
              return True
          else:return False




