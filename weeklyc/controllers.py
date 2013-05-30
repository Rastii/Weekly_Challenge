from weeklyc.database import db_session
from weeklyc.models import *
from weeklyc.forms import *


"""Challenge Controller
"""

#This will get the challenge data that will be publicy displayed,
# the flag will not be provided
def get_challenges():
	data = []
	challenges = db_session.query(Challenge)
	for challenge in challenges:
		data.append({
			'id': challenge.id,
			'name': challenge.name,
			'link': challenge.link,
			'solves': len(challenge.submissions),
		})
	if len(data) > 0:
		return data
	else:
		return None

#Returns list of users of solved a challenge with id of parameter
def get_challenge_users(challenge_id):
	challenge = db_session.query(Challenge)\
				.filter_by(id=challenge_id).first()
	print challenge
	if(challenge):
		return [user.login for user in challenge.users]
	else:
		return None

def get_users():
	data = []
	users = db_session.query(User)
	if users:
		for user in users:
			data.append({
				'name': user.login,
				#For future use
				#'submissions': [x.name for x in user.submissions]
				'submissions': len(user.submissions)
			})
		return data
	else:
		return data