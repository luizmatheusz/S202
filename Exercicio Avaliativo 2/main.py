from database import Database
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

# Conectando ao banco de dados
db = Database("bolt://3.239.245.61:7687", "neo4j", "acquisition-polarity-rehabilitation")

teacher_crud = TeacherCRUD(database=db)

# Questão 3
print("Questão 3:")
print("\nb) Criando um professor:")
teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="182.052.396-66")

print("\nc) Pesquisando um professor:")
teacher = teacher_crud.read(name="Chris Lima")
print(f"Nome: {teacher['name']}, ano de nascimento: {teacher['ano_nasc']}, CPF: {teacher['cpf']}")

print("\nd) Alterando o CPF de um professor:")
teacher_crud.update(name="Chris Lima", newCpf="162.052.777-77")

teacherCLI = TeacherCLI(teacher_crud=teacher_crud)
teacherCLI.run()