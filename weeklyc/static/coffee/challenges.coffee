$(document).ready ->
	$.ajax '/api/challenges',
		type: 'GET'
		dataType: 'json'
		error: (jqXHR, textStatus, errorThrown) ->
			console.error(jqXHR, textStatus, errorThrown)
		success: (data, textStatus, jqXHR) ->
			console.log(data, textStatus, jqXHR)
			for chal in data.reverse()
				btn = $('<button class="btn" type="button">Submit</button>').click () =>
					alert('this would submit the key');
				challengeBlock = $('
					<div class="span3">
						<div class="well text-center">
					      <h3>Challenge #' + chal.id + '</h3>
					      <h2>' + chal.name + '</h2>
					      <hr>
					      <p>Solves: ' + chal.solves + '</p>
					      <a href="' + chal.link + '">Download Challenge</a>
					      <div class="input-append">
					        <input class="input-small" id="appendedInputButton" type="text" placeholder="Flag">
					        
					      </div>
					    </div>
					</div>')



"""
<div class="span3">
    <div class="well text-center">
      <h3>Challenge #1</h3>
      <hr>
      <p>Solves: 0</p>
      <a href="#">Download Challenge</a>
      <div class="input-append">
        <input class="input-small" id="appendedInputButton" type="text" placeholder="Flag">
        
      </div>
    </div>
  </div>
"""