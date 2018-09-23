from db import db

# both models/item.py and models/user.py
# extend db.Model
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


    # lazy='dynamic' self.items is no longer a list of items
    # it is a query builder with ability to look into items table
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name


    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        # .query comes from SQLAlchemy - we can build queries
        # SELECT * FROM items WHERE name=name
        return cls.query.filter_by(name=name).first()
        # we can do things like this...
        # ItemModel.query.filter_by(name=name).filter_by(id=1)

    def save_to_db(self):
        # this method is saving the model to the database
        # we're only inserting one object
        # useful for update and insert... "upserting"
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
