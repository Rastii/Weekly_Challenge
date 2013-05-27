$(document).ready ->
	$.ajax '/api/challenges',
		type: 'GET'
		dataType: 'json'
		error: (jqXHR, textStatus, errorThrown) ->
			console.error(jqXHR, textStatus, errorThrown)
		success: (data, textStatus, jqXHR) ->
			console.log(data, textStatus, jqXHR)
			for chal in data
				btn = $('<button class="btn" type="button">Submit</button>').click () ->
					console.log('this would submit the key', this);
				challengeBlock = $('
					<div class="span3">
						<div class="well text-center">
					      <h3>Challenge #' + chal.id + '<br><small>' + chal.name + '</small></h3>
					      <hr>
					      <p>Solves: ' + chal.solves + '</p>
					      <a href="' + chal.link + '">Download Challenge</a>
					      <div class="input-append">
					        <input class="input-small" id="appendedInputButton" type="text" placeholder="Flag">					        
					      </div>
					    </div>
					</div>')
				challengeBlock.find('.input-append').append(btn)
				challengeBlock.appendTo('#challenges')