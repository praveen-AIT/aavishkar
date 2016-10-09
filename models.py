from app import db

class Blogpost(db.Model):

	__tablename__ = "accidents"
	#__table_args__ = {'extend_existing': True}

	serial = db.Column(db.Integer, primary_key=True)
	victim = db.Column(db.String)
	hospitals = db.Column(db.String)
	hospitals2 = db.Column(db.String)
	latitude = db.Column(db.Float)
	longitute = db.Column(db.Float)
	
	def __init__(self, victim, hospitals, hospitals2, latitude, longitute):
		self.victim = victim
		self.hospitals = hospitals
		self.distance = distance

	def __repr__(self):
		return '{}-{}-{}-{}-{}'.format(self.victim, self.hospitals, self.hospitals2, self.latitude, self.longitute)