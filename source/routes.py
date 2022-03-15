from flask import render_template, redirect, request, url_for, flash
from source import app, cryptoSearch, request, database, bcrypt
from source.forms import FormLogin, FormCreateAccount
from source.models import User
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        crypto = str(request.form.get('crypto')).lower()
        currency = str(request.form.get('fiats'))
        cryptodict = cryptoSearch(crypto, currency)
        return render_template('public/searchresult.html', cryptodict = cryptodict)
    return render_template('public/home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember= form_login.remember_me.data)
            flash(f'Login Sucessful on e-mail {form_login.email.data}', 'alert-sucess')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('homelogin'))
        else:
            flash('Login Failed. Invalid Email or Password, please try again.', 'alert-danger')
    return render_template('public/login.html', form_login = form_login)

@app.route('/register', methods=['GET','POST'])
def register():
    form_create_account = FormCreateAccount()
    if form_create_account.validate_on_submit() and 'submit_create_account' in request.form:
        pw_crypto = bcrypt.generate_password_hash(form_create_account.password.data)
        user = User(username = form_create_account.username.data, email = form_create_account.email.data, password = pw_crypto)
        database.session.add(user)
        database.session.commit()
        flash(f'Account created successfully for the email: {form_create_account.email.data}.', 'alert-sucess')
        login_user(user)
        return redirect(url_for('homelogin'))
    return render_template('public/register.html', form_create_account = form_create_account)

@app.route('/homelogin')
@login_required
def homelogin():
    return render_template('admin/loginhome.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('admin/profile.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
