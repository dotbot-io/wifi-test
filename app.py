#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from wifi import Cell, Scheme
from flask_wtf import Form

class WifiForm(Form):
    language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    form = WifiForm()
    cells = Cell.all('wlan0')
    return render_template('index.html', cells=cells, form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
