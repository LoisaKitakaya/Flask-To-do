import re
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import bp
from app.models.db_schema import User, Todo
from app.extensions import db

@bp.route('/')
@login_required
def index():

    '''App's homepage'''

    return render_template('index.html', current_user=current_user)

@bp.route('/about/')
def about():

    '''Page giving more info about the app'''

    return render_template('about.html')

@bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    '''Create a new user account'''

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password_one = request.form.get('password_one')
        password_two = request.form.get('password_two')

        try:

            username_already_in_use = User.query.filter_by(username=username).first()

        except:

            pass

        if username_already_in_use:

            flash("This username is already in use. Please choose a unique username.", "error")
            return redirect(url_for('todo.signup'))

        if not re.search("(^\w+)@([a-z]+)[.]([a-z]+\S)$", email):

            flash('Your email must be in the format of "abc@def.ghi", for example: example@email.com', "error")
            return redirect(url_for('todo.signup'))

        try:

            email_already_in_use = User.query.filter_by(email=email).first()

        except:

            pass

        if email_already_in_use:

            flash("This email is already in use. Please choose a unique email.", "error")
            return redirect(url_for('todo.signup'))

        if len(password_one) < 8 or len(password_two) < 8:

            flash("The password(s) provided is too short. Minimum characters expected for a strong password is 8.", "error")
            return redirect(url_for('todo.signup'))

        if password_one != password_two:

            flash("The passwords provided do not match.", "error")
            return redirect(url_for('todo.signup'))

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password_one, method='sha256')
        )

        try:

            db.session.add(new_user)

        except:

            raise

        else:
            
            db.session.commit()
            flash(f'User {username} created successfully!', 'message')

            return redirect(url_for('todo.login'))

    return render_template('signup.html')

@bp.route('/login/', methods=['GET', 'POST'])
def login():

    '''Login an already registered user'''

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        try:

            this_user = User.query.filter_by(username=username).first()

        except:

            flash('Please check you username and try again.', 'error')
            return redirect(url_for('todo.login'))

        else:

            if this_user == None:

                flash('Please check you username and try again.', 'error')
                return redirect(url_for('todo.login'))
            
            if not check_password_hash(this_user.password, password):

                flash('Please check you password and try again.', 'error')
                return redirect(url_for('todo.login'))

            login_user(this_user, remember=True)

            flash("Logged in successfully.", "message")
            return redirect(url_for('todo.index'))

    return render_template('login.html')

@bp.route('/logout/')
def logout():

    '''Logout user'''

    logout_user()

    flash("Logged out successfully.", "message")
    return redirect(url_for('todo.login'))

@bp.route('/add_task/', methods=['POST'])
def add_task():

    '''Add new task to db'''

    task = request.form.get('task')
    label = request.form.get('label')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    user_id = current_user.id

    new_task = Todo(
        task=task,
        label=label,
        description=description,
        due_date=str(due_date),
        user_id=user_id
    )

    try:

        db.session.add(new_task)

    except:

        raise

    else:

        db.session.commit()

        flash(f'Task {task} has been added.', 'message')
        return redirect(url_for('todo.index'))