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
        
    def update_player_name(self, player:Player, name):
        query = "MATCH (p:Player {id: $id_player}) SET p.name = $name"
        parameters = {"id_player": player.id, "name": name}
        self.db.execute_query(query, parameters)
        
    def update_player_stats(self, match:Match, player:Player, goals):
        query = "MATCH (p:Player {id: $id_player})-[r:Plays]->(m:Match {id: $id_match}) SET r.goals = $goals"
        parameters = {"id_player": player.id, "id_match": match.id, "goals": goals}
        self.db.execute_query(query, parameters)
        
    def delete_player(self, player:Player):
        query = "MATCH (p:Player {id: $id}) DETACH DELETE p"
        parameters = {"id": player.id}
        self.db.execute_query(query, parameters)
        
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_match(self, id_match):
        query = "MATCH (m:Match {id: $id_match})<-[r:Plays]-(p:Player) RETURN m.id AS id_match, p.name AS player_name, p.id AS id_player, r.goals AS goals"
        parameters = {"id_match": id_match}
        results = self.db.execute_query(query, parameters)
        
        if results:
            match_info = {
                "id_match": results[0]["id_match"],
                "players": []
            }
            for result in results:
                player_info = {"id": result["id_player"], "name": result["player_name"], "goals": result["goals"]}
                match_info["players"].append(player_info)
            return match_info
        else:
            return None  # Caso a partida não seja encontrada
        
    def get_player_match_history(self, id_player):
        query = "MATCH (p:Player {id: $id_player})-[r:Plays]->(m:Match) RETURN m.id AS id_match, p.name AS player_name, p.id AS id_player, r.goals AS goals"
        parameters = {"id_player": id_player}
        results = self.db.execute_query(query, parameters)
        
        if results:
            player_info = {
                "id_player": results[0]["id_player"],
                "matches": []
            }
            for result in results:
                match_info = {"id": result["id_match"], "goals": result["goals"]}
                player_info["matches"].append(match_info)
            return player_info
        else:
            return None  # Caso o jogador não seja encontrado