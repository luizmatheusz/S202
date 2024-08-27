from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()
pokedex = Pokedex(db)
writeAJson(pokedex.getPokemonByHeight("1.09 m"), "pokemon_by_height")
writeAJson(pokedex.getPokemonExcludingTypes(['Fighting', 'Fire']), "pokemon_excluding_types")
writeAJson(pokedex.getPokemonByEvolutionStatus(False), "pokemon_by_evolution_status")
writeAJson(pokedex.getPokemonByWeaknessCount(0), "pokemon_by_weakness_count")
writeAJson(pokedex.getPokemonByAvgSpawns([0.1, 0.3]), "pokemon_by_avg_spawns")
