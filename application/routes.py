from __init__ import app, db_engine
from flask import render_template, request
from models import Baking, Order
from sqlalchemy.orm import sessionmaker


@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404'


@app.errorhandler(500)
def internal_server_error(e):
    return 'Error 500'


@app.route('/', methods=['GET'])
def index():
    Session = sessionmaker(bind=db_engine)
    session = Session()

    baking = session.query(Baking).all()
    print(baking)

    return render_template("index.html", baking=baking)


@app.route('/execute_filtre', methods=['GET', 'POST'])
def execute_filtre():

    if request.method == 'POST':

        parameters = {"product_type" : [], "fast_delivery": None}

        if request.form.get("fast_delivery"):
            parameters['fast_delivery'] = True
        
        if request.form.get("mafin_checkbox"):
            parameters['product_type'].append('mafin')

        if request.form.get("icecream_checkbox"):
            parameters['product_type'].append('ice_cream')

        if request.form.get("cake_checkbox"):
            parameters['product_type'].append('cake')

        price_in = request.form.get("price_in")
        price_out = request.form.get("price_out")

        Session = sessionmaker(bind=db_engine)
        session = Session()

        if price_in and price_out:

            if parameters['fast_delivery']:

                if parameters['product_type']:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.product_type.in_(tuple(parameters['product_type'])),
                        Baking.fast_delivery == "yes",
                        Baking.price >= price_in,
                        Baking.price <= price_out
                    ]
                    baking = query.filter(*query_filter)

                else:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.fast_delivery == "yes",
                        Baking.price >= price_in,
                        Baking.price <= price_out
                    ]
                    baking = query.filter(*query_filter)

            elif parameters['product_type']:
                query = session.query(Baking)
                query_filter = [
                    Baking.product_type.in_(tuple(parameters['product_type'])),
                    Baking.price >= price_in,
                    Baking.price <= price_out
                ]
                baking = query.filter(*query_filter)

            else:
                query = session.query(Baking)
                query_filter = [
                    Baking.price >= price_in,
                    Baking.price <= price_out
                ]
                baking = query.filter(*query_filter)


        elif price_in:

            if parameters['fast_delivery']:

                if parameters['product_type']:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.product_type.in_(tuple(parameters['product_type'])),
                        Baking.fast_delivery == "yes",
                        Baking.price >= price_in
                    ]
                    baking = query.filter(*query_filter)

                else:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.fast_delivery == "yes",
                        Baking.price >= price_in
                    ]
                    baking = query.filter(*query_filter)

            elif parameters['product_type']:
                query = session.query(Baking)
                query_filter = [
                    Baking.product_type.in_(tuple(parameters['product_type'])),
                    Baking.price >= price_in
                ]
                baking = query.filter(*query_filter)
                
            else:
                query = session.query(Baking)
                query_filter = [
                    Baking.price >= price_in
                ]
                baking = query.filter(*query_filter)

        elif price_out:

            if parameters['fast_delivery']:

                if parameters['product_type']:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.product_type.in_(tuple(parameters['product_type'])),
                        Baking.fast_delivery == "yes",
                        Baking.price <= price_out
                    ]
                    baking = query.filter(*query_filter)

                else:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.fast_delivery == "yes",
                        Baking.price <= price_out
                    ]
                    baking = query.filter(*query_filter)

            elif parameters['product_type']:
                query = session.query(Baking)
                query_filter = [
                    Baking.product_type.in_(tuple(parameters['product_type'])),
                    Baking.price <= price_out
                ]
                baking = query.filter(*query_filter)

            else:
                query = session.query(Baking)
                query_filter = [
                    Baking.price <= price_out
                ]
                baking = query.filter(*query_filter)
        else:

            if parameters['fast_delivery']:

                if parameters['product_type']:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.product_type.in_(tuple(parameters['product_type'])),
                        Baking.fast_delivery == "yes"
                    ]
                    baking = query.filter(*query_filter)

                else:
                    query = session.query(Baking)
                    query_filter = [
                        Baking.fast_delivery == "yes"
                    ]
                    baking = query.filter(*query_filter)

            else:
                query = session.query(Baking)
                query_filter = [
                    Baking.product_type.in_(tuple(parameters['product_type']))
                ]
                baking = query.filter(*query_filter)

    return render_template("index.html", baking=baking)


@app.route('/order', methods=['GET'])
def orders():
    product_type = ["Choco Mafin", "Standart Mafin", "Choco Mafin Prime", "Fruit Cake", "Honey Cake", "Ice Creame"]
    price_for_product = {}
    orders = []
    price_all_orders = 0
    

    Session = sessionmaker(bind=db_engine)
    session = Session()


    for type in product_type:
        record = session.query(Baking).filter_by(product_name = type).first()
        price_for_product[type] = record.price

    orders_from_db = session.query(Order).all()

    for order in orders_from_db:
        baking = (order.baking.split(","))[ : -1]
        amount = (order.amount.split(","))[ : -1]
        customer= {"name": order.customer_name, "baking": {}}

        for baking_item, amount_item in zip(baking, amount):
            customer["baking"][baking_item] = int(amount_item)

        total_price = 0

        for baking_name in price_for_product:
            if baking_name in [baking for baking in customer["baking"]]:
                total_price += customer["baking"][baking_name] * price_for_product[baking_name]

        customer["total_price"] = total_price

        orders.append(customer)

    for order_price in orders:
        price_all_orders += order_price['total_price']

    return render_template("order.html", orders = orders, price_all_orders = price_all_orders)
