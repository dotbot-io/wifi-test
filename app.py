#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from wifi import Cell, Scheme

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    cells = Cell.all('wlan0')
    return render_template('index.html', cells=cells)
