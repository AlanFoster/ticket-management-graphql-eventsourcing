import pytest

from project.api.resolve_info import Context
from project.application.tickets import (TicketsApplication, close_application,
                                         get_application, init_application)

pytest.register_assert_rewrite("tests.helpers")


@pytest.fixture(scope="function")
def ticket_app():
    init_application()
    app = get_application()
    yield app
    close_application()


@pytest.fixture(scope="function")
def graphql_context(ticket_app: TicketsApplication):
    return Context(ticket_app=ticket_app)
