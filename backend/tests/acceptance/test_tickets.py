from application.tickets import TicketsApplication
from domain.ticket import Ticket


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
