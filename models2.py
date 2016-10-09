from app import db

class Blogposts(db.Model):

	__tablename__ = "accidents"

	serial = db.Column(db.Integer, primary_key=True)
	victim = db.Column(db.String)
	hospitals = db.Column(db.String)
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	
	def __init__(self, victim, hospitals, distance):
		self.victim = victim
		self.hospitals = hospitals
		self.distance = distance
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return '{}-{}-{}-{}-{}'.format(self.victim, self.hospitals, self.distance, self.latitude, self.longitude)