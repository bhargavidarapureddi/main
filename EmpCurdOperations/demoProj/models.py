from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True,nullable=False)
    email = db.Column(db.String(100), unique=True,nullable=False)

    def to_dict(self):
        return{
            'id':self.id,
            'username':self.username,
            'email':self.email
        }