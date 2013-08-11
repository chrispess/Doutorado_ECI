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
