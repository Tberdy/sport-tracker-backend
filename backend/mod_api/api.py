from flask import Blueprint
from flask_restful import reqparse, Api, Resource, fields, marshal_with

from backend import db
from .models import User, Match

mod_api = Blueprint('api', __name__)
api = Api(mod_api)

user_parser = reqparse.RequestParser()
user_parser.add_argument('firstname', type=str)
user_parser.add_argument('lastname', type=str)
user_parser.add_argument('email', type=str)

match_parser = reqparse.RequestParser()
match_parser.add_argument('name', type=str)
match_parser.add_argument('description', type=str)
match_parser.add_argument('userId', type=int)
match_parser.add_argument('userTime', type=float)
match_parser.add_argument('userDistance', type=float)
match_parser.add_argument('opponentId', type=int)
match_parser.add_argument('opponentTime', type=float)
match_parser.add_argument('opponentDistance', type=float)
match_parser.add_argument('locationName', type=str)
match_parser.add_argument('locationLatitude', type=float)
match_parser.add_argument('locationLongitude', type=float)
match_parser.add_argument('state', type=int)

user_fields = {
    'id': fields.Integer,
    'firstname': fields.String,
    'lastname': fields.String,
    'email': fields.String,
}

match_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'userId': fields.Integer,
    'userTime': fields.Float,
    'userDistance': fields.Float,
    'opponentId': fields.Integer,
    'opponentTime': fields.Float,
    'opponentDistance': fields.Float,
    'locationName': fields.String,
    'locationLatitude': fields.Float,
    'locationLongitude': fields.Float,
    'state': fields.Integer,
}


# User
# shows a single user item and lets you delete a user item
class UserApi(Resource):
    @marshal_with(user_fields)
    def get(self, user_id):
        user = User.query.get(user_id)
        return user

    def delete(self, user_id):
        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()

        return '', 204

    @marshal_with(user_fields)
    def put(self, user_id):
        args = user_parser.parse_args()
        user = User.query.get(user_id)
        user.firstname = args['firstname']
        user.lastname = args['lastname']
        user.email = args['email']
        db.session.add(user)
        db.session.commit()

        return user, 201


# UserList
# shows a list of all users, and lets you POST to add new users
class UserListApi(Resource):
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args()
        user = User(
            firstname=args['firstname'],
            lastname=args['lastname'],
            email=args['email']
        )
        db.session.add(user)
        db.session.commit()

        return user, 201


# Match
# shows a single match item and lets you delete a match item
class MatchApi(Resource):
    @marshal_with(match_fields)
    def get(self, match_id):
        match = Match.query.get(match_id)
        return match

    def delete(self, match_id):
        match = Match.query.get(match_id)

        db.session.delete(match)
        db.session.commit()

        return '', 204

    @marshal_with(match_fields)
    def put(self, match_id):
        args = match_parser.parse_args()
        match = Match.query.get(match_id)

        match.name = args['name']
        match.description = args['description']
        match.userId = args['userId']
        match.userDistance = args['userDistance']
        match.userTime = args['userTime']
        match.opponentId = args['opponentId']
        match.opponentDistance = args['opponentDistance']
        match.opponentTime = args['opponentTime']
        match.locationName = args['locationName']
        match.locationLatitude = args['locationLatitude']
        match.locationLongitude = args['locationLongitude']
        match.state = args['state']

        db.session.add(match)
        db.session.commit()

        return match, 201


# MatchList
# shows a list of all matches, and lets you POST to add new matches
class MatchListApi(Resource):
    @marshal_with(match_fields)
    def get(self):
        matchs = Match.query.all()
        return matchs

    @marshal_with(match_fields)
    def post(self):
        args = match_parser.parse_args()
        match = Match(
            name=args['name'],
            description=args['description'],
            userId=args['userId'],
            userTime=args['userTime'],
            userDistance=args['userDistance'],
            opponentId=args['opponentId'],
            opponentTime=args['opponentTime'],
            opponentDistance=args['opponentDistance'],
            locationName=args['locationName'],
            locationLatitude=args['locationLatitude'],
            locationLongitude=args['locationLongitude'],
            state=args['state'],
        )
        db.session.add(match)
        db.session.commit()

        return match, 201


# Register routing
api.add_resource(UserListApi, '/users')
api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(MatchListApi, '/matches')
api.add_resource(MatchApi, '/matches/<int:match_id>')
