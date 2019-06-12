from decimal import Decimal

from freezegun import freeze_time

from application.tickets import TicketsApplication
from domain.ticket import Ticket
from domain.tickets_projection import TicketListItem


def Any(cls):
    class Any(cls):
        def __eq__(self, other):
            return isinstance(other, cls)

        def __repr__(self):
            return f"[Any {cls.__name__}]"

        def __str__(self):
            return self.__repr__()

    return Any()


def test_create_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    assert ticket.id is not None
    assert ticket.name is None


def test_rename_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.rename_ticket(id=ticket_id, name="New ticket name")

    saved: Ticket = ticket_app.repository[ticket_id]
    assert saved.id is not None
    assert saved.name == "New ticket name"


def test_delete_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)

    ticket_app.delete_ticket(ticket_id)
    assert ticket_app.get_ticket(ticket_id) is None


def test_get_tickets_when_none_created(ticket_app: TicketsApplication):
    assert ticket_app.get_tickets() == []


def test_get_tickets_when_two_created(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket_app.create_ticket()
    with freeze_time("2012-01-15"):
        ticket_app.create_ticket()
    assert ticket_app.get_tickets() == [
        TicketListItem(ticket_id=Any(str), updated_at=Decimal("1326499200.000000")),
        TicketListItem(ticket_id=Any(str), updated_at=Decimal("1326585600.000000")),
    ]


def test_get_tickets_with_multiple_commands(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket = ticket_app.create_ticket()
        ticket_id = str(ticket.id)
    with freeze_time("2012-01-15"):
        ticket_app.rename_ticket(ticket_id, "New ticket name")

    assert ticket_app.get_tickets() == [
        TicketListItem(ticket_id=Any(str), updated_at=Decimal("1326585600.000000"))
    ]


def test_get_tickets_with_deleted_tickets(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.delete_ticket(ticket_id)

    assert ticket_app.get_tickets() == []
