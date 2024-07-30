"""
This module contains OpenAPI Documentation definition for the API.

It exposes a docs object that can be used to decorate request handlers with additional
information, used to generate OpenAPI documentation.
"""
from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

from app.docs.binders import set_binders_docs
from app.settings import Settings


def configure_docs(app: Application, settings: Settings, version: str):
    docs = OpenAPIHandler(
        info=Info(title=settings.info.title, version=settings.info.version, description=settings.info.description),
        anonymous_access=True,
        ui_path=f"/docs/{version}",
        json_spec_path = f"/openapi-{version}.json",
        yaml_spec_path = f"/openapi-{version}.yaml",
    )

    # include only endpoints whose path starts with "/api/"
    docs.include = lambda path, _: path.startswith(f"/api/{version}/")

    set_binders_docs(docs)

    docs.bind_app(app)
