import json

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker



DSN = 'postgresql://postgres:postgres@localhost:5432/netology_db'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    book = relationship("Book", back_populates="publisher")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    stock = relationship("Stock", back_populates="shop")

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.Integer,sq.ForeignKey("publisher.id"),nullable = False)

    publisher = relationship("Publisher",back_populates="book")

    stock = relationship("Stock",back_populates="book")

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer,sq.ForeignKey("book.id"),nullable = False)
    id_shop = sq.Column(sq.Integer,sq.ForeignKey("shop.id"),nullable = False)
    count = sq.Column(sq.Integer)

    book = relationship("Book", back_populates="stock")
    shop = relationship("Shop", back_populates="stock")

    sale = relationship("Sale",back_populates="stock")


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer,primary_key =True)
    price = sq.Column(sq.String(length=40))
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer,sq.ForeignKey("stock.id"),nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship("Stock", back_populates="sale")

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_all_tables(engine):
    Base.metadata.drop_all(engine)

#Задание 1,составление модели классов/создание таблицы
#create_tables(engine)
#drop_all_tables(engine)

session.close()