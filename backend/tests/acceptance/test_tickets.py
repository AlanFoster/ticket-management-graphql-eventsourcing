from application.ticket_management import TicketApplication
from domain.ticket import Ticket


def test_create_ticket(ticket_app: TicketApplication):
    ticket = Ticket.__create__()
    ticket.__save__()

    saved: Ticket = ticket_app.repository[ticket.id]
    assert saved.id is not None
    assert saved.name is None


def test_rename_ticket(ticket_app: TicketApplication):
    ticket = Ticket.__create__()

    ticket.rename("New ticket name")
    ticket.__save__()

    saved: Ticket = ticket_app.repository[ticket.id]
    assert saved.id is not None
    assert saved.name == "New ticket name"


def test_delete_ticket(ticket_app: TicketApplication):
    ticket = Ticket.__create__()
    ticket.__discard__()
    ticket.__save__()

    assert ticket.id not in ticket_app.repository
