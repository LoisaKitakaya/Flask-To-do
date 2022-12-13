from app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(254))
    todos = db.relationship('Todo', backref='user')

    def __repr__(self) -> str:
        
        return f'<User: "{self.username}">'

class Todo(db.Model):

    # __tablename__ = 'todos'
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    label = db.Column(db.String(50))
    description = db.Column(db.Text)
    due_date = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        
        return f'<Todo: "{self.task}">'