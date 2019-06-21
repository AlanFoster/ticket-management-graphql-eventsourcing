from datetime import datetime
from typing import Dict, List, TypeVar, Generic, Callable, cast

from freezegun import freeze_time

from application.tickets import TicketsApplication
from domain.ticket import Ticket, TicketFieldUpdated, TicketCloned

RequiredInstanceT = TypeVar("RequiredInstanceT")


def Any(cls: Generic[RequiredInstanceT]) -> Generic[RequiredInstanceT]:
    class Any:
        def __eq__(self, other):
            return isinstance(other, cls)

        def __repr__(self):
            return f"[Any {cls.__name__}]"

        def __str__(self):
            return self.__repr__()

    return cast(RequiredInstanceT, Any())


def ticket_as_dict(ticket: Ticket) -> Dict[str, Any]:
    return {
        "id": str(ticket.id),
        "name": ticket.name,
        "description": ticket.description,
        "updated_at": ticket.updated_at.isoformat(),
        "history": ticket.history,
    }


def tickets_as_dict(tickets: List[Ticket]) -> List[Dict[str, Any]]:
    return list(map(ticket_as_dict, tickets))


def test_create_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    assert ticket_as_dict(ticket) == {
        "id": Any(str),
        "name": None,
        "description": None,
        "updated_at": Any(str),
        "history": [],
    }


def test_rename_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.rename_ticket(id=ticket_id, name="New ticket name")

    saved: Ticket = ticket_app.repository[ticket_id]
    assert ticket_as_dict(saved) == {
        "id": Any(str),
        "name": "New ticket name",
        "description": None,
        "updated_at": Any(str),
        "history": [
            TicketFieldUpdated(
                field="name",
                old_value=None,
                new_value="New ticket name",
                timestamp=Any(datetime),
            )
        ],
    }


def test_update_description_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.update_ticket_description(id=ticket_id, description="New description")

    saved: Ticket = ticket_app.repository[ticket_id]
    assert ticket_as_dict(saved) == {
        "id": Any(str),
        "name": None,
        "description": "New description",
        "updated_at": Any(str),
        "history": [
            TicketFieldUpdated(
                field="description",
                old_value=None,
                new_value="New description",
                timestamp=Any(datetime),
            )
        ],
    }


def test_delete_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)

    ticket_app.delete_ticket(ticket_id)
    assert ticket_app.get_ticket(ticket_id) is None


def test_clone_ticket(ticket_app: TicketsApplication):
    original_ticket = ticket_app.create_ticket(
        name="Original ticket name", description="Original ticket description"
    )
    original_ticket_id = str(original_ticket.id)

    new_ticket = ticket_app.clone_ticket(id=original_ticket_id)
    new_ticket_id = str(new_ticket.id)

    assert original_ticket_id != new_ticket_id
    assert ticket_as_dict(new_ticket) == {
        "id": Any(str),
        "name": "CLONED - Original ticket name",
        "description": "Original ticket description",
        "updated_at": Any(str),
        "history": [
            TicketCloned(
                original_ticket_id=original_ticket_id,
                original_ticket_name="Original ticket name",
                timestamp=Any(datetime),
            )
        ],
    }


def test_clone_ticket_are_not_impacted_by_changes_to_the_original(
    ticket_app: TicketsApplication
):
    original_ticket = ticket_app.create_ticket(
        name="Original ticket name", description="Original ticket description"
    )
    original_ticket_id = str(original_ticket.id)

    new_ticket = ticket_app.clone_ticket(id=original_ticket_id)
    new_ticket_id = str(new_ticket.id)
    ticket_app.rename_ticket(id=original_ticket_id, name="New ticket name")

    new_ticket_reloaded = ticket_app.get_ticket(new_ticket_id)

    assert original_ticket_id != str(new_ticket.id)
    assert ticket_as_dict(new_ticket_reloaded) == {
        "id": Any(str),
        "name": "CLONED - Original ticket name",
        "description": "Original ticket description",
        "updated_at": Any(str),
        "history": [
            TicketCloned(
                original_ticket_id=original_ticket_id,
                original_ticket_name="Original ticket name",
                timestamp=Any(datetime),
            )
        ],
    }


def test_get_tickets_when_none_created(ticket_app: TicketsApplication):
    assert ticket_app.get_tickets() == []


def test_get_tickets_when_two_created(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket_app.create_ticket(name="first ticket")
    with freeze_time("2012-01-15"):
        ticket_app.create_ticket(name="second ticket")

    assert tickets_as_dict(ticket_app.get_tickets()) == [
        {
            "id": Any(str),
            "name": "first ticket",
            "description": None,
            "updated_at": "2012-01-14T00:00:00",
            "history": [],
        },
        {
            "id": Any(str),
            "name": "second ticket",
            "description": None,
            "updated_at": "2012-01-15T00:00:00",
            "history": [],
        },
    ]


def test_get_tickets_with_multiple_commands(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket = ticket_app.create_ticket(name="original name")
        ticket_id = str(ticket.id)
    with freeze_time("2012-01-15"):
        ticket_app.rename_ticket(ticket_id, "new ticket name")
        ticket_app.update_ticket_description(ticket_id, "new ticket description")

    assert tickets_as_dict(ticket_app.get_tickets()) == [
        {
            "id": Any(str),
            "name": "new ticket name",
            "description": "new ticket description",
            "updated_at": "2012-01-15T00:00:00",
            "history": [
                TicketFieldUpdated(
                    field="name",
                    old_value="original name",
                    new_value="new ticket name",
                    timestamp=datetime(year=2012, month=1, day=15),
                ),
                TicketFieldUpdated(
                    field="description",
                    old_value=None,
                    new_value="new ticket description",
                    timestamp=datetime(year=2012, month=1, day=15),
                ),
            ],
        }
    ]


def test_get_tickets_with_deleted_tickets(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.delete_ticket(ticket_id)

    assert ticket_app.get_tickets() == []
