from models.player import Player
from models.team import Team
from models.game import Game

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class GamesCLI(SimpleCLI):
    def __init__(self, games_model):
        super().__init__()
        self.games_model = games_model
        self.add_command("create_player", self.create_player)
        self.add_command("create_team", self.create_team)
        self.add_command("create_game", self.create_game)
        self.add_command("read_player", self.read_player_by_id)
        self.add_command("read_team", self.read_team_by_id)
        self.add_command("read_game", self.read_game_by_id)
        self.add_command("update_player", self.update_player)
        self.add_command("update_team", self.update_team)
        self.add_command("update_game", self.update_game)
        self.add_command("delete_player", self.delete_player)
        self.add_command("delete_team", self.delete_team)
        self.add_command("delete_game", self.delete_game)

    def create_player(self):
        id = input("Entre com o id: ")
        name = input("Entre com o nome: ")
        position = input("Entre com a posição: ")
        team = input("Entre com o time: ")
        img = input("Entre com o url da img: ")
        
        team = self.games_model.read_team_by_abbr(team)
        
        if(team != None):
            player = Player(id=id, name=name, position=position, team=team, img=img)
            self.games_model.create_player(player=player)
            
        else:
            print("Invalid team.")
        
    def create_team(self):
        id = input("Entre com o id: ")
        name = input("Entre com o nome: ")
        abbr = input("Entre com a sigla: ")
        team = Team(id=id, name=name, abbr=abbr)
        self.games_model.create_team(team=team)
        
    def create_game(self):
        id = input("Entre com o id: ")
        home_team = input("Entre com o nome do time mandante: ")
        away_team = input("Entre com o nome do time visitante: ")
        home_score = int(input("Entre com a pontuação do time mandante: "))
        away_score = int(input("Entre com a pontuação do time visitante: "))
        week = input("Entre com a semana do jogo: ")
        
        home_team = self.games_model.read_team_by_abbr(home_team)
        away_team = self.games_model.read_team_by_abbr(away_team)
        
        if(home_team != None and away_team != None):
            game = Game(id=id, home_team=home_team.to_dict(), away_team=away_team.to_dict(), home_score=home_score, away_score=away_score, week=week)
            self.games_model.create_game(game=game)
            
        else:
            print("Invalid teams.")        
        
    def read_player_by_id(self):
        id = input("Entre com o id: ")
        player = self.games_model.read_player_by_id(id)
        if player:
            print(f"ID: {player['_id']}")
            print(f"Nome: {player['name']}")
            print(f"Posição: {player['position']}")
            print(f"Time: {player['team']}")
            print(f"URL img: {player['img']}")
    
    def read_team_by_id(self):
        id = input("Entre com o id: ")
        team = self.games_model.read_team_by_id(id)
        if team:
            print(f"ID: {team['_id']}")
            print(f"Nome: {team['name']}")
            print(f"Sigla: {team['abbr']}")
            
            if len(team['roster'])>0:
                for i in team['roster']:
                    print(i)
                
            else:
                print("Não há elenco.")
                
    def read_game_by_id(self):
        id = input("Entre com o id: ")
        game = self.games_model.read_game_by_id(id)
        if game:
            print(f"ID: {game['_id']}")
            print(f"Semana: {game['week']}")
            print(f"Time Mandante: {game['home_team']}")
            print(f"Time Visitante: {game['away_team']}")
            print(f"Pontuação Mandante: {game['home_score']}")
            print(f"Pontuação Visitante: {game['away_score']}")
            print(f"Time Vencedor: {game['winner']}")
            print(f"Total de pontos: {game['total_score']}")

    def update_player(self):
        id = input("Entre com o id: ")
        name = input("Entre com o nome: ")
        position = input("Entre com a posição: ")
        team = input("Entre com o time: ")
        img = input("Entre com o url da img: ")
        player = Player(id=id, name=name, position=position, team=team, img=img)
        self.games_model.update_player(player=player)
        
    def update_team(self):
        id = input("Entre com o id: ")
        name = input("Entre com o nome: ")
        abbr = input("Entre com a sigla: ")
        team = Team(id=id, name=name, abbr=abbr)
        self.games_model.update_team(team=team)
        
    def update_game(self):
        id = input("Entre com o id: ")
        home_team = input("Entre com o nome do time mandante: ")
        away_team = input("Entre com o nome do time visitante: ")
        home_score = int(input("Entre com a pontuação do time mandante: "))
        away_score = int(input("Entre com a pontuação do time visitante: "))
        week = input("Entre com a semana do jogo: ")
        
        home_team = self.games_model.read_team_by_abbr(home_team)
        away_team = self.games_model.read_team_by_abbr(away_team)
        
        if(home_team != None and away_team != None):
            game = Game(id=id, home_team=home_team.to_dict(), away_team=away_team.to_dict(), home_score=home_score, away_score=away_score, week=week)
            self.games_model.update_game(game=game)
            
        else:
            print("Invalid teams.")

    def delete_player(self):
        id = input("Entre com o id: ")
        self.games_model.delete_player(id)
        
    def delete_team(self):
        id = input("Entre com o id: ")
        self.games_model.delete_team(id)
        
    def delete_game(self):
        id = input("Entre com o id: ")
        self.games_model.delete_game(id)
        
    def run(self):
        print("Welcome to the games CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()