from typing import Any

from blacksheep import Request, Response
from blacksheep.server import Application
from blacksheep.server.responses import json, text
from essentials.exceptions import (
    AcceptedException,
    ForbiddenException,
    NotImplementedException,
    ObjectNotFound,
    UnauthorizedException,
)


def configure_error_handlers(app: Application) -> None:
    async def bad_request_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        if request.path.startswith('/api'):
            return json({'error': str(exception) or "Bad Request"}, status=404)
        return text(str(exception) or "Bad Request", 404)

    async def not_found_handler(
        app: Application, request: Request, exception: Exception
    ) -> Response:
        if request.path.startswith('/api'):
            return json({'error': str(exception) or "Not found"}, status=404)
        return text(str(exception) or "Not found", 404)

    async def not_implemented(app: Application, request: Request, exception: Exception) -> Response:
        if request.path.startswith('/api'):
            return json({'error': "Not implemented"}, status=500)
        return text("Not implemented", status=500)

    async def unauthorized(app: Application, request: Request, exception: Exception) -> Response:
        if request.path.startswith('/api'):
            return json({'error': "Unauthorized"}, status=401)
        return text("Unauthorized", status=401)

    async def forbidden(app: Application, request: Request, exception: Exception) -> Response:
        if request.path.startswith('/api'):
            return json({'error': "Forbidden"}, status=403)
        return text("Forbidden", status=403)

    async def accepted(app: Application, request: Request, exception: Exception) -> Response:
        if request.path.startswith('/api'):
            return json({'error': "Accepted"}, status=202)
        return text("Accepted", status=202)

    app.exceptions_handlers.update(
        {
            400: bad_request_handler,
            404: not_found_handler,
            ObjectNotFound: not_found_handler,
            NotImplementedException: not_implemented,
            UnauthorizedException: unauthorized,
            ForbiddenException: forbidden,
            AcceptedException: accepted,
        }
    )
