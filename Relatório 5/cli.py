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


class LivroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o titulo: ")
        autor = input("Entre com o autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preco: "))
        self.livro_model.create_livro(id, titulo, autor, ano, preco)

    def read_livro(self):
        id = input("Entre com o id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"ID: {livro['_id']}")
            print(f"Titulo: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preco: {livro['preco']}")

    def update_livro(self):
        id = input("Entre com o id: ")
        titulo = input("Entre com o titulo: ")
        autor = input("Entre com o autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preco: "))
        self.livro_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("Entre com o id: ")
        self.livro_model.delete_livro(id)
        
    def run(self):
        print("Welcome to the livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()