from flask import Blueprint, render_template, request, flash, redirect, url_for
#flash: allows us to flash a message

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

from .models import Note


auth = Blueprint('auth', __name__)

@auth.route('/contacts')
def contacts():
    return render_template("pages/Contacts.html", user=current_user)


@auth.route('/information')
def information():
    return render_template("pages/information.html", user=current_user)
@auth.route('/about')
def about():
    return render_template("pages/about.html", user=current_user)

@auth.route('/resources')
@login_required
def resources():
    return render_template("User_pages/resources.html", user=current_user)


@auth.route('/profile')
@login_required
def profile():
    return render_template("User_pages/profile.html", user=current_user)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #filters information in database
        user = User.query.filter_by(email=email).first()
        #if we found a user
        if user:
            #if the inputed password is the same
            if check_password_hash(user.password, password):
                # flash("Logged in successfully!", category='success')
                login_user(user)
                return redirect(url_for('views.announcements'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    #gets information from the form
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        password = request.form.get('password')
        confirm = request.form.get('Confirm')

        #makes sure user does not already ixist
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')


        elif len(email) < 4:
            #shows a message
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name has to be greater than 1 character', category='error')
        elif password != confirm:
            flash('password do not match', category='error')
        elif len(password) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            new_user = User(email = email, password = generate_password_hash(password, method = 'sha256'), name = name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)#remembers that the user is logged in
            flash('Account created!', category='success')
            #replace views.py for a login page in future
            return redirect(url_for('views.announcements'))

    return render_template("signup.html", user=current_user)