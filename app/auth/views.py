from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegForm,LoginForm
from ..models import Users
from .. import db
from ..email import mail_message

@auth.route('/login', methods = ['GET','POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = Users.query.filter_by(username = loginform.username.data).first()
        if user != None and user.verify_password(loginform.password.data):
            login_user(user,loginform.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    return render_template('auth/login.html', loginform = loginform)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = Users(email = form.email.data, username = form.username.data, password = form.password.data)
        user.save_u()
        mail_message("Welcome to Pitch-World","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',form = form)