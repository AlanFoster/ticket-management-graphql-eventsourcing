from domain.ticket import Ticket


def test_create_ticket():
    ticket = Ticket.__create__()

    assert ticket.id is not None
    assert ticket.name is None


def test_rename_ticket():
    ticket = Ticket.__create__()

    ticket.rename("New ticket name")

    assert ticket.id is not None
    assert ticket.name is "New ticket name"


def test_delete_ticket():
    ticket = Ticket.__create__()
    ticket.__discard__()

    assert ticket.id is not None
    assert ticket.name is None
    assert ticket.__is_discarded__
