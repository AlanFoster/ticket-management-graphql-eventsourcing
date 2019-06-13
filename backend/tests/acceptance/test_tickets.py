from typing import Dict, List

from freezegun import freeze_time

from application.tickets import TicketsApplication
from domain.ticket import Ticket


def Any(cls):
    class Any(cls):
        def __eq__(self, other):
            return isinstance(other, cls)

        def __repr__(self):
            return f"[Any {cls.__name__}]"

        def __str__(self):
            return self.__repr__()

    return Any()


def ticket_as_dict(ticket: Ticket) -> Dict[str, Any]:
    return {"id": str(ticket.id), "name": ticket.name}


def tickets_as_dict(tickets: List[Ticket]) -> List[Dict[str, Any]]:
    return list(map(ticket_as_dict, tickets))


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
        ticket_app.create_ticket(name="first ticket")
    with freeze_time("2012-01-15"):
        ticket_app.create_ticket(name="second ticket")

    assert tickets_as_dict(ticket_app.get_tickets()) == [
        {"id": Any(str), "name": "first ticket"},
        {"id": Any(str), "name": "second ticket"},
    ]


def test_get_tickets_with_multiple_commands(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket = ticket_app.create_ticket(name="original name")
        ticket_id = str(ticket.id)
    with freeze_time("2012-01-15"):
        ticket_app.rename_ticket(ticket_id, "new ticket name")

    assert tickets_as_dict(ticket_app.get_tickets()) == [
        {"id": Any(str), "name": "new ticket name"}
    ]


def test_get_tickets_with_deleted_tickets(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.delete_ticket(ticket_id)

    assert ticket_app.get_tickets() == []
