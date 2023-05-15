from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # the get_all method will be used when we need to retrieve all the rows of the table 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users._schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    # the get_one method will be used when we need to retrieve just one specific row of the table
    # @classmethod
    # def get_one(cls, user_id):
    #     query  = "SELECT * FROM users WHERE id = %(id)s;"
    #     data = {'id':user_id}
    #     results = connectToMySQL('users._schema').query_db(query, data)
    #     return cls(results[0])

    # the save method will be used when we need to save a new user to our database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL('users._schema').query_db(query,data)
        return result


