from flask import render_template, redirect, request, url_for, flash
from source import app, cryptoSearch, request


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        crypto = str(request.form.get('crypto')).lower()
        currency = str(request.form.get('fiats'))
        cryptodict = cryptoSearch(crypto, currency)
        return render_template('searchresult.html', cryptodict = cryptodict)
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')