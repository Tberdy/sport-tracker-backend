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
match_parser.add_argument('user_id', type=int)
match_parser.add_argument('user_time', type=float)
match_parser.add_argument('user_distance', type=float)
match_parser.add_argument('opponent_id', type=int)
match_parser.add_argument('opponent_time', type=float)
match_parser.add_argument('opponent_distance', type=float)
match_parser.add_argument('location_name', type=str)
match_parser.add_argument('location_latitude', type=float)
match_parser.add_argument('location_longitude', type=float)

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
    'user_id': fields.Integer,
    'user_time': fields.Float,
    'user_distance': fields.Float,
    'opponent_id': fields.Integer,
    'opponent_time': fields.Float,
    'opponent_distance': fields.Float,
    'location_name': fields.String,
    'location_latitude': fields.Float,
    'location_longitude': fields.Float
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
        match.user_id = args['user_id']
        match.user_distance = args['user_distance']
        match.user_time = args['user_time']
        match.opponent_id = args['opponent_id']
        match.opponent_distance = args['opponent_distance']
        match.opponent_time = args['opponent_time']
        match.location_name = args['location_name']
        match.location_latitude = args['location_latitude']
        match.location_longitude = args['location_longitude']

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
            user_id=args['user_id'],
            user_time=args['user_time'],
            user_distance=args['user_distance'],
            opponent_id=args['opponent_id'],
            opponent_time=args['opponent_time'],
            opponent_distance=args['opponent_distance'],
            location_name=args['location_name'],
            location_latitude=args['location_latitude'],
            location_longitude=args['location_longitude']
        )
        db.session.add(match)
        db.session.commit()

        return match, 201


# Register routing
api.add_resource(UserListApi, '/users')
api.add_resource(UserApi, '/users/<int:user_id>')
api.add_resource(MatchListApi, '/matches')
api.add_resource(MatchApi, '/matches/<int:match_id>')
