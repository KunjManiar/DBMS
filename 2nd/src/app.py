import datetime

from src.common.database import Database
from flask import Flask, render_template, request, session, make_response

from src.models.order_by_customer import Order_by_customer
from src.models.order_details_customer import Order_details_customer
from src.models.payment_to_supplier import Payment_to_supplier
from src.models.order_details_supplier import Order_details_supplier
from src.models.product import Product
from src.models.customer import Customer
from src.models.staff import Staff
from src.models.supplier import Supplier

__author__ = 'kunj'

app = Flask(__name__)
app.secret_key = "KUNJ"
Database.initialize()
flag = 0

flag2,order_id=0,None

def get_customer(email):
    customer = Customer.from_email(email)
    if customer is None:
        staff = Staff.from_email(email)
        if staff is None:
            return None
        return staff
    return customer


@app.route('/')
def home_template():
    global flag
    if flag == 0:
        session['email'] = None
        flag += 1
    # print(session['email'])
    customer = get_customer(session['email'])
    if customer is not None:
        customer = Customer.from_email(session['email'])
        if customer is not None:
            return render_template('index.html', email=session['email'],
                                   name=customer.name if customer is not None else None)
        else:
            customer = Staff.from_email(session['email'])
        if customer is not None:
            return render_template('Staff_Login_ifame.html', email=session['email'],
                                   name=customer.name if customer is not None else None)

    return render_template('index.html', email=session['email'], name=customer.name if customer is not None else None)


@app.route('/login')
def login_template():
    customer = get_customer(session['email'])
    return render_template('login.html', email=session['email'], name=customer.name if customer is not None else None)


@app.route('/staff_login')
def staff_login():
    return render_template('staff_Login.html', )


@app.route('/customers_list')
def customers_list():
    customers = Customer.get_customer()
    return render_template('staff_customers_list.html', customers=customers)


@app.route('/add_product')
def add_product():
    return render_template('Staff_Add_Product.htm')

@app.route('/create_product',methods=['POST'])
def create_product():
    name = request.form['name']
    category = request.form['category']
    supplier = request.form['supplier']
    quantity = request.form['quantity']
    unit_price = request.form['unit_price']
    unit_selling_price = request.form['unit_selling_price']
    unit_in_order = request.form['unit_in_order']
    reorder_level = request.form['reorder_level']
    supplier = Product(name,category,supplier,quantity,unit_price,unit_selling_price,unit_in_order,reorder_level)
    supplier.save_to_mongo()
    return render_template('Staff_Add_Product.htm', message="Successful")
    # <!--name,category,supplier,quantity,unit_price,unit_selling_price,available_stock,unit_in_order,reorder_level-->


@app.route('/add_trans')
def add_trans():
    return render_template('Staff_Add_Transaction.htm')


@app.route('/add_supplier')
def add_supplier():
    return render_template('Staff_Add_Supplier.htm')


@app.route('/update_stocks')
def update_stocks():
    return render_template('Staff_Updating_stocks.htm')


@app.route('/auth_login', methods=['POST'])
def login_user():
    email = request.form['Email']
    password = request.form['Password']

    if Customer.valid_login(email, password):
        Customer.login(email)
        customer = Customer.from_email(email)
        return render_template("index.html", name=customer.name if customer is not None else None,
                               email=session['email'])

    elif Staff.valid_login(email, password):
        Staff.login(email)
        staff = Staff.from_email(email)
        return render_template("Staff_Login_ifame.html", name=staff.name if staff is not None else None,
                               email=session['email'])

    else:
        session['email'] = None
        return render_template("login.html", error="Invalid Email or Password")


@app.route('/auth_register', methods=['POST', 'GET'])
def register_user():
    if request.method == 'GET':
        return render_template("Staff_Login.html")
    else:
        email = request.form['Email']
        password = request.form['Password']
        gst = request.form['Gst']
        username = request.form['Username']
        address = request.form['Address']
        mobile = request.form['Mobile']
        customer = Customer(username, gst, email, address, mobile, password)
        customer.save_to_mongo()
        # name,gst_no,email,address,mobile,password,
        staff = Staff.from_email(session['email'])
        if staff is not None:
            return render_template("Staff_Login.html", message="Successful")
        else:
            Customer.login(email)
        return render_template("index.html", email=session['email'], name=username)


