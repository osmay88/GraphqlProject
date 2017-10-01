from flask import Flask


class Gapp(object):

    def __init__(self, import_name):
        super(Gapp, self).__init__()

        self._flask_app = Flask(import_name=import_name)
        self.init_bp()

    def init_bp(self):
        from bp.graphic import bp as graphic_bp
        self._flask_app.register_blueprint(graphic_bp, url_prefix='/graphic')

    def run_app(self):
        self._flask_app.run()


if __name__ == '__main__':
    app = Gapp(__name__)
    app.run_app()

