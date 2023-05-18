from __init__ import app, db_engine
from flask import render_template, request
from models import Baking
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


@app.route('/orders', methods=['GET'])
def orders():
    return "orders"
