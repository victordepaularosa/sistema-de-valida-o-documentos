# Importação das bibliotecas necessárias
from validate_docbr import CNPJ

class Doc_Cnpj:
    def __init__(self, documento) -> None:

        if self.validar(documento):
            self.cnpj = documento

        else:
            raise ValueError('CNPJ Inválido!!!!')

    def validar(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formato(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self) -> str:
        return self.formato()