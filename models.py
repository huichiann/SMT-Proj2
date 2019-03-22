from app import db
import datetime

user_challenge_table = db.Table(
	'user_challenge',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'), primary_key=True)
	)

class User(db.Model):
	__tablename__ = "user"
		
	# write your code here
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(80), unique=True, nullable=False)
	name = db.Column(db.String(80), nullable=False)
	contactnumber = db.Column(db.Integer, unique=True, nullable=False)
	#one-to-many relationship with daily_steps_record
	daily_steps_records = db.relationship("Daily_Steps_Record", back_populates="userrecord", cascade="all", lazy=True, uselist=True)
	#many-to-many relationship with challenge
	challenges = db.relationship("Challenge", secondary=user_challenge_table, lazy=True, back_populates="users")

	def __init__(self, email, name, contactnumber, challenges=None):
		# write your code here
		self.email = email
		self.name = name
		self.contactnumber = contactnumber
		challenges = [] if challenges is None else challenges
		self.challenges = challenges
	
	def serialize(self):
		result = {} 
		# write your code here 
		result['id'] = self.id
		result['email'] = self.email
		result['name'] = self.name
		result['contactNumber'] = self.contactnumber 
		result['challenges'] = [c.serialize() for c in self.challenges]
		return result 
		
class Daily_Steps_Record(db.Model):
	__tablename__ = "steps"
		
	# write your code here
	id = db.Column(db.Integer, primary_key=True)
	steps_taken = db.Column(db.Integer, nullable=False)
	date_added = db.Column(db.DateTime)
	#foreignkey from user
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
	#zero-to-one relationship with user
	userrecord = db.relationship("User", back_populates="daily_steps_records")

	def __init__(self, steps_taken, date_added, user_id):
		# write your code here
		self.steps_taken = steps_taken
		self.date_added = date_added
		self.user_id =user_id

	def serialize(self):
		result = {} 
		# write your code here 
		result["id"] = self.id
		result["user_id"] = self.user_id
		result["steps_taken"] = self.steps_taken
		result["date_added"] = self.date_added
		return result 

class Challenge(db.Model):
	__tablename__ = 'challenge'
		
	# write your code here
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	start = db.Column(db.DateTime)
	end = db.Column(db.DateTime)
	daily_steps_quota = db.Column(db.Integer, nullable=False)
	reward = db.Column(db.String(80), nullable=False)
	#many-to-many relationship with user
	users = db.relationship('User', secondary=user_challenge_table, lazy=True, back_populates='challenges')

	def __init__(self, title, daily_steps_quota, reward, start, end, participants = None):
		# write your code here
		self.title = title
		self.daily_steps_quota = daily_steps_quota
		self.reward = reward
		self.start = start
		self.end = end
		participants = [] if participants is None else participants
		self.participants = participants
	
	def serialize(self):
		result = {} 
		# write your code here
		result['id'] = self.id
		result['title'] = self.title
		result['daily_steps_quota'] = self.daily_steps_quota
		result['reward'] = self.reward
		result['start'] = self.start
		result['end'] = self.end 
		result['participants'] = [p.serialize() for p in self.participants]
		return result 