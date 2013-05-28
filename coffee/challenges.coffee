$(document).ready ->
	$.ajax '/api/challenges',
		type: 'GET'
		dataType: 'json'
		error: (jqXHR, textStatus, errorThrown) ->
			console.error(jqXHR, textStatus, errorThrown)
		success: (data, textStatus, jqXHR) ->
			for chal in data
				btn = $('<button class="btn" type="button">Submit</button>')
					.click () ->
						# Remove color (may be too fast but oh well)
						$(this).removeClass('btn-danger').removeClass('btn-success')

						# Submit a key
						$.ajax '/test/challenges/' + chal.id,
							type: 'POST'
							data: {foo: 'bar'}
							success: (data) =>
								if(data == '1')
									#Success
									$(this).addClass('btn-success').parent().parent().addClass('solved')
								else
									#Invalid key
									$(this).addClass('btn-danger')


				input = $('<input class="input-small" id="appendedInputButton" type="text" placeholder="Flag">')					
					.keydown (objectEvent) ->
						if objectEvent.keyCode == 13 #enter key
							# Click the submit button
							$(this).parent().find('button').click();


				challengeBlock = $('
					<div class="span3">
						<div class="well text-center" id="well-' + chal.id + '">
					      <h3>Challenge #' + chal.id + '<br><small>' + chal.name + '</small></h3>
					      <hr>
					      <p>Solves: ' + chal.solves + '</p>
					      <a href="' + chal.link + '">Download Challenge</a>
					      <div class="input-append">					        				        
					      </div>
					    </div>
					</div>')
				challengeBlock.find('.input-append').append(input)
				challengeBlock.find('.input-append').append(btn)
				challengeBlock.appendTo('#challenges')

				#Solved or not
				$.ajax '/api/challenges/' + chal.id + '/users',
					type: 'GET'
					dataType: 'json'
					success: (data) ->
						if window.user in data
							# User has solved this challenge
							$('#well-' + this.url.split('/')[3]).addClass('solved')
