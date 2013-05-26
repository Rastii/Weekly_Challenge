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
	return data

#This will get challenge submissions info, returns id, name, and
# amount of submissions associated with each challenge
def get_challenge_submission_info():
	data = []
	challenges = db_session.query(Challenge)
	for challenge in challenges:
		data.append({
			'name': challenge.name,
			'solves': len(challenge.submissions),
			'users': [user.login for user in challenge.users]
		})
	return data

#Returns list of users of solved a challenge with id of parameter
def get_challenge_users(challenge_id):
	challenge = db_session.query(Challenge)\
				.filter_by(id=challenge_id).first()
	print challenge
	if(challenge):
		return [user.login for user in challenge.users]
	else:
		return None
