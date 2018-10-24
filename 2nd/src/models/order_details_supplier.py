import uuid
from src.common.database import Database

class Order_details_supplier():

    def __init__(self, id_of_order,quantity, product_id, price, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.id_of_order = id_of_order
        self.quantity = quantity
        self.product = product_id
        self.price = price

    def save_to_mongo(self):
        Database.insert(collection='order_details_supplier',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'id_of_order': self.id_of_order,
            'quantity': self.quantity,
            'product': self.product,
            'price': self.price
        }

    @classmethod
    def from_id(cls, _id):
        order_details_customer = Database.find(collection='order_details_supplier',
                                               query={'_id': _id})
        return cls(**order_details_customer)
