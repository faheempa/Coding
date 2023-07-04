# how to run?

- open terminal
- run this command to install neccesory modules : pip3 install -r requirements.txt
- then "python3 run.py" to run the app

# order for documentation

- __init__.py
- models.py
- templates/layout.html
- routes.py : @app.route("/home")
- templates/home.html
- static/css/style.css
- forms.py
- routes.py : @app.route("/add_question", methods=['GET', 'POST'])
- templates/form.html
- routes.py : @app.route("/update_question/<int:question_id>", methods=['GET', 'POST'])
- routes.py : @app.route("/remove/<int:question_id>")
