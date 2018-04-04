from backend import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120))
    matches = db.relationship("Match", back_populates="user")

    def __init__(self, firstname, lastname, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="matches")
    opponent_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    opponent = db.relationship("User", back_populates="matches")
    user_time = db.Column(db.Float)
    user_distance = db.Column(db.Float)
    opponent_time = db.Column(db.Float)
    opponent_distance = db.Column(db.Float)
    location_name = db.Column(db.String)
    location_latitude = db.Column(db.Float)
    location_longitude = db.Column(db.Float)

    def __init__(
        self, name, description, user_id, opponent_id, user_time,
        user_distance, opponent_time, opponent_distance,
        location_name, location_latitude, location_longitude
    ):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.opponent_id = opponent_id
        self.user_time = user_time
        self.user_distance = user_distance
        self.opponent_time = opponent_time
        self.opponent_distance = opponent_distance
        self.location_name = location_name
        self.location_latitude = location_latitude
        self.location_longitude = location_longitude
