import sys
from weeklyc import app

app.jinja_env.line_statement_prefix = '%'
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

if len(sys.argv) > 1:
    if sys.argv[1] == 'run':
        #use this if you wanto view your page outside of localhost
        app.run(debug=True, host='0.0.0.0', port=5000)
        #app.run(debug=True, host='localhost', port=5000)
        sys.exit()

    elif sys.argv[1] == 'setup':
        from weeklyc.database import *
        kill_db()
        init_db()
        setup_db()
        sys.exit()

    elif sys.argv[1] == 'shell':
        from flask import *
        from weeklyc import *
        from weeklyc.models import *
        from IPython import embed
        embed()
        sys.exit()
print "Usage: %s <run> | <setup> | <shell>" % sys.argv[0]
sys.exit()
