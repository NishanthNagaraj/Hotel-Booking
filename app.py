from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from datetime import datetime
import MySQLdb.cursors
import re
  
def count_day(d0,d1):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(d0, date_format)
    b = datetime.strptime(d1, date_format)
    delta = b - a
    return (delta.days)

app = Flask(__name__) 
app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'tuturew'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)
@app.route('/')
def hello_world():
    return render_template("login.html")
@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/landing/room_selection')
def room_selection():
    return render_template('room_selection.html')  
# @app.route('/landing/room_selection/confirmation', methods =['GET', 'POST']) 
# def confirmation():
#     return render_template('confirmation.html')
@app.route('/landing/room_selection/confirmation/payment')
def payment():
    return render_template('payment.html') 
@app.route('/landing/room_selection/profile')
def profile():
    return render_template('profile.html')
@app.route('/')
@app.route('/landing', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            session['phone']=account[3]
            session['email']=account[2]
            session['username'] = account[1]
            session['user_id'] = account[0]
            session['password']=account[4]
            session['loggedin'] = True
            # cursor = mysql.connection.cursor()
            # cursor.execute('SELECT * FROM user_activity WHERE session_id=(SELECT max(session_id) FROM user_activity)')
            # ses=cursor.fetchone()
            # t=ses[0]
            # t=int(t)+1
            # session['id']=t
            cursor.execute('INSERT INTO user_activity (username,email,accounts_id) VALUES ( % s, % s, %s)', (session['username'],session['email'],session['user_id']))
            mysql.connection.commit()
            msg = 'Logged in successfully !'
            return render_template('landing.html')
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg = msg)
  

  
@app.route('/signup', methods =['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST'and 'username' in request.form and 'email' in request.form and 'phone' in request.form and 'password' in request.form and 'date' in request.form and 'gender' in request.form: 
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confirmpassword=request.form['confirmpassword']
        date = request.form['date']
        gender = request.form['gender']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email or not date or not gender or not phone:
            msg = 'Please fill out the form !'
        elif password!=confirmpassword:
            msg='passwords dont match !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s,%s,%s,%s)', (username,email,phone,password,date,gender))
            mysql.connection.commit()
        # msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html',msg=msg)

@app.route('/login', methods =['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.pop('total_price', None)
        session.pop('guests', None)
        session.pop('days', None)
        session.pop('checkout', None)
        session.pop('checkin', None)
        session.pop('price', None)
        session.pop('breakfast', None)
        session.pop('room_name', None)
        session.pop('room_id',None)
        session.pop('id', None)
        session.pop('loggedin', None)
        session.pop('password', None)
        session.pop('user_id', None)
        session.pop('username', None)
        session.pop('email', None)
        session.pop('phone',None)
        return redirect(url_for('hello_world'))
    session.pop('total_price', None)
    session.pop('guests', None)
    session.pop('days', None)
    session.pop('checkout', None)
    session.pop('checkin', None)
    session.pop('price', None)
    session.pop('breakfast', None)
    session.pop('room_name', None)
    session.pop('room_id',None)
    session.pop('id', None)
    session.pop('loggedin', None)
    session.pop('password', None)
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('phone',None)
    return redirect(url_for('hello_world'))    
        

@app.route('/landing/room_selection')
@app.route('/landing/room_selection', methods =['GET', 'POST'])
def select():
    msg = ''
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        if request.form['submit_button'] == '1':            
            cursor.execute('SELECT * FROM rooms WHERE id = 1')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        elif request.form['submit_button'] == '2':
            cursor.execute('SELECT * FROM rooms WHERE id = 2')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        elif request.form['submit_button'] == '3':
            cursor.execute('SELECT * FROM rooms WHERE id = 3')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        elif request.form['submit_button'] == '4':
            cursor.execute('SELECT * FROM rooms WHERE id = 4')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        elif request.form['submit_button'] == '5':
            cursor.execute('SELECT * FROM rooms WHERE id = 5')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        elif request.form['submit_button'] == '6':
            cursor.execute('SELECT * FROM rooms WHERE id = 6')
            room = cursor.fetchone()
            session['room_id']=room[0]
            session['room_name']=room[1]
            session['breakfast']=room[2]
            session['price']=room[3]
        mysql.connection.commit()  
        print('posted')
        session['checkin']=request.form['checkin']
        session['checkout']=request.form['checkout']
        session['days']=count_day(session['checkin'],session['checkout'])
        session['guests']=request.form['guests']
        session['total_price']=session['days']*session['price']
        return render_template('confirmation.html')
    return render_template('room_selection.html')

@app.route('/landing/room_selection/confirmation/payment')
@app.route('/landing/room_selection/confirmation/payment', methods =['GET', 'POST'])
def pay():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO bookings VALUES (NULL, % s, % s, % s,%s,%s,%s,%s,%s,NOW())', (session['user_id'],session['room_id'],session['room_name'],session['checkin'],session['checkout'],session['days'],session['guests'],session['total_price']))
        mysql.connection.commit()
    return render_template('success.html')
@app.route('/landing/room_selection/profile')
@app.route('/landing/room_selection/profile', methods =['GET', 'POST'])
def edit():
    if request.method=='POST':
        session['username']=request.form['username']
        session['phone']=request.form['phone']
        session['email']=request.form['email']
        cursor=mysql.connection.cursor()
        i=session['user_id']
        i=int(i)
        cursor.execute("""UPDATE accounts SET username = '{}', email = '{}', phone ='{}' WHERE id ={}""".format(session['username'], session['email'], session['phone'], i))
        mysql.connection.commit()
    return render_template('profile.html')

@app.route('/landing/room_selection/history')
@app.route('/landing/room_selection/history',methods=['GET','POST'])
def history():
    i=session['user_id']
    i=int(i)
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM bookings WHERE accounts_id = {}'.format(i))
    data=cursor.fetchall()
    mysql.connection.commit()
    return render_template('history.html',data=data)
# @app.route('/landing/room_selection/profile')
# @app.route('/landing/room_selection/profile', methods =['GET', 'POST'])
# def password():
#     if request.method=='POST':
#         current_password = request.form['current_password']
#         new_password=request.form['new_password']
#         if current_password==new_password:
#             cursor=mysql.connection.cursor()
#             i=session['user_id']
#             i=int(i)
#             cursor.execute("""UPDATE accounts SET password = '{}' WHERE id ={}""".format(session['password'], i))
#             mysql.connection.commit()
#     return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)