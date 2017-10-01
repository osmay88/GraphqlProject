# flask_sqlalchemy/app.py
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask_graphql import GraphQLView

from models import db_session
from schema import schema, Users

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)


@app.route('/adduser', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()

        return 'all goog'
    elif request.method == 'GET':
        return render_template('adduser.html', **{})
    else:
        return 400


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()