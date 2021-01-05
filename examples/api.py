from typing import Dict, Any

from flask import Blueprint

from examples.app_service import AppService

# TODO: think over class wrapper


def construct_examples_bp(app_service: AppService) -> Blueprint:
    bp = Blueprint('examples', __name__, url_prefix='/examples')

    @bp.route("/<str:id>")
    def get(id: str) -> Dict[str, Any]:
        return {}

    return bp


