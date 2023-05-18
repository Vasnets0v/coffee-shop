from sqlalchemy.orm import sessionmaker
from lorem_text import lorem
from random import choice, randrange, randint
from __init__ import db_engine
from models import Baking, Customer

Session = sessionmaker(bind=db_engine)
session = Session()

mafin1 = Baking("Choco Mafin", "mafin", "1.png", 344, 15, 25, lorem.paragraph(), "yes")
mafin2 = Baking("Standart Mafin", "mafin", "2.png", 344, 615, 25, lorem.paragraph(), "yes")
mafin3 = Baking("Choco Mafin Prime", "mafin", "3.png", 64, 135, 2355, lorem.paragraph(), "no")
fruit_cake = Baking("Fruit Cake", "cake", "4.png", 3144, 15, 295, lorem.paragraph(), "yes")
honey_cake = Baking("Honey Cake", "cake", "5.png", 3445, 15, 5, lorem.paragraph(), "yes")
ice_cream = Baking("Ice Creame", "ice_cream", "6.png", 34, 151, 225, lorem.paragraph(), "no")

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


def get_phone_number():
    ph_no = []
  
    ph_no.append(randint(6, 9))

    for i in range(1, 9):
        ph_no.append(randint(0, 9))
    
    return int("380" + "".join(str(num) for num in ph_no))


for _ in range(randrange(0, 101, 2)):
    # customer = Customer(str(choice(first_names) + " " + choice(last_names)), 3647)
    customer = Customer("23453456", 547)
    session.add(customer)

session.commit()
