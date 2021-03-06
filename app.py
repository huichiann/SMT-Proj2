from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://smtproj2user:smtproj2@localhost:5432/smtproj2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Daily_Steps_Record, Challenge

@app.route('/', methods=["GET"])
def print_hello():
	return 'Welcome to National Steps Challenge'

@app.route('/user', methods=["POST"])
def create_user():
	email = request.json['email']
	name = request.json['name']
	contactnumber = request.json['contactnumber']
	
	try:
		new_user = User(email=email, name=name, contactnumber=contactnumber)
		db.session.add(new_user)
		db.session.commit()
		return jsonify('<200> {} was created'.format(new_user))
	except Exception as e:
		return (str(e))

@app.route('/dailystep', methods=["POST"])
def create_daily_step():
	# write your code here
	steps_taken = request.json["steps_taken"]
	date_added = request.json["date_added"]
	email = request.json["email"]
	user_id = User.query.filter_by(email=email).first().id
	date_added = datetime.strptime(date_added, "%d/%m/%Y")

	try:
		new_dailystep = Daily_Steps_Record(steps_taken=steps_taken, date_added=date_added, user_id=user_id)
		db.session.add(new_dailystep)
		db.session.commit()
		return jsonify('<200> {} was created'.format(new_dailystep))
	except Exception as e:
		return (str(e))

@app.route('/challenge', methods=["POST"])
def create_challenge():
	# write your code here
	title = request.json["title"]
	daily_steps_quota = request.json["daily_steps_quota"]
	reward = request.json["reward"]
	start = request.json["start"]
	end = request.json["end"]

	start = datetime.strptime(start, "%d/%m/%Y")
	end = datetime.strptime(end, "%d/%m/%Y")

	print(type(start))

	try:
		new_challenge = Challenge(title=title, daily_steps_quota=daily_steps_quota, reward=reward, start=start, end=end)
		db.session.add(new_challenge)
		db.session.commit()

		return jsonify("<200> {} was created".format(new_challenge))
	except Exception as e:
		return (str(e))

@app.route('/users/', methods=['GET'])
def get_users():
    user = User.query.all()
    return jsonify([s.serialize() for s in user])

@app.route('/dailysteps/', methods=['GET'])
def get_daily_steps():
	# write your code here
	dailysteps = Daily_Steps_Record.query.all()
	return jsonify([s.serialize() for s in dailysteps])


# @app.route('/dailysteps/', methods=['GET'])
# def get_daily_steps():
# 	# write your code here
# 	return

# @app.route('/joinchallenge/', methods=['GET'])
# def join_challenge():
#     title = request.json["title"]
# 	email = request.json["email"]
# 	# write your code here
# 	try:
# 		student_id = Student.query.filter_by(email=email).first().id
# 		print(student_id)
# 		title_id = Challenge.query.filter_by(title=title).first().id
# 		print(title_id)
# 		new_challenger = 
	
if __name__ == '__main__':
	app.run(debug=True)