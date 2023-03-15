from __init__ import app


@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404'


@app.errorhandler(500)
def internal_server_error(e):
    return 'Error 500'


@app.route('/', methods=['GET'])
def index():
    return "Hello cafe"
