# Importação das bibliotecas necessárias
from CPF_Usuario import *
from CNPJ_empresa import *

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)

        if len(documento) == 11:
            return Doc_Cpf(documento)

        elif len(documento) == 14:
            return Doc_Cnpj(documento)

        else:
            raise ValueError('Documento Inválido!!!!')