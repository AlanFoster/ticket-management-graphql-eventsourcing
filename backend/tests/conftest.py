import pytest
from eventsourcing.domain.model.aggregate import AggregateRoot

from application.ticket_management import (
    init_application,
    get_application,
    close_application,
)


@pytest.fixture(scope="function")
def ticket_app():
    init_application(persist_event_type=AggregateRoot.Event)
    app = get_application()
    yield app
    close_application()
