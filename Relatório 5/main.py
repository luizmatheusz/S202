from database import Database
from livroModel import LivroModel
from cli import LivroCLI

db = Database(database='Relatório_5', collection='Livros')
livroModel = LivroModel(database=db)

# livroModel.create_livro(id="1", titulo="abc", autor="def", ano=2019, preco=10.5)
# livroModel.update_livro(id="1", titulo="ddd", autor="hhh", ano=2000, preco=17.5)
# livroModel.read_livro_by_id(id="1")
# livroModel.delete_livro(id="1")

livroCLI = LivroCLI(livro_model=livroModel)
livroCLI.run()