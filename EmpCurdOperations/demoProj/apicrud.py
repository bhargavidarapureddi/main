from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
 
db = SQLAlchemy(app)
api = Api(app)
 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
 
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
 
class User_data(Resource):
 
    def post(self):
        if request.method == 'POST':
            u = request.get_json()
 
            user = User(
                username=u.get('username'),
                email=u.get('email'),
 
            )
            db.session.add(user)
            db.session.commit()
 
            message = {
                'data': 'Record inserted successfully'
 
            }
            return jsonify(message)  # it will convert your dict to json
 
    def get(self):
        users = User.query.all()
        listUser = []
        for u in users:
            listUser.append(u.to_dict())
 
        return jsonify(listUser)
 
    def delete(self,id):
        u = User.query.get(id)
        if u is not None:
            db.session.delete(u)
            db.session.commit()
            msg = {
                "data": "record is deleted"
            }
        else:
            msg = {
                "data": "Record doesnot exists"
            }
        return jsonify(msg)
 
 
    def put(self,id):
        u = User.query.get(id)
        # json data from postman
        print(u)
        
        data= request.get_json()
        username = data.get('username')
        email = data.get('email')
 
        # update the data
        u.username = username
        u.email = email
 
        # db.session.add(u)
        db.session.commit()
        return jsonify({"data": "Record is udpated"})
 
 
api.add_resource(User_data, '/user','/user/<int:id>')
 
 
with app.app_context():
    db.create_all() #it will create the tables in database
 
if __name__=="__main__":
    app.run(debug=True)