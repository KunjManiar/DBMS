import uuid
from src.common.database import Database

class Order_to_supplier():

    def __init__(self,supplier_id,staff_id,total_quantity,error_msg,total_amount,date_of_order,order_receiving_date,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.supplier_id = supplier_id
        self.staff_id = staff_id
        self.total_quantity = total_quantity
        self.error_msg = error_msg
        self.total_amount = total_amount
        self.date_of_order = date_of_order
        self.order_receiving_date = order_receiving_date

    def save_to_mongo(self):
        Database.insert(collection='ordertosupplier',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'supplier_id' : self.supplier_id,
            'staff_id' : self.staff_id,
            'total_quantity' : self.total_quantity,
            'error_msg' : self.error_msg,
            'total_amount' : self.total_amount,
            'date_of_order' :self.date_of_order,
            'order_receiving_date' : self.order_receiving_date
        }

    @classmethod
    def from_id(cls,_id):
        ordertosupplier = Database.find(collection='ordertosupplier',
                              query={'_id':_id})
        return cls(**ordertosupplier)

   
