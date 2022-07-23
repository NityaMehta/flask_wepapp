from flask import Flask,redirect,url_for,request,render_template,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import mysql.connector
import re

app=Flask(__name__)
conn = mysql.connector.connect(user='root', password='P@assw0rd',host='127.0.0.1',database='info')
cursor=conn.cursor()
app.secret_key='12345678'

@app.route('/home')
def home():
    if 'username' in session:
        username=session['username']
        password=session['password']
        cursor.execute('select contact from ABOUT where username=%s',(username,))
        c1=cursor.fetchone()
        msg='WELCOME %s' %(username)
        return render_template('homedemo.html',msg=msg)
    return redirect(url_for('login'))

@app.route('/contactus')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def about():
    return render_template('about.html')
@app.route('/login',methods=['POST','GET'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        session['username']=username
        session['password']=password
        cursor.execute('SELECT *FROM ABOUT WHERE username=%s AND password=%s',(username,password))
        u1=cursor.fetchone()
        if u1:
            cursor.execute('select contact from ABOUT where username=%s',(username,))
            c1=cursor.fetchone()
            msg='WELCOME %s' %(username)
            
            return redirect(url_for('home'))
        else:
            msg="INCORRECT Username/Password"
    return render_template('login.html',msg=msg)

@app.route('/logout')
def logout():
    session.pop('username',None)
    print('logged out')
    return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])
def register():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        contact=request.form['contact']

        cursor.execute('SELECT *FROM ABOUT WHERE username=%s',(username,))
        u1=cursor.fetchone()
        if u1:
            msg= "Username already exists"
        else:                         
            try: 
                cursor.execute('INSERT INTO ABOUT(Username,Password,contact) VALUES (%s,%s,%s)',(username,password,contact))
                conn.commit()
                msg="Succesfull"
                return render_template('login.html',msg=msg)
            except:
                conn.rollback()
                msg="try again"
        
    return render_template('registering.html',msg=msg)

if __name__=="__main__":
    app.run(host='0.0.0.0',port='8001')
conn.close()
    
