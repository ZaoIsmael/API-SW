import os
import uuid

from functools import wraps
from bson.errors import InvalidId
from bson.json_util import ObjectId
from flask import Blueprint, render_template, abort, request, flash, redirect, send_from_directory, session

from sw import database, peoples, films

blueprint = Blueprint('frontend', __name__, template_folder='templates')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def save_urls(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = 'urls'
        if key in session:
            urls = session[key][:9]
            session[key] = [request.url, *urls]
        else:
            session[key] = [request.url]

        return f(*args, **kwargs)

    return decorated_function


@blueprint.route('/')
@save_urls
def index() -> str:
    return render_template('index.html', peoples=[doc for doc in database.DB.all(peoples.model.Peoples.COLLECTION)])


@blueprint.route('/films/<string:id_film>')
@save_urls
def films_index(id_film: str) -> str:
    try:
        film = database.DB.find_one(films.model.Films.COLLECTION, {'_id': ObjectId(id_film)})

        if film is None:
            abort(404)

        return render_template('film.html', film=film)
    except InvalidId as _:
        abort(404)


@blueprint.route('/peoples/<string:id_people>', methods=['GET'])
@save_urls
def peoples_index_get(id_people: str) -> str:
    try:
        people = database.DB.find_one(peoples.model.Peoples.COLLECTION, {'_id': ObjectId(id_people)})

        if people is None:
            abort(404)

        return render_template('people.html', people=people)
    except InvalidId as _:
        abort(404)


@blueprint.route('/peoples/<string:id_people>', methods=['POST'])
def peoples_index_post(id_people: str) -> str:
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = str(uuid.uuid4())
        file.save(os.path.join('uploads', filename))

        database.DB.update_one(
            peoples.model.Peoples.COLLECTION,
            {'_id': ObjectId(id_people)},
            {'$push': {'files': filename}}
        )

        flash('Fichero añadido')

        return redirect(request.url)


@blueprint.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory('uploads', filename)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
