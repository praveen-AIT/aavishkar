# Imports
from app import db

# Create database
from models import Blogpost

db.create_all()

# Adding data
def add_post():
	print("working")
	db.session.add(Blogpost("AJAY","AFMC", 80.33, 85.45))
	db.session.commit()
	print("DATA ADDED")
