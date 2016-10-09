from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
# from flask.ext.heroku import Heroku
import time
from functools import wraps
import sqlite3
# from sms import send
from datetime import datetime
#from pytz import timezone


# Application object
app = Flask(__name__)
app.secret_key = "praveen"

#heroku = Heroku(app)
# Database object
db = SQLAlchemy(app)

# Sqlalchemy configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from db_create import *
from models import Blogpost

# Login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('login'))
	return wrap


# Routes
@app.route('/login', methods=["GET", "POST"])
def login():
	error = None
	if(request.method=="POST"):
		if(request.form['username'] == "admin" and request.form['password'] == "jenny"):
			session['logged_in'] = True
			return redirect(url_for('home'))

		else:
			error = "Invalid Credentials!!!"
	return render_template("login.html", error=error)

@app.route('/home', methods=["GET", "POST"])
def home():
	with sqlite3.connect("lock.db") as connection:
		cur = connection.cursor()

		# date from posts table
		cur1 = cur.execute("select hospitals from accidents")
		dat_db1 = [row[0] for row in cur1.fetchall()]
		#print(dat_db1[1])
		for hosp in dat_db1:
			print hosp

		cur1 = cur.execute("select victim from accidents")
		dat_db2 = [row[0] for row in cur1.fetchall()]
		for vict in dat_db2:
			print vict

	db.create_all()
	db.session.commit()
	return render_template("home.html", vict=dat_db2, hosp=dat_db1)

if __name__ == '__main__':
	app.run(debug=True)
