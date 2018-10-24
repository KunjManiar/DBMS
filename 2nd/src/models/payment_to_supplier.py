import uuid
from src.common.database import Database

class Payment_to_supplier():

    def __init__(self,id_of_order,mode,total_payment,credited_amount,debited_amount,date_of_debit,date_of_credit,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.id_of_order = id_of_order
        self.mode = mode
        self.total_payment = total_payment
        self.credited_amount = credited_amount
        self.debited_amount = debited_amount
        self.date_of_debit = date_of_debit
        self.date_of_credit = date_of_credit 

    def save_to_mongo(self):
        Database.insert(collection='payment_to_supplier',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'id_of_order' : self.id_of_order,
            'mode' : self.mode,
            'total_payment' : self.total_payment,
            'credited_amount' : self.credited_amount,
            'debited_amount' : self.debited_amount,
            'date_of_debit' : self.date_of_debit,
            'date_of_credit' :self.date_of_credit
        }

    @classmethod
    def from_id(cls,_id):
        paymenttosupplier = Database.find(collection='payment_to_supplier',
                              query={'_id':_id})
        return cls(**paymenttosupplier)
