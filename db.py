from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

scope_dict = {
    1 : "Aquarius",
    2 : "Pisces", 
    3 : "Aries",
    4 : "Taurus",
    5 : "Gemini",
    6 : "Cancer",
    7 : "Leo",
    8 : "Virgo",
    9 : "Libra",
    10 : "Scorpio",
    11 : "Sagittarius",
    12 : "Capricorn"
}

# your classes here
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sign_id = db.Column(db.Integer, db.ForeignKey('signs.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.sign_id = kwargs.get("sign_id")

    def serialize(self): 
        return {
            "id" : self.id,
            "name" : self.name,
            "sign_id" : self.sign_id
        }
    
class Signs(db.Model):
    __tablename__ = "signs"
    id = db.Column(db.Integer, primary_key=True)
    sign = db.Column(db.Integer, nullable=False)
    horoscope = db.Column(db.String, nullable=False)
    users = db.relationship("Users", cascade="delete")
   
    def __init__(self, **kwargs):
        self.sign = kwargs.get("sign")
        self.horoscope = kwargs.get("horoscope")

    def serialize(self): 
        return {
            "id" : self.id,
            "sign" : scope_dict.get(self.sign),
            "horoscope" : self.horoscope,
            "users" : [u.serialize() for u in self.users]
        }
    



