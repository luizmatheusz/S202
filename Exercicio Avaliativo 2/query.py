from database import Database

# Conectando ao banco de dados
db = Database("bolt://3.239.245.61:7687", "neo4j", "acquisition-polarity-rehabilitation")

# Questão 1
# print("\nQuestão 1:")
# query = "MATCH (:Player {name: $name, id: $id})"
# parameters = {"name": player.name, "id": player.id}
# db.execute_query(query, parameters)

# print("\na) Ano de nascimento e CPF dos professores:")
# query = "MATCH (t:Teacher) RETURN t.ano_nasc, t.cpf"
# results = db.execute_query(query)
# for result in results:
#     print(f"Ano de nascimento: {result['t.ano_nasc']}\nCPF: {result['t.cpf']}")
    
# print("\nb) Nome e ano de nascimento dos professores que o nome começa com M:")
# query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.ano_nasc"
# results = db.execute_query(query)
# for result in results:
#     print(f"Nome: {result['t.name']}\nAno de nascimento: {result['t.ano_nasc']}")

# print("\nc) Nome das cidades:")
# query = "MATCH (c:City) RETURN c.name"
# results = db.execute_query(query)
# for result in results:
#     print(f"{result['c.name']}")

# print("\nd) Nome, endereço e número das escolas com 150 <= número <= 550")
# query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
# results = db.execute_query(query)
# for result in results:
#     print(f"Nome: {result['s.name']}, endereço: {result['s.address']}, número: {result['s.number']}")

# Questão 2
print("\nQuestão 2")
# print("\na) Ano de nascimento do professor mais jovem e do professor mais velho:")
# query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc DESC LIMIT 1"
# results = db.execute_query(query)
# print(f"Ano de nascimento do professor mais jovem: {results[0]['t.ano_nasc']}")
# query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1"
# results = db.execute_query(query)
# print(f"Ano de nascimento do professor mais velho: {results[0]['t.ano_nasc']}")

# print("\nb) Média aritmética dos habitantes das cidades:")
# query = "MATCH (c:City) RETURN avg(c.population) as avg_population"
# results = db.execute_query(query)
# print(f"Média: {results[0]['avg_population']}")

# print("\nc) Cidade com o CEP 37540-000")
# query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') as name"
# results = db.execute_query(query)
# print(f"Nome da cidade: {results[0]['name']}")

# print("\nd) Terceiro caractere de cada professor")
# query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS caractere"
# results = db.execute_query(query)
# for result in results:
#     print(f"Caractere: {result['caractere']}")


# Criando jogadores
# p1 = Player(name="Luiz", id=1)
# p2 = Player(name="Matheus", id=2)
# p3 = Player(name="Fulano", id=3)
# game_db.create_player(player=p1)
# game_db.create_player(player=p2)
# game_db.create_player(player=p3)

# # Criando partidas
# m1 = Match(id=1)
# m2 = Match(id=2)
# game_db.create_match(match=m1)
# game_db.create_match(match=m2)

# # Criando relacionamentos partida-jogador
# game_db.node_match_player(match=m1, player=p2, goals=3)
# game_db.node_match_player(match=m1, player=p1, goals=1)
# game_db.node_match_player(match=m2, player=p1, goals=0)
# game_db.node_match_player(match=m2, player=p3, goals=2)
# game_db.node_match_player(match=m2, player=p2, goals=5)

# # Atualizando jogadores
# game_db.update_player_name(player=p2, name="Joao")
# game_db.update_player_stats(match=m1, player=p1, goals=2)
# game_db.update_player_stats(match=m2, player=p3, goals=0)

# # Obtendo informações
# print("Jogadores:")
# print(game_db.get_players())
# print("Partida:")
# print(game_db.get_match(id_match=1))
# print("Histórico de um jogador:")
# print(game_db.get_player_match_history(id_player=2))

# # Excluindo jogadores
# game_db.delete_player(player=p1)