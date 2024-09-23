from typing import Collection

class Passageiro:
    def __init__(self, nome:str, documento:str):
        self.nome = nome
        self.documento = documento
        
    # Funcao que transforma os parametros em dicionario, para o MongoDB entender
    def to_dict(self):
        return {
            "nome": self.nome,
            "documento": self.documento
        }
        