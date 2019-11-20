from freezegun import freeze_time
from graphene.test import Client

from project.api.resolve_info import Context
from project.api.schema import schema
from project.application.tickets import TicketsApplication
from tests.api import raise_original_error


@freeze_time("2012-01-14")
def test_get_ticket(snapshot, ticket_app: TicketsApplication, graphql_context: Context):
    ticket = ticket_app.create_ticket(
        name="My ticket", description="My ticket description"
    )
    ticket_app.rename_ticket(str(ticket.id), "Ticket renamed")
    ticket_app.update_ticket_description(str(ticket.id), "New ticket description")
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    get_ticket = """
        query ($id: ID!) {
            ticket(id: $id) {
                name
                description
                updatedAt
                history {
                    __typename
                    timestamp
                    ... on TicketFieldUpdated {
                        field
                        oldValue
                        newValue
                    }
                    ... on TicketCloned {
                        originalTicketId
                        originalTicketName
                    }
                }
            }
        }
    """

    executed = client.execute(get_ticket, variables={"id": str(ticket.id)})
    snapshot.assert_match(executed)


@freeze_time("2012-01-14")
def test_get_cloned_ticket(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    original_ticket = ticket_app.create_ticket(
        name="My ticket", description="My ticket description"
    )
    original_ticket_id = str(original_ticket.id)
    ticket_app.rename_ticket(original_ticket_id, "Original ticket name")
    ticket_app.update_ticket_description(
        original_ticket_id, "Original ticket description"
    )
    new_ticket = ticket_app.clone_ticket(id=original_ticket_id)
    new_ticket_id = str(new_ticket.id)
    ticket_app.rename_ticket(id=new_ticket_id, name="New ticket name")

    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    get_ticket = """
        query ($id: ID!) {
            ticket(id: $id) {
                name
                description
                updatedAt
                history {
                    __typename
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
    """

    executed = client.execute(get_ticket, variables={"id": new_ticket_id})
    snapshot.assert_match(executed)


@freeze_time("2012-01-14")
def test_get_tickets_when_none_created(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    get_tickets = """
        query {
            tickets {
                name
                description
                updatedAt
            }
        }
    """

    executed = client.execute(get_tickets, variables={})
    snapshot.assert_match(executed)


@freeze_time("2012-01-14")
def test_get_tickets_when_multiple_created(
    snapshot, ticket_app: TicketsApplication, graphql_context: Context
):
    ticket_app.create_ticket(name="My first ticket")
    ticket_app.create_ticket(name="My second ticket")
    client = Client(schema, context=graphql_context, format_error=raise_original_error)
    get_tickets = """
        query {
            tickets {
                name
                description
                updatedAt
            }
        }
    """

    executed = client.execute(get_tickets, variables={})
    snapshot.assert_match(executed)
