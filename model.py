from flask_sqlalchemy import SQLAlchemy
from werkzeug  import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    _tablename_ = "users"
    uid = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(100))
    lasttname = db.Column(db.String(100))
    email = db.Column(db.String(120),unique = True)
    pwdhash = db.Column(db.String(54))

    def _init_(self,firstname,lastname,email,password):
        self.firstname = firstname.title()
        self.lasttname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self,password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.pwdhash,password)      

