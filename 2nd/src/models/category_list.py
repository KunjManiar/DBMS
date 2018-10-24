import uuid
from src.common.database import Database


class Category_list():

    def __init__(self, selling_price,category_name, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.selling_price = selling_price
        self.category_name = category_name

    def save_to_mongo(self):
        Database.insert(collection='category_list',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'category_name': self.category_name,
            'selling_price': self.selling_price
        }

    @classmethod
    def from_id(cls, _id):
        categorylist = Database.find(collection='category_list',
                                     query={'_id': _id})
        return cls(**categorylist)
