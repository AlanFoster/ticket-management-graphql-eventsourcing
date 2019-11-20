from api.resolve_info import Context
from api.schema import schema
from application.tickets import TicketsApplication
from domain.ticket import Ticket
from freezegun import freeze_time
from graphene.test import Client
from tests.api import raise_original_error


def get_latest_ticket_as_dict(tickets_apps: TicketsApplication, ticket: Ticket):
    latest_ticket = tickets_apps.get_ticket(str(ticket.id))
    if latest_ticket is None:
        return None
    return {"name": latest_ticket.name, "description": latest_ticket.description}


def test_create_ticket(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    create_ticket = """
        mutation ($name: String!, $description: String!) {
            createTicket(name: $name, description: $description) {
                ok
                ticket {
                    name
                    description
                }
            }
        }
    """

    executed = client.execute(
        create_ticket,
        variables={
            "name": "testing ticket",
            "description": "testing ticket description",
        },
    )
    assert executed["data"]["createTicket"]["ok"]
    snapshot.assert_match(executed)


def test_rename_ticket(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    ticket = ticket_app.create_ticket(name="My ticket")

    create_ticket = """
        mutation ($id: ID!, $name: String!) {
            renameTicket(id: $id, name: $name) {
                ok
            }
        }
    """
    executed = client.execute(
        create_ticket, variables={"id": str(ticket.id), "name": "testing ticket"}
    )

    assert executed["data"]["renameTicket"]["ok"]
    snapshot.assert_match(get_latest_ticket_as_dict(ticket_app, ticket))


def test_update_ticket_description(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    ticket = ticket_app.create_ticket(name="My ticket")

    create_ticket = """
        mutation ($id: ID!, $description: String!) {
            updateTicketDescription(id: $id, description: $description) {
                ok
            }
        }
    """
    executed = client.execute(
        create_ticket,
        variables={"id": str(ticket.id), "description": "updated description"},
    )

    assert executed["data"]["updateTicketDescription"]["ok"]
    snapshot.assert_match(get_latest_ticket_as_dict(ticket_app, ticket))


def test_delete_ticket(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    ticket = ticket_app.create_ticket(name="My ticket")

    delete_ticket = """
        mutation ($id: ID!) {
            deleteTicket(id: $id) {
                ok
            }
        }
    """
    executed = client.execute(delete_ticket, variables={"id": str(ticket.id)})

    assert executed["data"]["deleteTicket"]["ok"]
    snapshot.assert_match(get_latest_ticket_as_dict(ticket_app, ticket))


@freeze_time("2012-01-14")
def test_clone_ticket(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    original_ticket = ticket_app.create_ticket(name="My ticket")
    original_ticket_id = str(original_ticket.id)

    delete_ticket = """
        mutation ($id: ID!) {
            cloneTicket(id: $id) {
                ok
                ticket {
                    name
                    description
                    history {
                        __typename
                        timestamp
                        ... on TicketFieldUpdated {
                            field
                            oldValue
                            newValue
                        }
                        ... on TicketCloned {
                            originalTicketName
                        }
                    }
                }
            }
        }
    """
    executed = client.execute(delete_ticket, variables={"id": original_ticket_id})

    assert executed["data"]["cloneTicket"]["ok"]
    snapshot.assert_match(executed)
