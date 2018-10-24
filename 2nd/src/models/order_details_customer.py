import uuid
from src.common.database import Database


class Order_details_customer():

    def __init__(self, quantity, product_id, price,order_id, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.quantity = quantity
        self.product = product_id
        self.order_id = order_id
        self.price = price


    def save_to_mongo(self):
        Database.insert(collection='order_details_customer',
                        data=self.json())


    def json(self):
        return {
            '_id': self._id,
            'quantity': self.quantity,
            'order_id' : self.order_id,
            'product': self.product,
            'price': self.price
        }


    @classmethod
    def from_id(cls, _id):
        order_details_customer = Database.find(collection='order_details_customer',
                                               query={'_id': _id})
        return cls(**order_details_customer)
