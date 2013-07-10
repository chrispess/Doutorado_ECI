# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.support.identification.OBJECT_ID  import OBJECT_ID
from openehr.BASIC_TYPES import typeStr
#casse que permite criar uma referência para outro objeto, que pode existir localmente ou em outro local
class OBJECT_REF():

 #id unico de um objeto. != null
 #TODO: MATHEUS, alterei o parâm
 id = OBJECT_ID(value = typeStr)

 #namespace a que o identificador pertence no contexto do sistema. != null
 #ex: "terminology", "demographic"
 namespace = typeStr

 #nome da classe do objeto a que o identificador se refere. !=null
 type = typeStr

 # construtor
 def __init__(self, id, namespace, type):
     self.id = id
     self.namespace = namespace
     self.type = type


 #métodos get

   # retorna id
     def getId():
         return self.id

   # retorna namespace
     def getNamespace():
         return self.namespace

   # retorna type
     def getType():
         return self.type



 #verifica igualdade comparando o objeto com outro pasado como parâmetro
 def equal(self, other):
     if(self == other):
         return True
     else:return False



 #retorna o string representativo do objeto
 def toString(self):
         object_ref = []
         object_ref.append(self.id)
         object_ref.append(self.namespace)
         object_ref.append(self.type)
         return object_ref


 #seta namespace
 def setNamespace(self, namepace):
     self.namespace = namepace


 #seta type
 def setType(self, type):
     self.type = type






