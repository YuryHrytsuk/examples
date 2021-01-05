import gunicorn.app.base
from elasticsearch import Elasticsearch
from flask import Flask

from examples.api import construct_examples_bp


es_client = Elasticsearch(hosts=["elasticsearch"])

settings = {
    "mappings": {
        "properties": {
            "text": {
                "type": "text"
            },
            "description": {
                "type": "text"
            },
            "tags": {
                "type": "keyword",
            },
        }
    }
}

es_client.indices.create(index='examples', body=settings)


def create_app():
    app = Flask(__name__)

    app.register_blueprint(construct_examples_bp())

    return app


class WebApplication(gunicorn.app.base.BaseApplication):

    def init(self, parser, opts, args):
        pass

    def __init__(self, app, options=None):
        if options is None:
            options = {}

        self.options = options
        self.application = app

        super().__init__()

    def load_config(self):
        config = {
            key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
