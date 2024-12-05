class Team:
    def __init__(self, id: str, name: str, abbr:str):
        self.id = id
        self.name = name
        self.abbr = abbr
        self.roster = []
        
    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'abbr': self.abbr,
            'roster': self.roster
        }
            
        return data
        
    def show_info(self):
        print(f"Team: [{self.abbr}] {self.name}")