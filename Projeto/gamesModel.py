from pymongo import MongoClient
from bson.objectid import ObjectId
from models.player import Player
from models.team import Team
from models.game import Game

class GamesModel:
    def __init__(self, db_players, db_teams, db_games):
        self.db_players = db_players
        self.db_teams = db_teams
        self.db_games = db_games

    def create_player(self, player: Player):
        try:
            res = self.db_players.collection.insert_one({"_id": player.id, "name": player.name, "position": player.position, "team": player.team.to_dict(), "img": player.img})
            print(f"Player created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None
        
    def create_team(self, team: Team):
        try:
            res = self.db_teams.collection.insert_one({"_id": team.id, "name": team.name, "abbr": team.abbr, "roster": []})
            print(f"Team created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None
        
    def create_game(self, game: Game):
        try:
            res = self.db_games.collection.insert_one({"_id": game.id, "home_team": game.home_team, "away_team": game.away_team, "home_score": game.home_score, "away_score": game.away_score, "total_score": game.total_score, "week": game.week, "winner": game.winner})
            print(f"Game created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None
        
    def read_player_by_id(self, id: str):
        try:
            res = self.db_players.collection.find_one({"_id": id})
            print(f"Player found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading livro: {e}")
            return None
        
    def read_team_by_abbr(self, abbr: str):
        try:
            res = self.db_teams.collection.find_one({"abbr": abbr})
            team = Team(id=res['_id'], name=res['name'], abbr=res['abbr'])
            print(f"Team found: {team.show_info()}")
            return team
        except Exception as e:
            print(f"An error occurred while reading team: {e}")
            return None
        
    def read_team_by_id(self, id: str):
        try:
            res = self.db_teams.collection.find_one({"_id": id})
            print(f"Team found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading livro: {e}")
            return None
        
    def read_game_by_id(self, id: str):
        try:
            res = self.db_games.collection.find_one({"_id": id})
            print(f"Game found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading livro: {e}")
            return None

    def update_player(self, player: Player):
        try:
            res = self.db_players.collection.update_one({"_id": player.id}, {"$set": {"name": player.name, "position": player.position, "team": player.team, "img": player.img}})
            print(f"Player updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating livro: {e}")
            return None
        
    def update_team(self, team: Team):
        try:
            res = self.db_teams.collection.update_one({"_id": team.id}, {"$set": {"name": team.name, "abbr": team.abbr, "roster": []}})
            print(f"Team updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating livro: {e}")
            return None
        
    def update_game(self, game: Game):
        try:
            res = self.db_games.collection.update_one({"_id": game.id}, {"home_team": game.home_team, "away_team": game.away_team, "home_score": game.home_score, "away_score": game.away_score, "total_score": game.total_score, "week": game.week, "winner": game.winner})
            print(f"Game updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating livro: {e}")
            return None

    def delete_player(self, id: str):
        try:
            res = self.db_players.collection.delete_one({"_id": id})
            print(f"Player deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting livro: {e}")
            return None
        
    def delete_team(self, id: str):
        try:
            res = self.db_teams.collection.delete_one({"_id": id})
            print(f"Team deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting team: {e}")
            return None
        
    def delete_game(self, id: str):
        try:
            res = self.db_games.collection.delete_one({"_id": id})
            print(f"Game deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting game: {e}")
            return None