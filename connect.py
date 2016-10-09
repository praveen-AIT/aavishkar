from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import db
from models import Blogpost

app = Flask(__name__)
engine = create_engine('postgres://rqltuxsejkcyrg:vNtgV4hVy6HeU33-EAaXHramUU@ec2-54-221-255-192.compute-1.amazonaws.com:5432/d8n8d93ibr11sf')
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
data = Blogpost(victim="AIT, PUNE", hospitals="AFMC", distance=70)
#db.session.add(data)
#db.session.commit()
#a = session.query(Blogpost).all()
#print(a)
b = Blogpost.query.all()
print(b)