from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.controllers import register_controllers
from flask import flash
import re
from flask_bcrypt import Bcrypt
bycrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Register:
    db= 'login_registration_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
#creating a user
    @classmethod
    def create(cls,data):
        query ="INSERT INTO Register (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result=connectToMySQL(cls.db).query_db(query,data)
        return result
    
#validating the data from Register from the workbench
    @staticmethod
    def validate_Register(newReg):
        is_valid = True 
        if len(newReg['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(newReg['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(newReg['email']) < 5:
            flash("Email is required.")
            is_valid = False
        if not EMAIL_REGEX.match(newReg['email']):
            is_valid = False
        if len(newReg['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid=False
        if newReg['password_confirm'] != newReg['password']:
            flash("Password does not match.")
            is_valid=False
        return is_valid
