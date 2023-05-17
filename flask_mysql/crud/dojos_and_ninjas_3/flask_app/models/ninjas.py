from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for u in results:
            ninjas.append( cls(u) )
        return ninjas

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO dojos ('first_name, last_name, age) VALUES (%(first_name)s, %(last_name)s, %(age)s);"
        return connectToMySQL('burgers').query_db( query, data)