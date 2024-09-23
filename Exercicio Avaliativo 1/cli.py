from bson import ObjectId
from passageiro import Passageiro
from corrida import Corrida
from motorista import Motorista

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_DAO):
        super().__init__()
        self.motorista_DAO = motorista_DAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        m_corridas = []
        flag = 's'
        
        while flag != 'n':
            print("\nCriando passageiro:")
            p_nome = input("Entre com o nome: ")
            p_documento = input("Entre com o documento: ")
            p = Passageiro(nome=p_nome, documento=p_documento)
            
            print("\nCriando corrida:")
            c_nota = int(input("Entre com a nota: "))
            c_distancia = float(input("Entre com a distancia: "))
            c_valor = float(input("Entre com o valor: "))
            c_passageiro = p
            c = Corrida(nota=c_nota, distancia=c_distancia, valor=c_valor, passageiro=c_passageiro)
            m_corridas.append(c.to_dict())
            flag = input("Deseja adicionar mais uma corrida? ('s': sim, 'n': nao) ")
            
        print("\nCriando motorista:")
        m_nota = int(input("Entre com a nota: "))
        m = Motorista(nota=m_nota, corridas=m_corridas)
        self.motorista_DAO.create_motorista(m)

    def read_motorista(self):
        id = ObjectId(input("Entre com o id: "))
        self.motorista_DAO.read_motorista_by_id(id)

    def update_motorista(self):
        id = ObjectId(input("Entre com o id: "))
        nota = int(input("Entre com a nota: "))
        self.motorista_DAO.update_motorista(id, nota)

    def delete_motorista(self):
        id = ObjectId(input("Entre com o id: "))
        self.motorista_DAO.delete_motorista(id)
        
    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()