from app import db
import re

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    label = db.Column(db.Integer)
    genre = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def to_dict(self):
        dict = {
        'name': self.name,
        'label': self.label,
        'genre': self.genre,
        'price': self.price,
        }
        return dict

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'amount': self.amount,
        }
        return dict