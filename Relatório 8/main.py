from database import Database
from match import Match
from player import Player

db = Database("bolt://34.201.28.26:7687", "neo4j", "liberty-chatter-impact")
db.drop_all()
