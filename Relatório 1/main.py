class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}.'

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f'O aluno {self.nome} está presente.'

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        txt = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n'
        for aluno in self.alunos:
            txt += aluno.presenca() + '\n'
        return txt

professor = Professor("Roberto")
aluno1 = Aluno("Luiz")
aluno2 = Aluno("Matheus")
aluno3 = Aluno("Ana")
aula = Aula(professor, "Computação Gráfica")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.adicionar_aluno(aluno3)
print(aula.listar_presenca())