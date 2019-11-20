from datetime import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from freezegun import freeze_time

from project.application.tickets import TicketsApplication
from project.domain.ticket import Ticket, TicketCloned, TicketFieldUpdated
from tests.helpers import AssertableTicket, any_instance_of


def tickets_as_assertable_tickets(tickets: List[Ticket]) -> List[AssertableTicket]:
    return list(map(AssertableTicket.from_model, tickets))


def test_create_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    assert AssertableTicket.from_model(ticket) == AssertableTicket(
        id=any_instance_of(str),
        name=None,
        description=None,
        updated_at=any_instance_of(str),
        history=[],
    )


def test_rename_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.rename_ticket(id=ticket_id, name="New ticket name")

    saved = ticket_app.repository[ticket_id]
    assert AssertableTicket.from_model(saved) == AssertableTicket(
        id=any_instance_of(str),
        name="New ticket name",
        description=None,
        updated_at=any_instance_of(str),
        history=[
            TicketFieldUpdated(
                field="name",
                old_value=None,
                new_value="New ticket name",
                timestamp=any_instance_of(datetime),
            )
        ],
    )


def test_update_description_ticket(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.update_ticket_description(id=ticket_id, description="New description")

    saved = ticket_app.repository[ticket_id]
    assert AssertableTicket.from_model(saved) == AssertableTicket(
        id=any_instance_of(str),
        name=None,
        description="New description",
        updated_at=any_instance_of(str),
        history=[
            TicketFieldUpdated(
                field="description",
                old_value=None,
                new_value="New description",
                timestamp=any_instance_of(datetime),
            )
        ],
    )


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
    assert AssertableTicket.from_model(new_ticket) == AssertableTicket(
        id=any_instance_of(str),
        name="CLONED - Original ticket name",
        description="Original ticket description",
        updated_at=any_instance_of(str),
        history=[
            TicketCloned(
                original_ticket_id=original_ticket_id,
                original_ticket_name="Original ticket name",
                timestamp=any_instance_of(datetime),
            )
        ],
    )


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
    assert AssertableTicket.from_model(new_ticket_reloaded) == AssertableTicket(
        id=any_instance_of(str),
        name="CLONED - Original ticket name",
        description="Original ticket description",
        updated_at=any_instance_of(str),
        history=[
            TicketCloned(
                original_ticket_id=original_ticket_id,
                original_ticket_name="Original ticket name",
                timestamp=any_instance_of(datetime),
            )
        ],
    )


def test_get_tickets_when_none_created(ticket_app: TicketsApplication):
    assert ticket_app.get_tickets() == []


def test_get_tickets_when_two_created(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket_app.create_ticket(name="first ticket")
    with freeze_time("2012-01-15"):
        ticket_app.create_ticket(name="second ticket")

    assert tickets_as_assertable_tickets(ticket_app.get_tickets()) == [
        AssertableTicket(
            id=any_instance_of(str),
            name="first ticket",
            description=None,
            updated_at="2012-01-14T00:00:00",
            history=[],
        ),
        AssertableTicket(
            id=any_instance_of(str),
            name="second ticket",
            description=None,
            updated_at="2012-01-15T00:00:00",
            history=[],
        ),
    ]


def test_get_tickets_with_multiple_commands(ticket_app: TicketsApplication):
    with freeze_time("2012-01-14"):
        ticket = ticket_app.create_ticket(name="original name")
        ticket_id = str(ticket.id)
    with freeze_time("2012-01-15"):
        ticket_app.rename_ticket(ticket_id, "new ticket name")
        ticket_app.update_ticket_description(ticket_id, "new ticket description")

    assert tickets_as_assertable_tickets(ticket_app.get_tickets()) == [
        AssertableTicket(
            id=any_instance_of(str),
            name="new ticket name",
            description="new ticket description",
            updated_at="2012-01-15T00:00:00",
            history=[
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
        )
    ]


def test_get_tickets_with_deleted_tickets(ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket()
    ticket_id = str(ticket.id)
    ticket_app.delete_ticket(ticket_id)

    assert ticket_app.get_tickets() == []
