from models.team import Team

class Player:
    def __init__(self, id:str, name: str, position: str, team: Team, img: str):
        self.id = id
        self.name = name
        self.position = position
        self.team = team
        self.img = img
        
    def to_dict(self):
        return {
            'name': self.name,
            'position': self.position,
            'team': self.team.to_dict(),
            'img': self.img,
        }
        
    def show_info(self):
        print(f"{self.name} - {self.position}")