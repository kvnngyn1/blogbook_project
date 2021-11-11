from app.blueprints.auth.models import User
from .import bp as app
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user
from app import db


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        # if email and password don't match
        if user is None or not user.check_password(password):
            # show and error message
            flash('Youe typed in either an incorrect email or password', 'danger')
            # redirect to the login page
            return redirect(url_for('auth.login'))
        # otherwise
        # log the user in
        login_user(user)
        flash('You have logged in successfully!', 'info')
        return redirect(url_for('main.home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user is not None:
            flash('That user already exists. Please try another email address', 'warning')
            return redirect(url_for('auth.register'))
        if request.form.get('password') != request.form.get('confirm_password'):
            flash('Your password do not match.', 'danger')
            return redirect(url_for('auth.register'))

        # u = User(
        #     first_name=request.form.get('first_name'),
        #     last_name=request.form.get('last_name'),
        #     email=request.form.get('email'),
        #     password=request.form.get('password')
        # )
        # db.session.add(u)
        # db.session.commit()
    
        u = User()
        u.from_dict(request.form)
        u.save()
    # Everything is now coming from models.from_dict()


        flash('User has registered successfully', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('main.home'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # current_user.update_profile(request.form)
        u = User.query.get(current_user.id)
        u.first_name = request.form.get('first_name')
        u.last_name = request.form.get('last_name')
        u.email = request.form.get('email')
        u.bio = request.form.get('bio')
        db.session.commit()

        flash('NOICE! UPDATE COMPLETE!', 'info')
        return redirect(url_for('auth.profile'))
    return render_template('profile.html')
