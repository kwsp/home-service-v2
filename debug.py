#!./flask/bin/python

from home_service import create_app

app = create_app()
app.run(port="6969", debug=True)
