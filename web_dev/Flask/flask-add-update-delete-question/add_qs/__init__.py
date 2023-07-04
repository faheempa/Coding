# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialization
app = Flask(__name__)
database = "skillsharp"
username = "7nyxz1bj8gc440qn0jp0"
host = "aws.connect.psdb.cloud"
password = "pscale_pw_SUUgNzhHum1MM322QLMJrPWCt6QJypDYFwxNjgqd9uM"
connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# making routes accessible
from add_qs import routes

# creating dabaase and tables if not already
with app.app_context():
    db.create_all()
    db.session.commit()
 