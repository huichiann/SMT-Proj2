from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://smtproj2user:smtproj2@localhost:5432/smtproj2db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Daily_Steps_Record, Challenge

@app.route('/', methods=["GET"])
def print_hello():
	return 'Welcome to National Steps Challenge'

# @app.route('/user', methods=["POST"])
# def create_user():
# 	# write your code here
# 	ic = request.json['ic']
# 	name = request.json['name']
# 	try:
# 		new_user = User(ic=ic, name=name)
# 		db.session.add(new_user)
# 		db.session.commit()
# 		return jsonify('{} was created'.format(new_user))

# @app.route('/dailystep', methods=["POST"])
# def create_daily_step():
# 	# write your code here
# 	steps = request.json['steps']
# 	date = request.json['date']

# @app.route('/challenge', methods=["POST"])
# def create_challenge():
# 	# write your code here
	
# @app.route('/users/', methods=['GET'])
# def get_users():
# 	# write your code here


# @app.route('/dailysteps/', methods=['GET'])
# def get_daily_steps():
# 	# write your code here

# @app.route('/challenges/', methods=['GET'])
# def get_challenges():
# 	# write your code here
	
if __name__ == '__main__':
	app.run(debug=True)