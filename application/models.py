from __init__ import db_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
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
    

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column("customer_id", Integer, primary_key=True)
    full_name = Column("customer_full_name", String, nullable=False)
    phone = Column("phone", Integer, nullable=False)


    def __init__(self, customer_id, customer_name, phone):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone = phone

    def __repr__(self):
        return self.customer_id


# другій клас: замовлення на вироби
class PaidOrder(Base):
    __tablename__ = "paid_order"
    
    order_id = Column("order_id", Integer, primary_key=True)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.customer_id"), nullable=False)
    product_id = Column("product_id", Integer, ForeignKey("baking.product_id"), nullable=False)
    num_of_items = Column("num_of_items", Integer, nullable=False)


    def __init__(self, customer_id, product_id, num_of_items):
        self.customer_id = customer_id
        self.product_id = product_id
        self.num_of_items = num_of_items

    def __repr__(self):
        return f"{self.customer_id} {self.product_id} {self.num_of_items}"
    

Base.metadata.create_all(bind=db_engine)

Session = sessionmaker(bind=db_engine)
s = Session()
s.commit()