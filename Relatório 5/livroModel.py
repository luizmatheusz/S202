from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_livro(self, id:str, titulo:str, autor:str, ano:int, preco:float):
        try:
            res = self.db.collection.insert_one({"_id": id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Livro created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None
        
    def read_livro_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": id})
            print(f"Livro found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading livro: {e}")
            return None

    def update_livro(self, id: str,titulo:str, autor:str, ano:int, preco:float):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            print(f"Livro updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print(f"Livro deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting livro: {e}")
            return None