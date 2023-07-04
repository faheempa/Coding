# how to run?

- open terminal
- run this command to install neccesory modules : pip3 install -r requirements.txt
- then "python3 run.py" to run the app

# order for documentation

- .env - just a file to store cretentials, no need to include it in the doc
- config.py
- __init__.py
- routes.py : @app.route("/home")
- templates/layout.html
- templates/home.html
- models.py
- forms.py : RegistrationForm
- routes.py : @app.route("/register", methods=["GET", "POST"])
- templates/register.html
- forms.py : LoginForm
- routes.py : @app.route("/login", methods=["GET", "POST"])
- templates/login.html
- @app.route("/logout")
- forms.py : RequestResetForm
- routes.py : @app.route("/reset_password", methods=["GET", "POST"])
- routes.py : def send_reset_email(user):
- templates/reset_request.html
- forms.py : ResetPasswordForm
- routes.py : @app.route("/reset_password/<token>", methods=["GET", "POST"])
- templates/reset_password.html
- forms.py : UpdateAccountForm
- routes.py : @app.route("/account", methods=["GET", "POST"])
- templates/account.html
- routes.py : def save_picture(form_picture):
- static/img/dp - profile pics are saved here
- instance folder : folder made by the compiler, in which local database is stored