from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///product.db'
db=SQLAlchemy(app)


class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    created=db.Column('Created',db.DateTime,default=datetime.datetime.now)
    name=db.Column('Name',db.String())
    price=db.Column('Price',db.String())
    size=db.Column('Size',db.String())
    photo=db.Column('Photo',db.String())
    category=db.Column('Category',db.String())
    material=db.Column('Material',db.String())
    caution=db.Column('Caution',db.String())
    delivery=db.Column('Delivery',db.String())
    alt=db.Column('Alt',db.String())

    def __repr__(self):
        return f'''<Product Name: {self.name} Procuct Price:{self.price}
                    Size:{self.size} Photo:{self.photo}
                    Material:{self.material} Caution:{self.caution}
                    Category:{self.category} Delivery:{self.delivery}
                    Alt:{self.alt}'''