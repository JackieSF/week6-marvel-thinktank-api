from flask import Blueprint, render_template, request, url_for, flash, redirect
from marvel.forms import UserLoginForm
from marvel.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)
            
            new_user = User(email, password)

            db.session.add(new_user)
            db.session.commit()
            
            flash(f'You made a new account: {email}', 'user-created')
        
            return redirect(url_for('site.home'))
    
    except:
        raise Exception('oop! you almost had it!')
    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash("Congrats. You're in.", 'auth-success')
                return redirect(url_for('site.home')
            else:
                flash("you did something wrong somewhere", 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('oop! you almost had it!')
    return render_template('signin.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('oh great. you left.', 'auth-success')
    return redirect(url_for('site.home'))