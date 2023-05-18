from __init__ import db_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# перший клас: кондитерські вироби
class Baking(Base):
    __tablename__ = "baking"

    product_id = Column("product_id", Integer, primary_key=True)
    product_name = Column("product_name", String, nullable=False)
    product_type = Column("product_type", String, nullable=False)
    img = Column("img", String, nullable=False)
    weight = Column("weight", Integer, nullable=False)
    amount = Column("amount", Integer, nullable=False)
    price = Column("price", Integer, nullable=False)
    description = Column("description", String, nullable=False)
    fast_delivery = Column("fast_delivery", String, nullable=False)


    def __init__(self, product_name, product_type, img, weight, amount, price, description, fast_delivery):
        self.product_name = product_name
        self.product_type = product_type
        self.img = img
        self.weight = weight
        self.amount = amount
        self.price = price
        self.description = description
        self.fast_delivery = fast_delivery


    def __repr__(self):
        return f"id: {self.product_id}, name: {self.product_name}"
    

class Order(Base):
    __tablename__ = "order"

    order_id = Column("order_id", Integer, primary_key=True)
    customer_name = Column("customer_name", String)
    baking = Column("baking", String)
    amount = Column("amount", String)


    def __init__(self, customer_name, baking, amount):
        self.customer_name = customer_name
        self.baking = baking
        self.amount = amount

    def __repr__(self):
        return f"id {self.order_id}"


Base.metadata.create_all(bind=db_engine)

Session = sessionmaker(bind=db_engine)
s = Session()
s.commit()