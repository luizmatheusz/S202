from database import Database
from match import Match
from player import Player
from game_database import GameDatabase

# Conectando ao banco de dados
db = Database("bolt://34.201.28.26:7687", "neo4j", "liberty-chatter-impact")
db.drop_all()

game_db = GameDatabase(database=db)

# Criando jogadores
p1 = Player(name="Luiz", id=1)
p2 = Player(name="Matheus", id=2)
p3 = Player(name="Fulano", id=3)
game_db.create_player(player=p1)
game_db.create_player(player=p2)
game_db.create_player(player=p3)

# Criando partidas
m1 = Match(id=1)
m2 = Match(id=2)
game_db.create_match(match=m1)
game_db.create_match(match=m2)

# Criando relacionamentos partida-jogador
game_db.node_match_player(match=m1, player=p2, goals=3)
game_db.node_match_player(match=m1, player=p1, goals=1)
game_db.node_match_player(match=m2, player=p1, goals=0)
game_db.node_match_player(match=m2, player=p3, goals=2)
game_db.node_match_player(match=m2, player=p2, goals=5)

# Atualizando jogadores
game_db.update_player_name(player=p2, name="Joao")
game_db.update_player_stats(match=m1, player=p1, goals=2)
game_db.update_player_stats(match=m2, player=p3, goals=0)

# Obtendo informações
print("Jogadores:")
print(game_db.get_players())
print("Partida:")
print(game_db.get_match(id_match=1))
print("Histórico de um jogador:")
print(game_db.get_player_match_history(id_player=2))

# Excluindo jogadores
game_db.delete_player(player=p1)