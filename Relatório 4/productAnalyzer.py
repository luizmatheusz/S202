from typing import Collection
import pymongo # type: ignore
from helper.writeAJson import writeAJson

class ProductAnalyzer():
    def __init__(self, db):
        self.db = db
        
    def total_vendas(self):
        return writeAJson(self.db.collection.aggregate([
            {"$group": {"_id": "$data_compra", "total": {"$sum": 1}}},
        ]), "total_vendas")
    
    def produto_mais_vendido(self):
        return writeAJson(self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]), "produto_mais_vendido")
    
    def cliente_mais_gastou(self):
        return writeAJson(self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]), "cliente_mais_gastou")
    
    def produtos_acima_um(self):
        return writeAJson(self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total": {"$gt": 1}}}
        ]), "produtos_acima_um")