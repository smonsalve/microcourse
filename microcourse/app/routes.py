from flask import render_template,flash, redirect, url_for, request
from werkzeug.urls import url_parse
from werkzeug.utils import redirect
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

@app.route("/") 
@app.route("/index")
@login_required
def index():
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",title="Inicio")    

# LOGIN #######################################################################
@app.route("/login", methods=['GET','POST'])
def login():

    if current_user.is_authenticated: 
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # flash(f"Login requested for user {form.username.data}. remember_me={form.remember_me.data}")
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data): 
            flash(" usuario o password incorrecto")
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)

        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)

# LOGOUT ######################################################################
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email= form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, you are now registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)