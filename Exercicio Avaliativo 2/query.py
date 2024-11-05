from database import Database

# Conectando ao banco de dados
db = Database("bolt://3.239.245.61:7687", "neo4j", "acquisition-polarity-rehabilitation")

# Questão 1
print("\nQuestão 1:")
print("\na) Ano de nascimento e CPF dos professores:")
query = "MATCH (t:Teacher) RETURN t.ano_nasc, t.cpf"
results = db.execute_query(query)
for result in results:
    print(f"Ano de nascimento: {result['t.ano_nasc']}\nCPF: {result['t.cpf']}")
    
print("\nb) Nome e ano de nascimento dos professores que o nome começa com M:")
query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.ano_nasc"
results = db.execute_query(query)
for result in results:
    print(f"Nome: {result['t.name']}\nAno de nascimento: {result['t.ano_nasc']}")

print("\nc) Nome das cidades:")
query = "MATCH (c:City) RETURN c.name"
results = db.execute_query(query)
for result in results:
    print(f"{result['c.name']}")

print("\nd) Nome, endereço e número das escolas com 150 <= número <= 550")
query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
results = db.execute_query(query)
for result in results:
    print(f"Nome: {result['s.name']}, endereço: {result['s.address']}, número: {result['s.number']}")

# Questão 2
print("\nQuestão 2")
print("\na) Ano de nascimento do professor mais jovem e do professor mais velho:")
query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc DESC LIMIT 1"
results = db.execute_query(query)
print(f"Ano de nascimento do professor mais jovem: {results[0]['t.ano_nasc']}")
query = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1"
results = db.execute_query(query)
print(f"Ano de nascimento do professor mais velho: {results[0]['t.ano_nasc']}")

print("\nb) Média aritmética dos habitantes das cidades:")
query = "MATCH (c:City) RETURN avg(c.population) as avg_population"
results = db.execute_query(query)
print(f"Média: {results[0]['avg_population']}")

print("\nc) Cidade com o CEP 37540-000")
query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') as name"
results = db.execute_query(query)
print(f"Nome da cidade: {results[0]['name']}")

print("\nd) Terceiro caractere de cada professor")
query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS caractere"
results = db.execute_query(query)
for result in results:
    print(f"Caractere: {result['caractere']}")