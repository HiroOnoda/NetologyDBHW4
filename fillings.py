import json
from collections import namedtuple

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/netology_db'
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Задание 3,заполнение полей из json-файла
with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for line in data:
   model = line.get('model')
   match model:
        case "publisher":
            model = Publisher
            #name = line["fields"]["name"]
        case "book":
            model = Book
        case "shop":
            model = Shop
        case "stock":
            model = Stock
        case "sale":
            model = Sale
   session.add(model(id = line['pk'],**line["fields"]))
session.commit()

# q = session.query(Publisher)
# for s in q.all():
#     print(s.id,s.name)

session.close()