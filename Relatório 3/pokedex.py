from typing import Collection
import pymongo # type: ignore

class Pokedex:
    def __init__(self, db):
        self.db = db
        
    def getPokemonByHeight(self, height):
        return self.db.collection.find({"height": height})
    
    def getPokemonByWeaknessCount(self, n_weaknesses):
        return self.db.collection.find({"weaknesses": {"$size": n_weaknesses}})
    
    def getPokemonExcludingTypes(self, types):
        return self.db.collection.find({"type": {"$nin": types}})
    
    def getPokemonByEvolutionStatus(self, has_evolution):
        return self.db.collection.find({"next_evolution": {"$exists": has_evolution}})
    
    def getPokemonByAvgSpawns(self, avg_spawn):
        return self.db.collection.find({"avg_spawns": {"$gt": avg_spawn[0], "$lt": avg_spawn[1]}})
        
        