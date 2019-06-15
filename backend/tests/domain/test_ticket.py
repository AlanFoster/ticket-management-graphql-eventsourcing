from freezegun import freeze_time

from domain.ticket import Ticket


@freeze_time("2012-01-14")
def test_create_ticket():
    ticket: Ticket = Ticket.__create__()

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.description == None
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_create_ticket_with_provided_values():
    ticket: Ticket = Ticket.__create__(
        name="Immediately named", description="Immediately described"
    )

    assert ticket.id is not None
    assert ticket.name == "Immediately named"
    assert ticket.description == "Immediately described"
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_rename_ticket():
    ticket: Ticket = Ticket.__create__()

    ticket.rename("New ticket name")

    assert ticket.id is not None
    assert ticket.name == "New ticket name"
    assert ticket.description is None
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_update_description_ticket():
    ticket: Ticket = Ticket.__create__()

    ticket.update_description("New ticket description")

    assert ticket.id is not None
    assert ticket.name == None
    assert ticket.description == "New ticket description"
    assert ticket.updated_at.isoformat() == "2012-01-14T00:00:00"


@freeze_time("2012-01-14")
def test_delete_ticket():
    ticket: Ticket = Ticket.__create__()
    ticket.__discard__()

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.description is None
    assert ticket.__is_discarded__
