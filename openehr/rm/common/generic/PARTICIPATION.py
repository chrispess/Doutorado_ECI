# -*- coding: utf-8 -*-
__author__ = 'chrispess'

from openehr.rm.common.generic.PARTY_PROXY import PARTY_PROXY
from openehr.rm.datatypes.text.DV_TEXT import DV_TEXT
from openehr.rm.datatypes.text.DV_CODED_TEXT import DV_CODED_TEXT
from openehr.rm.datatypes.text.CODE_PHRASE import CODE_PHRASE
from openehr.rm.support.identification.TERMINOLOGY_ID import TERMINOLOGY_ID
from openehr.BASIC_TYPES import typeStr
from openehr.BASIC_TYPES import typeInt, INITIAL_DAY
from openehr.rm.datatypes.quantity.DATE_TIME.DV_DURATION import DV_DURATION

class PARTICIPATION(object):

    #[1..1] o id de participantes na atividade
    performer = PARTY_PROXY()

    #[1..1] a função do participante. pode ser codificado
    #TODO Matheus: DV_TEXT nao receve "value" como parametro e sim uma tupla.
    ###TODO MATHEUS-11-04-13: Retirei value =, a classe DV_TEXT não espera este parâmetro
    function = DV_TEXT(typeStr)

    #[1..1] o modo em que houve a interação.
    # ex: presencial, por telefone, email, etc
    mode = DV_CODED_TEXT(CODE_PHRASE( teminology_id = TERMINOLOGY_ID(name=typeStr, version_id=typeStr), code_string=typeStr))

    # o intervalo de tempo durante o qual a participação ocorreu
    # optou-se por utilizar a classe DV_DURATION para esta representação
    # ##TODO Matheus: dia nao pode ser 0 (typeInt), mudei para 1 (INITIAL_DAY) definindo-o em BASIC_TYPES.py
    time = DV_DURATION(dia = INITIAL_DAY, hora = typeInt, minuto = typeInt , segundo = typeInt)

    #construtor
    def __init__(self, *args):
        if(len(args)==3):
           self.performer = args[0]
           self.function = args[1]
           self.mode = args[2]

        elif(len(args)==4):
         self.performer = args[0]
         self.function = args[1]
         self.mode = args[2]
         self.time = args[3]

