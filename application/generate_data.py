from sqlalchemy.orm import sessionmaker
from lorem_text import lorem
from random import choice, sample
from __init__ import db_engine
from models import Baking, Order

mafin1 = Baking("Choco Mafin", "mafin", "1.png", 4, 15, 25, lorem.paragraph(), "no")
mafin2 = Baking("Standart Mafin", "mafin", "2.png", 7, 615, 25, lorem.paragraph(), "yes")
mafin3 = Baking("Choco Mafin Prime", "mafin", "3.png", 64, 135, 255, lorem.paragraph(), "no")
fruit_cake = Baking("Fruit Cake", "cake", "4.png", 94, 15, 295, lorem.paragraph(), "yes")
honey_cake = Baking("Honey Cake", "cake", "5.png", 30, 15, 5, lorem.paragraph(), "yes")
ice_cream = Baking("Ice Creame", "ice_cream", "6.png", 99, 151, 225, lorem.paragraph(), "no")


Session = sessionmaker(bind=db_engine)
session = Session()

session.add(mafin1)
session.add(mafin2)
session.add(mafin3)
session.add(fruit_cake)
session.add(honey_cake)
session.add(ice_cream)

session.commit()

product_type = ["Choco Mafin", "Standart Mafin", "Choco Mafin Prime", "Fruit Cake", "Honey Cake", "Ice Creame"]
first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

def get_full_name():
    return str(choice(first_names) + " " + choice(last_names))


def get_baking():
    amount_baking = choice(range(1, 6))
    baking = sample(product_type, amount_baking)

    baking_and_amount = {}

    for i in baking:
        baking_and_amount[i] = choice(range(1, 20))

    return baking_and_amount


for _ in range(20):
    baking = get_baking()
    customer_name = get_full_name()

    baking_to_string = ""
    amount_baking = ""

    for i in baking:
        baking_to_string += i + ","
        amount_baking += str(baking[i]) + ","

    order = Order(customer_name, baking_to_string, amount_baking)
    session.add(order)

    session.commit()