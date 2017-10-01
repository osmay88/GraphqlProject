from flask import Blueprint
from flask.globals import request
import json

from schema import schema

bp = Blueprint('graphic', __name__)


@bp.route('/', methods=['POST',])
def query():
    payload = request.get_json(silent=True)
    if payload.get('query') is None:
        return 'Not good'
    query = payload['query']
    data = schema.execute(query)
    return json.dumps({'data': data.data, 'error': data.errors})
