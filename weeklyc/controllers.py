from weeklyc.database import db_session
from weeklyc.models import *
from weeklyc.forms import *


"""Challenge Controller
"""

#This will get the challenge data that will be publicy displayed,
# the flag will not be provided
def get_challenges():
	data = []
	challenges = db_session.query(Challenge.id, Challenge.name,
									Challenge.link)
	for id, name, link in challenges:
		data.append({
			'id': id,
			'name': name,
			'link': link
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
			'solves': len(challenge.submissions)
		})
	return data

def get_challenge_info():
	data = []
	pass
