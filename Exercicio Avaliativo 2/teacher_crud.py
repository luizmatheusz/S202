class TeacherCRUD:
    def __init__(self, database):
        self.db = database
        
    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        
    def read(self, name):
        query = "MATCH (t:Teacher) WHERE t.name = $name RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results[0]
        
    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        
    def update(self, name, newCpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)