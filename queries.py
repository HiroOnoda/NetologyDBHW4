import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/netology_db'
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Задание 2
#Принимаем publisher(name/id)
#Выводим: название книги | название магазина | стоимость покупки | дата покупки

def id_publisher_query(session,pub_id):
    q = (session.query(Publisher,Book,Stock,Sale,Shop)).join(Book,Book.id_publisher == Publisher.id).join(Stock,Stock.id_book == Book.id).join(Sale,Sale.id_stock == Stock.id).join(Shop,Shop.id == Stock.id_shop).filter(Publisher.id == pub_id)
    print("Результат запроса по id " + str(pub_id) + ": ")
    for s in q.all():
        print(s.Book.title," | ",s.Shop.name," | ",s.Sale.price," | ",s.Sale.date_sale)
    pass

def name_publisher_query(session,pub_name):
    q = (session.query(Publisher,Book,Stock,Sale,Shop)).join(Book,Book.id_publisher == Publisher.id).join(Stock,Stock.id_book == Book.id).join(Sale,Sale.id_stock == Stock.id).join(Shop,Shop.id == Stock.id_shop).filter(Publisher.name == pub_name)
    print("Результат запроса по имени "+str(pub_name)+": ")
    for s in q.all():
        print(s.Book.title," | ",s.Shop.name," | ",s.Sale.price," | ",s.Sale.date_sale)
    pass

id_publisher_query(session,1)
name_publisher_query(session,"Pearson")
