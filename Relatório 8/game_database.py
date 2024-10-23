from match import Match
from player import Player

class GameDatabase:
    def __init__(self, database):
        self.db = database
        
    def create_player(self, player:Player):
        query = "CREATE (:Player {name: $name, id: $id})"
        parameters = {"name": player.name, "id": player.id}
        self.db.execute_query(query, parameters)
        
    def create_match(self, match:Match):
        query = "CREATE (:Match {id: $id})"
        parameters = {"id": match.id}
        self.db.execute_query(query, parameters)    
        
    def node_match_player(self, match:Match, player:Player, goals):
        query = "MATCH (p:Player {id: $id_player}), (m:Match {id: $id_match}) CREATE (p)-[:Plays {goals: $goals}]->(m)"
        parameters = {"id_player": player.id, "id_match": match.id, "goals": goals}
        self.db.execute_query(query, parameters)
        
    def update_player_stats(self, match:Match, player:Player, goals):
        query = "MATCH (p:Player {id: $id_player})-[r:Plays]->(m:Match {id: $id_match}) SET r.goals = $goals"
        parameters = {"id_player": player.id, "id_match": match.id, "goals": goals}
        self.db.execute_query(query, parameters)
        
    def delete_player(self, player:Player):
        query = "MATCH (p:Player {id: $id}) DETACH DELETE p"
        parameters = {"id": player.id}
        self.db.execute_query(query, parameters)