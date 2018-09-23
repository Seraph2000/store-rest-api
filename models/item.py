from db import db

# both models/item.py and models/user.py
# extend db.Model
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

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
