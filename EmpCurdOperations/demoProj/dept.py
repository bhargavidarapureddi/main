import json

from flask import Flask,request,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db=SQLAlchemy(app)

class Department(db.Model):

    deptno= db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(60))
    loc = db.Column(db.String(60))
   
    def serializer(self):
        return {
              "deptno":self.deptno,
              "dname":self.dname,
              "loc":self.loc
               
        }

    def __str__(self):
        return self.dname + self.loc

@app.route('/create',methods=['POST'])
def create_user():
    if request.method=='POST':
       d=request.get_json()

       dpt=Department(
           deptno=d.get('deptno'),
           dname=d.get('dname'),
           loc=d.get('loc'),
       )
       db.session.add(dpt)
       db.session.commit()

       message={
        'data':'Record inserted successfully'
        }
       return jsonify(message) #it will convert your dict to json



@app.route('/list',methods=['GET'])
def list_users():
     dpts=Department.query.all()
     listUser=[]
     for d in dpts:
         listUser.append(d.serializer())

     return jsonify(listUser)

@app.route('/get/<id>',methods=['GET'])
def get_user_by_id(id):
      u=Department.query.get(int(id)).serializer()
      return jsonify(u)

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete_by_id(id):
      u= Department.query.get(id)
      if u is not None:
          db.session.delete(u)
          db.session.commit()
          msg={
               "data":"record is deleted"
          }
      else:
          msg = {
              "data": "Record doesnot exists"
          }
      return jsonify(msg)

@app.route('/update/<int:id>',methods=['PUT'])
def update_user_id(id):
    u = Department.query.get(id)
    #json data from postman
    dname =request.json.get('dname')
    loc =request.json.get('loc')

    #update the data
    u.dname=dname
    u.loc=loc
    

    db.session.add(u)
    db.session.commit()
    return jsonify({"data":"Record is udpated"})



with app.app_context():
    db.create_all() #it will create the tables in database

if __name__=="__main__":
    app.run(debug=True)