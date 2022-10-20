#importing libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

#connecting to mysql server
app = Flask(__name__)
conn = MySQLdb.connect("localhost","root","Ash#010902","scraping" )
cursor = conn.cursor()
mysql = MySQL(app)

#login page route
@app.route('/', methods = ['GET', 'POST'])
def login():
    #condition to check entered credentials
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('state'))
    return render_template('LOGIN.html')

#states page route
@app.route('/state', methods=['GET','POST'])
def state():
    return render_template('state.html')

#categories page route
@app.route('/Telangana', methods=['GET','POST'])
def Telangana():
    return render_template('Telangana.html')

#sub categories page route
@app.route('/Aerospace_and_Aviation', methods=['GET','POST'])
def Aerospace_and_Aviation():
    return render_template('Aerospace_and_Aviation.html')

#sub categories page route
@app.route('/Engineering_and_Technology', methods=['GET','POST'])
def Engineering_and_Technology():
    return render_template('Engineering_and_Technology.html')

#sub categories jobs and company details page route
@app.route('/Aircraft_maintenance', methods=['GET','POST'])
def Aircraft_maintenance():
    cursor.execute("SELECT * FROM jobs_details_aircraft_maintenance")
    data1 = cursor.fetchall()
    cursor.execute("SELECT * FROM company_details WHERE Sub_category='Aircraft maintenance'")
    data2 = cursor.fetchall()
    return render_template('Aircraft_maintenance.html', data1=data1, data2=data2)

#sub categories jobs and company details page route
@app.route('/Ground_operation_manager', methods=['GET','POST'])
def Ground_operation_manager():
    cursor.execute("SELECT * FROM jobs_details_ground_operation_manager")
    data1 = cursor.fetchall()
    cursor.execute("SELECT * FROM company_details WHERE Sub_category='Ground operation manager'")
    data2 = cursor.fetchall()
    return render_template('Ground_operation_manager.html', data1=data1, data2=data2)

#sub categories jobs and company details page route
@app.route('/Computer_engineer', methods=['GET','POST'])
def Computer_engineer():
    cursor.execute("SELECT * FROM jobs_details_computer_engineer")
    data1 = cursor.fetchall()
    cursor.execute("SELECT * FROM company_details WHERE Sub_category='Computer engineer'")
    data2 = cursor.fetchall()
    return render_template('Computer_engineer.html', data1=data1, data2=data2)

#sub categories jobs and company details page route
@app.route('/Electrical_engineer', methods=['GET','POST'])
def Electrical_engineer():
    cursor.execute("SELECT * FROM jobs_details_electrical_engineer")
    data1 = cursor.fetchall()
    cursor.execute("SELECT * FROM company_details WHERE Sub_category='Electrical engineer'")
    data2 = cursor.fetchall()
    return render_template('Electrical_engineer.html', data1=data1, data2=data2)

#search bar route
@app.route('/search', methods=['GET','POST'])
def search():
    var = request.form.get('search')
    if var=='Aerospace and Aviation':
        return render_template('Aerospace_and_Aviation.html')
    if var=='Engineering and Technology':
        return render_template('Engineering_and_Technology.html')
    if var=='Computer Engineer':
        return redirect(url_for('Computer_engineer'))
    if var=='Electrical Engineer':
        return redirect(url_for('Electrical_engineer'))
    if var=='Aircraft Maintenance':
        return redirect(url_for('Aircraft_maintenance'))
    if var=='Ground Operation Manager':
        return redirect(url_for('Ground_operation_manager'))
    if var=='Telangana':
        return redirect(url_for('Telangana'))

#to run the code
app.run(debug=True)