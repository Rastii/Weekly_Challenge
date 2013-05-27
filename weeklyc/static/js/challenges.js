// Generated by CoffeeScript 1.6.2
(function() {
  $(document).ready(function() {
    return $.ajax('/api/challenges', {
      type: 'GET',
      dataType: 'json',
      error: function(jqXHR, textStatus, errorThrown) {
        return console.error(jqXHR, textStatus, errorThrown);
      },
      success: function(data, textStatus, jqXHR) {
        var btn, chal, challengeBlock, _i, _len, _results;

        console.log(data, textStatus, jqXHR);
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          chal = data[_i];
          btn = $('<button class="btn" type="button">Submit</button>').click(function() {
            return console.log('this would submit the key', this);
          });
          challengeBlock = $('\
					<div class="span3">\
						<div class="well text-center">\
					      <h3>Challenge #' + chal.id + '<br><small>' + chal.name + '</small></h3>\
					      <hr>\
					      <p>Solves: ' + chal.solves + '</p>\
					      <a href="' + chal.link + '">Download Challenge</a>\
					      <div class="input-append">\
					        <input class="input-small" id="appendedInputButton" type="text" placeholder="Flag">					        \
					      </div>\
					    </div>\
					</div>');
          challengeBlock.find('.input-append').append(btn);
          _results.push(challengeBlock.appendTo('#challenges'));
        }
        return _results;
      }
    });
  });

}).call(this);