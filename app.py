#!/usr/bin/env python
# coding=utf-8

from flask import Flask
from sw import films, peoples, frontend
from sw.command.index import create_data
from sw.database import DB

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__, static_url_path=UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

DB.init()

app.register_blueprint(films.index.blueprint, url_prefix="/api/films/")
app.register_blueprint(peoples.index.blueprint, url_prefix="/api/peoples/")
app.register_blueprint(frontend.routes.blueprint)

app.cli.add_command(create_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
