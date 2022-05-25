from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user
from forms.login_form import LoginForm
from forms.registration_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from forms.password_checker import password_checker
from models.model import Users
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('views.users'))

    login = LoginForm()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Wrong username or password', category='error')
            return redirect(url_for('auth.login'))
        else:
            login_user(user, remember=True)
            return redirect(url_for('views.index'))

    return render_template('login.html', login=login, user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():

    register = RegistrationForm()

    if current_user.is_authenticated:
        return redirect(url_for('views.users'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_repeat = request.form.get('password_repeat')
        password_check = password_checker(password)

        user = Users.query.filter_by(username=username).first()

        if user:
            flash('Username already exists', category='error')
        elif password_check['length_error'] == True:
            flash('Password need to be at least 8 characthers long', category='error')
        elif password_check['password_ok'] == False:
            flash('Password needs to contain upper and lower case letters, at least one symbol, and at least one digit', category='error')
        elif password != password_repeat:
            flash("Passwords must match")
        else:    
            new_user = Users(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account successfully created! You can login now', category='success')
            return redirect(url_for('auth.login'))

    return render_template('register.html', register=register, user=current_user)
