from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, User
app = Flask(__name__)

# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate().init_app(app, db)



api = Api(app) #restframework


class Users(Resource):

    # read
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            return {'user': user.to_dict()}, 200
        else:
            users = User.query.all()
            return {'users': [user.to_dict() for user in users]}, 200

    # create
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            return {'error': 'Username and email are required'}, 400
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User added successfully'}, 201

    # update
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        if not username or not email:
            return {'error': 'Username and email are required'}, 400
        user.username = username
        user.email = email
        db.session.commit()
        return {'message': 'User updated successfully'}, 200

    # delete
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 200

# use api.add_resource to add the paths
api.add_resource(Users, '/users', '/users/<int:user_id>')
with app.app_context():
    db.create_all()

if __name__ == '__main__':
   app.run(port=5555, debug=True)