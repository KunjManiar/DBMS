from src.common.database import Database
import datetime
import uuid

class Payment_by_customer():

    def __init__(self,order_id,mode,total_payment,credited_amount,date_of_debit,date_of_credit,_id):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.order_id = order_id
        self.mode = mode
        self.total_payment = total_payment
        self.credited_amount = credited_amount
        self.date_of_debit = date_of_debit
        self.date_of_credit = date_of_credit

    def save_to_mongo(self):
        Database.insert(collection='payment_by_customer',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'order_id' : self.order_id,
            'mode' : self.mode,
            'total_payment' : self.total_payment,
            'credited_amount' : self.credited_amount,
            'date_of_debit' : self.date_of_debit,
            'date_of_credit' : self.date_of_credit
        }

    @classmethod
    def from_id(cls, _id):
        payment_by_customer = Database.find(collection='payment_by_customer',
                              query={'_id': _id})
        return cls(**payment_by_customer)
