import sys
import MySQLdb as mdb

reload(sys)
sys.setdefaultencoding('utf8') 

from flask import Flask
from flask import render_template
from flask import session
from flask import request
app = Flask(__name__)

con = mdb.connect('localhost', 'root', 'wngml5436', 'oss');
@app.route('/')
def login_form():
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Members WHERE StudentId="+request.form['studentid'])
            if cur.rowcount == 0:
                cur.close()
                return render_template('default_form.html', message = 'Your studentid is not registered yet, please signup')
            
            rows = cur.fetchall()
            if (rows[0]["Password"]!=request.form['password']):
                cur.close()
                return render_template('default_form.html', message = 'Your password is wrong')

            cur.execute("SELECT * FROM Members WHERE StudentId="+request.form['studentid']+" and Password=\'"+request.form['password']+"\'")
            if cur.rowcount == 0:
                cur.close()
                return render_template('default_form.html', message = 'Your password is wrong')
            rows = cur.fetchall()
        
            session['logged_in'] = True
            return render_template('default_form.html', message = "Welcome!!!")
    else:
        return render_template('default_form.html', message = 'Wrong approach')

@app.route('/signup_form')
def signup_form():
    return render_template('signup_form.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Members WHERE StudentId="+request.form['studentid'])
            if cur.rowcount > 0:
                cur.close()
                return render_template('default_form.html', message = 'Your studentid is already registered')
            cur.execute("INSERT INTO Members(StudentId, PhoneNumber, LastName, FirstName, Password) VALUES("+request.form['studentid']+","+request.form['phonenumber']+",\'"+ request.form['lastname']+"\', \'"+ request.form['firstname']+"\', \'"+ request.form['password']+"\')")
        return render_template('default_form.html', message = "Welcome " + request.form['firstname'] )
    else:
        return render_template('default_form.html', message = 'Wrong approach')

@app.route('/withdraw_form')
def withdraw_form():
    return render_template('withdraw_form.html')

@app.route('/withdraw', methods=['POST'])
def withdraw():
    if request.method == 'POST':
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Members WHERE StudentId="+request.form['studentid']+" and PhoneNumber="+request.form['phonenumber'])
            if cur.rowcount == 0:
                cur.close()
                return render_template('default_form.html', message = 'There is no such a member' )
            
            rows = cur.fetchall()
            if rows[0]['Password']!=str(request.form['password']):
                cur.close()
                return render_template('default_form.html', message = 'You put wrong password')
            cur.execute("DELETE FROM Members WHERE StudentId="+request.form['studentid']+" and Password=\'"+request.form['password']+"\'")
            return render_template('default_form.html', message="Goodbye")
    else:
        return render_template('default_form.html', message = 'Wrong approach')

@app.route('/find_form')
def find_form():
    return render_template('find_form.html')

@app.route('/find', methods=['POST'])
def find():
    if request.method == 'POST':
        with con:
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Members WHERE StudentId="+request.form['studentid']+" and PhoneNumber="+request.form['phonenumber'])
            if cur.rowcount == 0:
                cur.close()
                return render_template('default_form.html', message = 'There is no such a member' )
            
            rows = cur.fetchall()
            user = rows[0]['FirstName']
            lastname = rows[0]['LastName']  
            cur.execute("UPDATE Members SET Password=\'"+request.form['password']+"\' WHERE StudentId="+request.form['studentid'])
            return render_template('default_form.html', message = "Your password is updated")
    else:
        return render_template('default_for.html', message = 'Wrong approach')

app.secret_key = 'sample_secret_key'

if __name__=='__main__':
    app.run()

