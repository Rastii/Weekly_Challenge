$->

	window.userSolves = {}
	window.challengeCount = 0
	window.completeCounter = 0;

	# Get a list of all challenges
	$.ajax '/api/challenges',
		type: 'GET'
		dataType: 'json'
		error: (jqXHR, textStatus, errorThrown) ->
			console.error(jqXHR, textStatus, errorThrown)
		success: (data, textStatus, jqXHR) ->
			window.challengeCount = data.length
			for challenge in data
				# Add a point for each user who solved the challenge
				$.ajax '/api/challenges/'+challenge.id+'/users',
					type: 'GET'
					dataType: 'json'
					error: (jqXHR, textStatus, errorThrown) ->
						console.error(jqXHR, textStatus, errorThrown)
					success: (data) ->
						for user in data
							if window.userSolves[user]?						
								window.userSolves[user] += 1
							else
								window.userSolves[user] = 1
					complete: () ->
						#IDK If there's a better way to do this, there's sooo much async going on!
						if window.completeCounter < window.challengeCount - 1
							window.completeCounter++
						else
							#DONE!
							#Sort by score
							names = (n for n of window.userSolves)
							sortedNames = names.sort (a, b) -> window.userSolves[b] - window.userSolves[a]

							#Print
							for name in sortedNames
								$('<tr><td>' + name + '</td><td>' + window.userSolves[name] + '</td></tr>').appendTo('#scoreboard')

			