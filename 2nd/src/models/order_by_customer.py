import uuid
from src.common.database import Database


class Order_by_customer():

    def __init__(self, total_quantity, total_amount, date_of_order,customer_id,order_completion_date=None,staff_id=None, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.total_quantity = total_quantity
      #  self.error_message = error_message
        self.total_amount = total_amount
        self.date_of_order = date_of_order
        self.order_completion_date = order_completion_date
        self.customer_id = customer_id
        self.staff_id = staff_id


    def save_to_mongo(self):
        Database.insert(collection='order_by_customer',
                        data= self.json())


    def json(self):
        return {
            '_id': self._id,
            'total_quantity': self.total_quantity,
        #    'error_msg': self.error_message,
            'total_amt': self.total_amount,
            'date_of_order': self.date_of_order,
            'order_completion_date': self.order_completion_date,
            'customer_id': self.customer_id,
            'staff_id': self.staff_id
        }


    @classmethod


    def from_id(cls, _id):
        order_by_customer = Database.find(collection='order_by_customer',
                              query={'_id': _id})
        return cls(**order_by_customer)
