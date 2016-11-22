#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from wifi import Cell, Scheme
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class WifiForm(FlaskForm):
    wifi = SelectField('WiFI network', choices=[])
    submit = SubmitField('submit')

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'blaba'

@app.route('/', methods=["GET", "POST"])
def index():
    form = WifiForm()
    cells = Cell.all('wlan0')
    form.wifi.choices = [(idx, c.ssid + '@' + str(c.frequency)) for idx, c in enumerate(cells)]
    if form.validate_on_submit():
        return form.wifi.data
    return render_template('index.html', cells=cells, form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
