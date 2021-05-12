from db import db
from flask import Flask
from db import Users
from db import Signs
from flask import request 
import json

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


app = Flask(__name__)
db_filename = "horoscope.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False


db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({
        "success" : True, 
        "data": data
    }), code

def failure_response(error, code=404):
    return json.dumps({"success" : False, "error": error}), code

def load_scopes():
    signs = [
        Signs(sign=1, horoscope="Make an effort to heal a family rift that has been an emotional drag for too long. You can quite easily find the words to persuade loved ones and relatives that the constant bickering has got to stop. You're supposed to be on the same side."),
        Signs(sign=2, horoscope="You won't hesitate to let others know what you think today, and if some of your thoughts are less than flattering, well, that's just too bad. As far as you are concerned the truth is more important than making people feel good - and you're right."),
        Signs(sign=3, horoscope="You may have to make a big decision concerning your money situation today. If you are unhappy at having to live hand-to-mouth then now is the time to come up with new ways to boost your income. Think long-term but act immediately."),
        Signs(sign=4, horoscope="Today's new moon in your sign means there can be no more doubts or delays. You know what you want from life and you know you have what it takes to get it, so stop dreaming and start acting. You'll be amazed how quickly success arrives."),
        Signs(sign=5, horoscope="You don't need to keep looking over your shoulder. No one is going to jump out of the shadows at you. At this time of year more than most you can be a bit nervous, so steer clear of people and situations that make you feel uncomfortable"),
        Signs(sign=6, horoscope="If you are involved in a cause or social movement then what happens today will confirm that you are making a difference. If you are not involved, then you should be. You can do a lot of good in the world."),
        Signs(sign=7, horoscope="If you get a chance to move up in the world you must grab it with both hands. Yes, it will require extra work and yes, you will have to make a long-term commitment, but those things cannot be avoided if you want to be someone special."),
        Signs(sign=8, horoscope="Find a way to leave the daily grind behind you for a while. Get out into the world and have a good time. You know what they say: all work and no play makes Virgo a dull boy or girl, and that's not the image you want to project."),
        Signs(sign=9, horoscope="Start looking at ways to make serious money, rather than just getting by day to day. Every decision you make and every action you take must be aimed at improving your financial situation. If something doesn't pay well then give it a miss."),
        Signs(sign=10, horoscope="It may be the case that loved ones are having a bigger say in your affairs these days but is that such a bad thing? Today's new moon urges you to listen to advice from those you are closest to. And don't just listen, act on it too!"),
        Signs(sign=11, horoscope="You may not be one for detailed schedules - you prefer to take each moment as it comes - but if you want to make progress in one particular direction then you do need to get organized. If you don't, your workload may overwhelm you."),
        Signs(sign=12, horoscope="Ignore the critics and the cynics and do what every fiber of your being tells you is right. You've accomplished a lot in recent weeks and have a right to feel proud, but you can and you must achieve even more in the very near future.")
    ]

    for sign in signs:
        db.session.add(sign)
    db.session.commit()

# your routes here
@app.route("/api/users/", methods=["POST"])
def create_user():
    if Signs.query.all() == []:
        load_scopes()
    body = json.loads(request.data)
    name = body.get("name")
    sign_name = body.get("sign")
    sign_num = 0
    for key in scope_dict:  
        if scope_dict.get(key) == sign_name:
            sign_num = key 
    sign = Signs.query.filter_by(sign=sign_num).first()
    if name is None or sign is None:
        return failure_response("Missing field!", 400)    
    new_user = Users(name=name, sign_id=sign.serialize().get("id"))
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/api/users/<int:user_id>/")
def get_user(user_id):
    u = Users.query.filter_by(id=user_id).first()
    if u is None:
        return failure_response("No user found!")
    user = u.serialize()
    sign = Signs.query.filter_by(id=user.get("sign_id")).first()
    print(sign.serialize())
    return_user = {
        "id" : user.get("id"),
        "name" : user.get("name"),
        "sign" : sign.serialize().get("sign"),
    }
    return success_response(return_user)


@app.route("/api/users/<int:user_id>/horoscope/")
def get_scope_by_user(user_id):
    user = Users.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("No user found!")
    horoscope = Signs.query.filter_by(id=user.serialize().get("sign_id")).first()
    return success_response(horoscope.serialize().get("horoscope"))
    return user

@app.route("/api/users/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = Users.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("No user found!")
    db.session.delete(user)
    db.session.commit()
    return success_response(user.serialize())

@app.route("/api/<int:user_sign>/")
def get_scope(user_sign):
    sign = Signs.query.filter_by(sign=user_sign).first()
    if sign is None:
        return failure_response("No horoscope found!")
    return success_response(sign.serialize())    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
