import uuid
from src.common.database import Database

class Supplier():

    def __init__(self,company_name,staff_id,contact_person_name,gst_no,email_id,address,mobile,_id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.company_name = company_name
        self.staff_id = staff_id
        self.contact_person_name = contact_person_name
        self.gst_no = gst_no
        self.email = email_id
        self.address = address
        self.mobile = mobile

    def save_to_mongo(self):
        Database.insert(collection='supplier',
                        data=self.json())

    def json(self):
        return {
            '_id' : self._id,
            'company_name' : self.company_name,
            'staff_id' : self.staff_id,
            'contact_person_name' : self.contact_person_name,
          #  'contact_person_lname' : self.contact_person_lname,
            'gst_no' : self.gst_no,
            'email' :self.email,
            'address' : self.address,
			'mobile' : self.mobile
        }

    @classmethod
    def from_id(cls,_id):
        supplier = Database.find(collection='supplier',
                              query={'_id':_id})
        return cls(**supplier)

    @classmethod
    def from_email(cls,email):
        supplier = Database.find(collection='supplier',
                              query={'_id': _id})
        return cls(**supplier)
