from flask import Flask,request,redirect,jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db=SQLAlchemy(app)

class Employee(db.Model):

    empno= db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String(60))
    sal = db.Column(db.Float)
    deptno=db.Column(db.Integer)
   
    def serializer(self):
        return {
              "empno":self.empno,
              "ename":self.ename,
              "sal":self.sal,
              "deptno":self.deptno
               
        }


@app.route('/create',methods=['POST'])
def create_user():
    if request.method=='POST':
       d=request.get_json()

       dpt=Employee(
           empno=d.get('empno'),
           ename=d.get('ename'),
           sal=d.get('sal'),
           deptno=d.get('deptno')
       )
       db.session.add(dpt)
       db.session.commit()

       message={
        'data':'Record inserted successfully'
        }
       return jsonify(message) #it will convert your dict to json



@app.route('/list',methods=['GET'])
def list_users():
     dpts=Employee.query.all()
     listUser=[]
     for d in dpts:
         listUser.append(d.serializer())

     return jsonify(listUser)

@app.route('/get/<int:empno>',methods=['GET'])
def get_user_by_id(empno):
      u=Employee.query.get(empno)
      print(u)
      
      resp=requests.get("http://localhost:5000/get/{}".format(u.deptno))
      dct={"empno":u.empno,"ename":u.ename,"sal":u.sal,"deptno":u.deptno,
           "departname":resp.json().get('dname'),
           "loc":resp.json().get('loc')
        }

      
      print(dct)
      return jsonify(dct)

@app.route('/delete/<int:empno>',methods=['DELETE'])
def delete_by_id(empno):
      u= Employee.query.get(empno)
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

@app.route('/update/<int:empno>',methods=['PUT'])
def update_user_id(empno):
    u =Employee.query.get(empno)
    #json data from postman
    
    ename =request.json().get('ename')
    sal=request.json().get('sal')
    deptno =request.json().get('deptno')

    #update the data
    u.ename=ename
    u.sal=sal
    u.deptno=deptno
    

    db.session.add(u)
    db.session.commit()
    return jsonify({"data":"Record is udpated"})



with app.app_context():
    db.create_all() #it will create the tables in database

if __name__=="__main__":
    app.run(debug=True,port=8000)