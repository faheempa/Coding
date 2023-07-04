from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# This is the form for adding and updating questions
class QuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired(), Length(max=2000)])
    answer = StringField('Answer', validators=[DataRequired(), Length(max=250)])
    option_a = StringField('Option A', validators=[DataRequired(), Length(max=250)])
    option_b = StringField('Option B', validators=[DataRequired(), Length(max=250)])
    option_c = StringField('Option C', validators=[Length(max=250)])
    option_d = StringField('Option D', validators=[Length(max=250)])
    section = StringField('Section', validators=[DataRequired(), Length(max=250)])
    topic = StringField('Topic', validators=[DataRequired(), Length(max=250)])

# inherits from QuestionForm
class AddQuestionForm(QuestionForm):
    submit = SubmitField('Add Question')

# inherits from QuestionForm
class UpdateQuestionForm(QuestionForm):
    submit = SubmitField('Update Question')


    

