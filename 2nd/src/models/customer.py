from src.common.database import Database
from flask import Flask,session
import uuid

class Customer():

    def __init__(self,name,gst_no,email,address,mobile,password,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        #self.staff_id = staff_id
        self.gst_no = gst_no
        self.email = email
        self.address = address
        self.mobile = mobile
        self.password = password

    def save_to_mongo(self):
        Database.insert(collection='customer',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'name' : self.name,
         #   'staff_id' : self.staff_id,
            'gst_no' : self.gst_no,
            'email' : self.email,
            'address' : self.address,
            'mobile' : self.mobile,
            'password' : self.password
        }

    @classmethod
    def from_id(cls, _id):
        customer = Database.find_one(collection='customer',
                              query={'_id': _id})
        if customer is not None:
            return cls(**customer)
        else:
            return None

    @classmethod
    def from_email(cls, email):
        customer = Database.find_one(collection='customer',
                              query={'email': email})
        if customer is not None:
            return cls(**customer)
        else:
            return None

    @staticmethod
    def valid_login(email,password):
        staff = Customer.from_email(email)
        if staff is not None:
            return staff.password == password
        return False

    @staticmethod
    def login(email):
        session['email'] = email

    @classmethod
    def get_customer(cls):
        customers = Database.find_collection('customer')

        return [cls(**customer) for customer in customers]