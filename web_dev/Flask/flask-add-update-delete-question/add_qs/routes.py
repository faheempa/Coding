from flask import render_template, url_for, redirect, request
from add_qs.forms import AddQuestionForm, UpdateQuestionForm
from add_qs.models import Questions
from add_qs import db, app

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    questions = Questions.query.order_by(Questions.QID.desc()).paginate(page=page, per_page=15)
    return render_template('home.html', items=questions, title='Home')


@app.route("/add_question", methods=['GET', 'POST'])
def add_question():
    form = AddQuestionForm()
    if request.method == 'POST':
        question = Questions(QID = Questions.getNextQID(), Question=form.question.data, 
                             Answer=form.answer.data, OptionA=form.option_a.data, 
                             OptionB=form.option_b.data, OptionC=form.option_c.data, 
                             OptionD=form.option_d.data, Section=form.section.data, Topic=form.topic.data)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("form.html", title='Form', form=form)

@app.route("/update_question/<int:question_id>", methods=['GET', 'POST'])
def update_question(question_id):
    question = Questions.query.get_or_404(question_id)
    form = UpdateQuestionForm()
    if request.method == 'POST':
        question.Question = form.question.data
        question.Answer = form.answer.data
        question.OptionA = form.option_a.data
        question.OptionB = form.option_b.data
        question.OptionC = form.option_c.data
        question.OptionD = form.option_d.data
        question.Section = form.section.data
        question.Topic = form.topic.data
        db.session.commit()
        return redirect(url_for('home'))
    else:
        form.question.data = question.Question
        form.answer.data = question.Answer
        form.option_a.data = question.OptionA
        form.option_b.data = question.OptionB
        form.option_c.data = question.OptionC
        form.option_d.data = question.OptionD
        form.section.data = question.Section
        form.topic.data = question.Topic
    return render_template("form.html", title='Form', form=form)

@app.route("/remove/<int:question_id>")
def remove(question_id):
    question = Questions.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('home'))