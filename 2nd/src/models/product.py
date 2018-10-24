from src.common.database import Database
import uuid

class Product():

    def __init__(self,name,category,supplier,quantity,unit_price,unit_selling_price,unit_in_order,reorder_level,available_stock=None,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.category = category
        self.supplier = supplier
        self.quantity = quantity
        self.unit_price = unit_price
        self.unit_selling_price = unit_selling_price
        self.available_stock = 0 if available_stock is None else available_stock
        self.unit_in_order = unit_in_order
        self.reorder_level = reorder_level

    def save_to_mongo(self):
        Database.insert(collection='product',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'name' : self.name,
            'category' : self.category,
            'supplier' : self.supplier,
            'quantity' : self.quantity,
            'unit_price' : self.unit_price,
            'unit_selling_price' :self.unit_selling_price,
            'available_stock' : self.available_stock,
            'unit_in_order' : self.unit_in_order,
            'reorder_level' : self.reorder_level
        }

    @classmethod
    def from_id(cls, _id):
        staff = Database.find(collection='staff',
                              query={'_id': _id})
        return cls(**staff)
