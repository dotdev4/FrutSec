import sqlalchemy

from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from flask import jsonify

engine = sqlalchemy.create_engine('sqlite:///database.db')

base = declarative_base()
base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

class Productos(base):
    __tablename__ = "Productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String(50))
    #data = Column(LargeBinary)
    price = Column(Integer)

    def __repr__(self):
        return self
    def __repr__(self):
        return ({
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            #'data' : self.data,
            'price' : self.price
        })

def insert(name, description, price):
    Session = sessionmaker(bind=engine)
    session = Session()

    a = Productos(name=name, description=description, price=price)
    
    session.add(a)
    session.commit()

if __name__ == "__main__":
    base.metadata.create_all(engine)