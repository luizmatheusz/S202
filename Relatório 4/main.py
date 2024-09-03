from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
# db.resetDatabase()

product_analyzer = ProductAnalyzer(db)
product_analyzer.total_vendas()
product_analyzer.produto_mais_vendido()
product_analyzer.cliente_mais_gastou()
product_analyzer.produtos_acima_um()