import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
# SQLAlchemy database is going to live at the root of our project
# doesn't have to be sqlite - could be mysql, postgresql, etc...
# SQLAlchemy will JUST WORK!
# only need to change THIS LINE OF CODE!
# fetch app's confg value - os.environ.get('DATABASE_URL')
# DATABASE_URL is created in Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# to know when an object changed but not saved
# Flask checks for changes
# this turns it off. flask_sqlalchemy library has own tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# replace with something long and complicated for production
app.secret_key = 'seraphina'
# allow us to add resources to it
api = Api(app)

# initialise jwt object
# JWT creates a new endpoint - /auth
# when we call /auth, we send it a username and a password
jwt = JWT(app, authenticate, identify)

# add the resources here, with correct corresponding endpoints!
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')

api.add_resource(UserRegister, '/register')

# this never runs on Heroku
# uwsgi runs the app for us!
if __name__ == '__main__':
    # circular imports
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
