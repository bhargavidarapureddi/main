import json
from flask import Flask,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60))
    email=db.Column(db.String(60))
    password=db.Column(db.String(500))
    mobile_number=db.Column(db.String(300))

    def serializer(self):
        return{
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password":self.password,
            "mobile_number":self.mobile_number
        }
    def __str__(self):
        return self.name+self.email+str(self.mobile_number)
    
@app.route("/create",methods=['POST'])
def create_user():
    if request.method=='POST':
        u=request.get_json()

        user=User(
            name=u.get('name'),
            email=u.get('email'),
            password=u.get('password'),
            mobile_number=u.get('mobile_number')
        )
        db.session.add(user)
        db.session.commit()

        message={
            'data':'Record inserted successfully'
        }
        return jsonify(message)   #it will convert dict to json
@app.route('/list',methods=['GET'])
def list_user():
    users=User.query.all()
    listUser=[]
    for u in users:
        listUser.append(u.serializer())
    return jsonify(listUser)

@app.route('/get/<int:id>',methods=['GET'])
def get_user_by_id(id):
    u=User.query.get(id).serializer()
    return jsonify(u)

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_by_id(id):
    u=User.query.get(id)
    if u is not None:
        db.session.delete(u)
        db.session.commit()
        msg={
            "data":"Record is deleted"
        }
    else:
        msg={
            "data":"Record doesnot exists"
        }
    return jsonify(msg)
    
@app.route('/update/<int:id>',methods=['PUT'])
def update_user_id(id):
    u=User.query.get(id)
    name=request.json.get('name')
    email=request.json.get('email')
    password=request.json.get('password')
    mobile_number=request.json.get('mobile_number')

    u.name=name
    u.email=email
    u.password=password
    u.mobile_number=mobile_number

    db.session.add(u)
    db.session.commit()
    return jsonify({"data":"Record is updated"})

with app.app_context():
    db.create_all()       #it will create tables in Database
app.run(debug=True)