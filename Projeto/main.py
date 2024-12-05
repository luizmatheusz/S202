from database import Database
from gamesModel import GamesModel
from cli import GamesCLI

db_players = Database(database='Projeto', collection='Players')
db_teams = Database(database='Projeto', collection='Teams')
db_games = Database(database='Projeto', collection='Games')
db_players.resetDatabase()
db_teams.resetDatabase()
db_games.resetDatabase()
gamesModel = GamesModel(db_players=db_players, db_teams=db_teams, db_games=db_games)

gamesCLI = GamesCLI(games_model=gamesModel)
gamesCLI.run()