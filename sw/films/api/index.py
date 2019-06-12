from flask import Blueprint, make_response, Response, jsonify, request
from bson.json_util import dumps, ObjectId
from bson.errors import InvalidId
from sw import database, films
import re

blueprint = Blueprint('films', __name__)


@blueprint.route('')
def index() -> Response:
    q = request.args.get('q')
    if q is not None:
        search_expr = re.compile(f".*{q}.*", re.I)
        films_collection = database.DB.find(films.model.Films.COLLECTION, {'name': {'$regex': search_expr}})
        response = make_response(dumps(films_collection), 200)
    else:
        response = make_response(dumps([doc for doc in database.DB.all(films.model.Films.COLLECTION)]), 200)

    response.mimetype = 'application/json'

    return response


@blueprint.route('<string:id_film>')
def show(id_film: str) -> Response:
    try:
        film = database.DB.find_one(films.model.Films.COLLECTION, {'_id': ObjectId(id_film)})

        if film is None:
            response = make_response(jsonify({'message': 'No existe este documento'}), 200)
        else:
            response = make_response(dumps(film), 200)

        response.mimetype = 'application/json'

        return response
    except InvalidId as e:
        response = make_response(jsonify({'message': str(e)}), 404)
        response.mimetype = 'application/json'

        return response
