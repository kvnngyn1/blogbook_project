from flask.helpers import url_for
from app import db
from flask_login import login_user, logout_user, current_user
from flask import request, flash, redirect, url_for, render_template
from app.blueprints.main.models import Post
from .import bp as app

@app.route('/', methods=['GET', 'POST'])
def home():
    print(current_user) if current_user else None
    # adds ability to add a post into sql database
    if request.method == 'POST':
        p = Post(
        body=request.form.get('body'),
        user_id=request.form.get('user_id')
        )
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully', 'success')
        return redirect(url_for('main.home'))
    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }

    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


