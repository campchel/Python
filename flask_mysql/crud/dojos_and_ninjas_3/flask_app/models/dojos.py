from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s),NOW(),NOW());"
        # comes back as the new row id
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def get_one_dojo_ninjas(cls,data):
        query= """SELECT * FROM dojos
        JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id=%(id)s;
        """
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        one_dojo=cls(result[0])
        for row_from_db in result:
            ninja_data={
            "id" : row_from_db['ninjas.id'],
            "first_name" : row_from_db['first_name'],
            "last_name" : row_from_db['last_name'],
            "age" : row_from_db['age'],
            "created_at" : row_from_db['ninjas.created_at'],
            "updated_at" : row_from_db['ninjas.updated_at'],
            "dojo_id" : row_from_db['dojo_id']
            }
            one_dojo.all_ninjas.append( ninjas.Ninja(ninja_data) )
        return one_dojo
