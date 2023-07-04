

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# SQLAlchemy Database Configuration With MySQL
database = "skillsharp"
username = "7nyxz1bj8gc440qn0jp0"
host = "aws.connect.psdb.cloud"
password = "pscale_pw_SUUgNzhHum1MM322QLMJrPWCt6QJypDYFwxNjgqd9uM"

connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}:3306/{database}"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)

# Creating model table for our CRUD database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


if __name__ == "__main__":

    # using app context because we are not running the app
    with app.app_context():
        
        # create tables
        db.create_all()
        
        #inserting some data
        # id is provided automatically
        db.session.add(User(username='faheem', email="faheem@gmail.com", password="wecewcc"))
        db.session.add(User(username='pranav', email="pranav@gmail.com", password="dwdcwccec"))
        db.session.add(User(username='alan', email="alan@gmail.com", password="sfsdsd", image_file='alan.jpg'))
        db.session.add(User(username='vinay', email="vinay@gmail.com", password="dwdcwccwefwefec", image_file='vinay.jpg'))
        db.session.commit()

        #fetching data
        print("\nfetching data: ")
        all_users = User.query.all()
        for user in all_users:
            print(user)

        print("\nusers sorted by username in asc: ")
        all_users = User.query.order_by(User.username.asc()).all()
        for user in all_users:
            print(user)

        print("\npranav's data: ")
        user = User.query.filter_by(username="pranav").first()
        print(user)

        print("\nusers data who name starts with 'a': ")
        users = User.query.filter(User.username.like('a%')).all()
        for user in users:
            print(user)

        # # updating data
        user = User.query.filter_by(username='faheem').first()
        user.username = "faheempa"
        user.email = "faheempa788@gmail.com"
        user.image_file = "faheempa.jpg"
        db.session.commit()

        # # deleting data
        user = User.query.filter_by(username='vinay').first()
        db.session.delete(user)
        db.session.commit()

        # drop table
        db.session.execute(text("DROP TABLE user"))
        db.session.commit()
        

