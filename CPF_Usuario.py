# Importação das bibliotecas necessárias
from validate_docbr import CPF

class Doc_Cpf:
    def __init__(self, documento) -> None:

        if self.validar(documento):
            self.cpf = documento
        
        else:
            raise ValueError('CPF Inválido!!!!')

    def validar(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formato(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self) -> str:
        return self.formato()