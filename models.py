from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///product.db'
db=SQLAlchemy(app)


class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    created=db.Column('Created',db.DateTime,default=datetime.datetime.now)
    url=db.Column('url',db.String())
    name=db.Column('Name',db.String())
    detail=db.Column('Deatil',db.String())
    type=db.Column('Type',db.String())
    price=db.Column('Price',db.String())
    onseason=db.Column('onSeason',db.String())
    



    def __repr__(self):
        return f'''<Product ( URL:{self.url}
            Name:{self.name}
            Price:{self.price}
            Detail:{self.detail}
            Type:{self.type}
            Price:{self.price}
            onSeason:{self.onseason}
            )'''
