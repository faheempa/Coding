from flask import render_template, url_for, flash, redirect, request
from signup_login import app, db, bcrypt
from signup_login.forms import RegistrationForm, LoginForm, UpdateAccountForm
from signup_login.models import User
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from PIL import Image
from signup_login.forms import RequestResetForm, ResetPasswordForm
from email.message import EmailMessage
import smtplib
import ssl


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            flash("Login Successful ", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            if user == None:
                flash("Login Unsuccessful. User does not exist", "danger")
            else:
                flash("Login Unsuccessful. Wrong password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


def send_reset_email(user):
    token = user.password.split("/")[0]
    sender = app.config["MAIL_USERNAME"]
    password = app.config["MAIL_PASSWORD"]
    reciver = user.email
    subject = "Password Reset Request"
    body = f"""To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
    """
    em = EmailMessage()
    em["From"] = sender
    em["To"] = reciver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, reciver, em.as_string())


@app.route("/reset_password", methods=["GET", "POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user == None:
            flash("Email does not exist", "danger")
            return redirect(url_for("reset_request"))
        send_reset_email(user)
        flash(
            "An email has been sent with a link to reset your password.",
            "info",
        )
        return redirect(url_for("login"))
    return render_template("reset_request.html", title="Reset Password", form=form)


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    user = User.query.filter(User.password.like(f"{token}%")).first()
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("reset_request"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("reset_password.html", title="Reset Password", form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/img/dp", picture_fn)

    output_size = (100, 100)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="img/dp/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )
