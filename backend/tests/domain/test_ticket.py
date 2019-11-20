from datetime import datetime

from freezegun import freeze_time

from project.domain.ticket import Ticket, TicketFieldUpdated


@freeze_time("2012-01-14")
def test_create_ticket():
    ticket = Ticket.create()

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.description is None
    assert ticket.history == []
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_create_ticket_with_provided_values():
    ticket = Ticket.create(
        name="Immediately named", description="Immediately described"
    )

    assert ticket.id is not None
    assert ticket.name == "Immediately named"
    assert ticket.description == "Immediately described"
    assert ticket.history == []
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_rename_ticket():
    ticket = Ticket.create()

    ticket.rename("New ticket name")

    assert ticket.id is not None
    assert ticket.name == "New ticket name"
    assert ticket.description is None
    assert ticket.history == [
        TicketFieldUpdated(
            field="name",
            old_value=None,
            new_value="New ticket name",
            timestamp=datetime(2012, 1, 14, 0, 0),
        )
    ]
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_update_description_ticket():
    ticket = Ticket.create()

    ticket.update_description("New ticket description")

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.description == "New ticket description"
    assert ticket.history == [
        TicketFieldUpdated(
            field="description",
            old_value=None,
            new_value="New ticket description",
            timestamp=datetime(2012, 1, 14, 0, 0),
        )
    ]
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_delete_ticket():
    ticket = Ticket.create()
    ticket.__discard__()

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.description is None
    assert ticket.history == []
    assert ticket.__is_discarded__
