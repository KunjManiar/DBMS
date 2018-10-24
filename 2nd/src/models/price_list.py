import uuid
from src.common.database import Database

class Price_list():

    def __init__(self,selling_price,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.selling_price = selling_price

    def save_to_mongo(self):
        Database.insert(collection='price_list',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'selling_price' : self.selling_price
        }

    @classmethod
    def from_id(cls,_id):
        pricelist = Database.find(collection='price_list',
                              query={'_id':_id})
        return cls(**pricelist)

