from add_qs import db
from sqlalchemy import text

# Questions table
class Questions(db.Model):
    QID = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(2000), nullable=False)
    Answer = db.Column(db.String(250), nullable=False)
    OptionA = db.Column(db.String(250), nullable=False)
    OptionB = db.Column(db.String(250), nullable=False)
    OptionC = db.Column(db.String(250))
    OptionD = db.Column(db.String(250))
    Section = db.Column(db.String(250), nullable=False)
    Topic = db.Column(db.String(250), nullable=False)

    # string representation for printing purposes
    def __repr__(self):
        return f"""Q: {self.Question}', '{self.Answer}', '{self.Section}')"""
    
    # to get the next QID
    @staticmethod
    def getNextQID():
        val = db.session.execute(text(f"select max(QID) from questions")).all()[0][0]
        return val + 1 if val else 1

