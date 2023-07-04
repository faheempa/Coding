from project.models import User
from project.signup_and_login.forms import RegistrationForm, LoginForm, UpdateAccountForm
from project import bcrypt

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"HOME" in response.data

def test_registration_page(client, app):
    with app.app_context():
        # test get request
        response = client.get("/register")
        assert response.status_code == 200

        # testing form
        form = RegistrationForm()
        assert form.validate() is False

        # test post request with invalid data
        form.username.data = 'testuser'
        form.email.data = 'testuser@example.com'
        form.password.data = 'pass'
        form.confirm_password.data = 'pass'
        assert form.validate() is False
        response = client.post("/register", data=form.data, follow_redirects=True)
        assert b"Registration Unsuccessful. Please check your details and try again" in response.data

        # test post request with valid data
        form.username.data = 'testuser'
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        assert form.validate() is True
        response = client.post("/register", data=form.data, follow_redirects=True)
        assert b'Your account has been created! You are now able to log in' in response.data

        # test if user is created
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'testuser@example.com'
        assert user.username == 'testuser'
        assert User.query.count() == 1

        # test if we can use same username to register
        form.username.data = 'testuser'
        form.email.data = 'test@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        assert form.validate() is False

        # test if we can use same email to register
        form.username.data = 'testuser2'
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        assert form.validate() is False

        # test if we can add new user
        form.username.data = 'testuser2'
        form.email.data = 'testuser2@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        assert form.validate() is True
        response = client.post("/register", data=form.data, follow_redirects=True)
        assert b'Your account has been created! You are now able to log in' in response.data
        assert User.query.count() == 2

        # test if password matches
        user = User.query.filter_by(username=form.username.data).first()
        assert bcrypt.check_password_hash(user.password, form.password.data) is True

def test_login_page(client, app):
    with app.app_context():
        # test get request
        response = client.get("/login")
        assert response.status_code == 200

        # add a user
        form = RegistrationForm()
        form.username.data = 'testuser'
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        response = client.post("/register", data=form.data, follow_redirects=True)

        # login with invalid user
        form = LoginForm()
        form.email.data = 'test@example.com'
        form.password.data = 'password'
        assert form.validate() is True
        response = client.post("/login", data=form.data, follow_redirects=True)
        assert b'Login Unsuccessful. User does not exist' in response.data

        # login with invalid password
        form = LoginForm()
        form.email.data = 'testuser@example.com'
        form.password.data = 'wrongpassword'
        assert form.validate() is True
        response = client.post("/login", data=form.data, follow_redirects=True)
        assert b'Login Unsuccessful. Wrong password' in response.data

        # login with valid data
        form = LoginForm()
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        assert form.validate() is True
        response = client.post("/login", data=form.data, follow_redirects=True)
        assert b'Login Successful' in response.data

def test_account_page(client, app):
    with app.app_context():

        # test get request without login
        response = client.get("/account", follow_redirects=True)
        assert b"Please log in to access this page" in response.data

        # add a user
        form = RegistrationForm()
        form.username.data = 'testuser'
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        form.confirm_password.data = 'password'
        response = client.post("/register", data=form.data, follow_redirects=True)

        # login with valid data
        form = LoginForm()
        form.email.data = 'testuser@example.com'
        form.password.data = 'password'
        assert form.validate() is True
        response = client.post("/login", data=form.data, follow_redirects=True)
        assert b'Login Successful' in response.data

        # test get request with login
        response = client.get("/account")
        assert b"<title>Account</title>" in response.data

        # update account details
        form = UpdateAccountForm()
        form.username.data = 'testuserUpdated'
        form.email.data = "updated@gmail.com"
        form.picture.data = "default.jpg"
        response = client.post("/account", data=form.data, follow_redirects=True)
        assert b"Your account has been updated!" in response.data

        # test if user is updated
        user = User.query.filter_by(username='testuserUpdated').first()
        assert user is not None
        assert user.email == 'updated@gmail.com'
        assert user.username == 'testuserUpdated'

        

    
