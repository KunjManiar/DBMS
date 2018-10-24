from src.common.database import Database
import uuid
import datetime
from flask import session
class Staff():

    def __init__(self,email,name,date_of_birth,gender,address,password,mobile,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.mobile = mobile
        self.password = password

    def save_to_mongo(self):
        Database.insert(collection='staff',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'name' : self.name,
            'email' : self.email,
            'date_of_birth' : self.date_of_birth,
            'gender' : self.gender,
            'address' : self.address,
            'mobile' : self.mobile,
            'password' :self.password
        }

    @classmethod
    def from_id(cls,_id):
        staff = Database.find(collection='staff',
                              query={'_id':_id})
        return cls(**staff)

    @classmethod
    def from_email(cls,email):
        staff = Database.find_one(collection='staff',
                              query={'email': email})
        if staff is not None:
            return cls(**staff)

    @staticmethod
    def valid_login(email,password):
        staff = Staff.from_email(email)
        if staff is not None:
            return staff.password == password
        return False

    @staticmethod
    def login(email):
        session['email'] = email

#email,name,date_of_birth,gender,address,password,mobile
#Database.initialize()
#staff = Staff("bhuvnesh@gmail.com","Bhuvnesh",datetime.datetime(year=1998,month=12,day=2),"male","312","password",90804124201)
#print(staff.json())
#staff.save_to_mongo()
