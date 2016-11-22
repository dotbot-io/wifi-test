#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from wifi import Cell, Scheme
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class WifiForm(FlaskForm):
    language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'blaba'

@app.route('/')
def index():
    cells = Cell.all('wlan0')
    form = WifiForm()
    form.language.choices = [(idx, c.ssid + '@' str(c.frequency)) for idx, c in enumarate(cells)]
    return render_template('index.html', cells=cells, form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
