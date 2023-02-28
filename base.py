import sqlalchemy

from sqlalchemy import Column, Integer, String, LargeBinary, func
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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
    categoria = Column(String(10))
    price = Column(Integer)

    def __repr__(self):
        return self
    def getJSON(self):
        return ({
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'categoria' : self.categoria,
            'price' : self.price
        })

def insert(name, description, categoria, price):
    Session = sessionmaker(bind=engine)
    session = Session()

    a = Productos(name=name, description=description, categoria=categoria, price=price)
    
    session.add(a)
    session.commit()

def filter(cat): # query que filtra por parámetro de categoria pasado
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(Productos).filter(Productos.categoria == cat)
    
    return query

if __name__ == "__main__":
    base.metadata.create_all(engine)
