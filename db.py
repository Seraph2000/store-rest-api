from flask_sqlalchemy import SQLAlchemy

# this is an object
# it's going to link to our flask app and look at
# all the objects we tell it to
# map those objects to rows in a db
db = SQLAlchemy()
