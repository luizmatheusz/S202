from typing import Collection
from passageiro import Passageiro

class Corrida:
    def __init__(self, nota:int, distancia:float, valor:float, passageiro:Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
    
    # Funcao que transforma os parametros em dicionario, para o MongoDB entender
    def to_dict(self):
        return {
            "nota": self.nota,
            "distancia": self.distancia,
            "valor": self.valor,
            "passageiro": self.passageiro.to_dict()  # Convertendo passageiro para dicionário
        }