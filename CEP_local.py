# Importação das bibliotecas necessárias
import requests

class Busca_endereco:

    def __init__(self, cep) -> None:
        cep = str(cep)

        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP Inválido!!!')

    def __str__(self) -> str:
        return self.format_cep()

    def cep_valido(self, cep):

        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f'{self.cep[0:5]}-{self.cep[5:]}'
    
    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        requisicao = requests.get(url)
        dados = requisicao.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )