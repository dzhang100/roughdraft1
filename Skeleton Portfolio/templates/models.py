# from . import database
# from flask_login import UserMixin
# from sqlalchemy.sql import func

# #class for creating personal notes
# class Note(database.Model):
#     id = database.column(database.Integer, primary_key = True)
#     data = database.Column(database.String(10000))
#     date = database.Column(database.DataTime(timezone=True), default=func.now())
    
#     #foreign key which assigns a user to a note. This is for a one to many relationship, since one user can have multiple notes
#     user_id = database.Column(database.Integer, database.ForeignKey('user.id'))#assigns user id to a note


# class User(database.Model, UserMixin):
#     id = database.Column(database.Integer, primary_key = True)

#     #email is stored as a String, with a max character limit of 150
#     email = database.Column(database.String(150), unique = True)
#     #password is stored as a String, with a max character limit of 150
#     password = database.Column(database.string(150))
#     #name is stored as a String, with a max character limit of 150
#     name = database.Column(database.string(150))
    
#     #a list of all of the notes
#     notes = database.relationship('Note')



from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Note')