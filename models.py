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
    alt=db.Column('alt',db.String())
    name=db.Column('Name',db.String())
    price=db.Column('price',db.String())
    size=db.Column('size',db.String())
    material=db.Column('material',db.String())
    type=db.Column('type',db.String())
    caution=db.Column('caution',db.String())
    delivery=db.Column('delivery',db.String())
    description=db.Column('description',db.Text)



    def __repr__(self):
        return f'''<Product ( URL:{self.url}
            ALT:{self.alt}
            Name:{self.name}
            Price:{self.price}
            Size:{self.size}
            Material:{self.material}
            Type:{self.type}
            Caution:{self.caution}
            Delivery:{self.delivery}
            Description:{self.description}
            )'''