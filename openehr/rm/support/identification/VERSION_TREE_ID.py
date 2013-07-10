# -*- coding: utf-8 -*-
__author__ = 'chrispess'
from openehr.BASIC_TYPES import typeStr
class VERSION_TREE_ID:

# formato lexico
# value: trunkVersion ['.' branchNumber '.' branchVersion]
# trunk_version: {digito}+
# branch_number: {digito}+
# branch_version: {digito}+
# digit:          [0 - 9]

    #string com a formado identificador
    value = typeStr



    #construtor
    def __init__(self, value = typeStr):
        self.value =  value



    #retorna trunkVersion
    def trunk_version(self):
        return self.trunkVersion



    #retorna branchNumber
    def branch_number(self):
        return self.branchNumber



    # retorna branchVersion
    def branch_version(self):
        return self.branchVersion



    #retorna true se o identificador representa um branch
    def is_branch(self):
        if(self.branchVersion != None):
            return True
        else:return False


    # retorna true se é a primeira cópia numa árvore de versões
    def is_first(self):
        if(self.trunkVersion == "1"):
            return True
        else:return False



    #retorna value
    def getValue(self):
        return self.value


    #verifica igualdade comparando o objeto com outro passado como parâmetro
    def equal(self, other):
        if(self.value == other.value):
            return True
        else:return False


