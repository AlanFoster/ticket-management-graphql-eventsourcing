import pytest
from application.tickets import init_application, get_application, close_application
from domain.ticket import Ticket


@pytest.fixture(scope="function")
def ticket_app():
    init_application(persist_event_type=Ticket.Event)
    app = get_application()
    yield app
    close_application()
