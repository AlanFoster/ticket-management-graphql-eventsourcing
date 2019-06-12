import pytest
from application.tickets import init_application, get_application, close_application


@pytest.fixture(scope="function")
def ticket_app():
    init_application()
    app = get_application()
    yield app
    close_application()