@app.route('/logout')
def user_logout():
    session['email'] = None
    global flag
    flag = 0
    return make_response(home_template())


@app.route('/checkout', methods=['POST'])
def checkout():
    customer = get_customer(session['email'])
    return render_template("checkout.html", email=session['email'],
                           name=customer.name if customer is not None else None)


@app.route('/about')
def about():
    customer = get_customer(session['email'])
    return render_template("about.html", email=session['email'], name=customer.name if customer is not None else None)


@app.route('/drinks')
def drinks():
    customer = get_customer(session['email'])
    return render_template("drinks.html", email=session['email'], name=customer.name if customer is not None else None)


@app.route('/vegetables')
def vegetables():
    customer = get_customer(session['email'])
    return render_template("vegetables.html", email=session['email'],
                           name=customer.name if customer is not None else None)


@app.route('/kitchen')
def kitchen():
    customer = get_customer(session['email'])
    return render_template("kitchen.html", email=session['email'], name=customer.name if customer is not None else None)


@app.route('/contact_us')
def contact_us():
    customer = get_customer(session['email'])
    return render_template("mail.html", email=session['email'],
                           name=customer.name if customer is not None else None)


@app.route('/payment')
def payment():
    customer = get_customer(session['email'])
    return render_template("payment.html", email=session['email'], name=customer.name if customer is not None else None)


@app.route('/create_supplier', methods=['POST'])
def create_supplier():
    # company_name,staff_id,contact_person_name,gst_no,email_id,address,mobile
    company_name = request.form['Companyname']
    staff_id = session['email']
    contact_person_name = request.form['Contact_person_name']
    gst_no = request.form['Gst_no']
    email_id = request.form['Email']
    address = request.form['Address']
    mobile = request.form['Mobile']
    supplier = Supplier(company_name, staff_id, contact_person_name, gst_no, email_id, address, mobile)
    supplier.save_to_mongo()
    return render_template("Staff_Add_Supplier.htm", message="Successful")


@app.route('/c_transaction', methods=['POST'])
def create_transaction():
    # id_of_order, mode, total_payment, credited_amount, debited_amount, date_of_debit, date_of_credit
    id_of_order = request.form['Oid']
    mode = request.form['Mode']
    total_payment = request.form['total_payment']
    credited_amount = request.form['Credited_amount']
    debited_amount = request.form['Debited_amount']
    date_of_debit = request.form['dod']
    date_of_credit = request.form['doc']
    supplier = Payment_to_supplier(id_of_order, mode, total_payment, credited_amount, debited_amount, date_of_debit, date_of_credit)
    supplier.save_to_mongo()
    return render_template("Staff_Add_Transaction.htm", message="Successful")


@app.route('/create_order', methods=['POST'])
def create_order():
    id_of_order = request.form['id_of_order']
    quantity = request.form['Quantity']
    product_id = request.form['product_id']
    price = request.form['price']
    supplier = Order_details_supplier(id_of_order, quantity, product_id, price)
    supplier.save_to_mongo()
    return render_template("staff_Updating_Stocks.htm", message="Successful")

@app.route('/caaart',methods=['POST'])
def cart():
    x = request.data
    print(x)
    global flag2
    flag2 = 0
    global order_id
    order_id = None
    return make_response(checkout())


@app.route('/order_details_customer',methods=['POST'])
def order_details_customer():
    #quantity, product_id, price,order_id
    quantity = request.form['add']
    product_id = request.form['product_id']
    price = request.form['amount']
    #total_quantity, total_amount, date_of_order, customer_id, order_completion_date = None, staff_id = None,
    global flag2,order_id
    if flag2 == 0:
        order = Order_by_customer(0,0,datetime.datetime.utcnow(),session["email"])
        order.save_to_mongo()
        flag2+=1
        order_id = order._id
    order_l_id = order_id
    order.total_quantity+=int(quantity)
    order.total_amount+=int(price)
    order_d_c = Order_details_customer(quantity,product_id, price,order_l_id)
    order_d_c.save_to_mongo()
    return make_response(home_template())

if __name__ == '__main__':
    app.run(port=4999)
