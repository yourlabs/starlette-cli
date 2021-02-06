#!/usr/bin/env python3
import apps

from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse

project = apps.Project(
    APPS=['starlette_cli']
)


class TestMiddleware:
    def __init__(self, app, some):
        self.app = app

    async def __call__(self, scope, receive, send):
        return await self.app(scope, receive, send)


def test_view(*args):
    return PlainTextResponse('ok')


app = project.starlette(
    routes=[Route('/', test_view)],
    middleware=[Middleware(TestMiddleware, some='thing')]
)

if __name__ == '__main__':
    project.apps['cli'].entry_point()
