from flask import Flask
from sqlalchemy import create_engine
from config import DB_PATH


# Create an application and a database engine
app = Flask(__name__)
db_engine = create_engine(DB_PATH)


# Load App Settings
app.config.from_pyfile('config.py')

# import routes
from routes import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1194)