from locale import currency

from flask import render_template
from source import app, cryptoSearch, request


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        crypto = str(request.form.get('crypto'))
        currency = str(request.form.get('fiats'))
        cryptodict = cryptoSearch(crypto, currency)
        return render_template('searchresult.html', cryptodict = cryptodict)
    return render_template('home.html')
