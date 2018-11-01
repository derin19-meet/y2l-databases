from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_product(product, description, year, price):
  new_product = Product(
    product=product,
    description=description,
    year=year,
    price=price)
  session.add(new_product)
  session.commit()

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  session.query(Product).filter_by(
    id= id).delete()
  session.commit()


def get_product(id):
  pass
