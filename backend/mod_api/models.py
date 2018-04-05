from backend import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(120))

    def __init__(self, firstname, lastname, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    opponentId = db.Column(db.Integer, db.ForeignKey('user.id'))
    userTime = db.Column(db.Float)
    userDistance = db.Column(db.Float)
    opponentTime = db.Column(db.Float)
    opponentDistance = db.Column(db.Float)
    locationName = db.Column(db.String(50))
    locationLatitude = db.Column(db.Float)
    locationLongitude = db.Column(db.Float)
    state = db.Column(db.Integer)

    def __init__(
        self, name, description, userId, opponentId, userTime,
        userDistance, opponentTime, opponentDistance,
        locationName, locationLatitude, locationLongitude, state
    ):
        self.name = name
        self.description = description
        self.userId = userId
        self.opponentId = opponentId
        self.userTime = userTime
        self.userDistance = userDistance
        self.opponentTime = opponentTime
        self.opponentDistance = opponentDistance
        self.locationName = locationName
        self.locationLatitude = locationLatitude
        self.locationLongitude = locationLongitude
        self.state = state
