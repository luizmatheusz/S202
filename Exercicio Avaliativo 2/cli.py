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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome: ")
        ano_nasc = input("Entre com o ano de nascimento: ")
        cpf = input("Entre com o CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Entre com o nome: ")
        teacher = self.teacher_crud.read(name)
        if teacher:
            print(f"Nome: {teacher['name']}")
            print(f"Ano de nascimento: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")

    def update_teacher(self):
        name = input("Entre com o nome: ")
        newCpf = input("Entre com o novo CPF: ")
        self.teacher_crud.update(name, newCpf)

    def delete_teacher(self):
        name = input("Entre com o nome: ")
        self.teacher_crud.delete(name)
        
    def run(self):
        print("Welcome to the teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()