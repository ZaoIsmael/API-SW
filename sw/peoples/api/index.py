from flask import Blueprint, make_response, Response
from bson.json_util import dumps
from sw import database, peoples

blueprint = Blueprint('peoples', __name__)


@blueprint.route('')
def index() -> Response:
    response = make_response(dumps([doc for doc in database.DB.all(peoples.model.Peoples.COLLECTION)]), 200)
    response.mimetype = 'application/json'

    return response
