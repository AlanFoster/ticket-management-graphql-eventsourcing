from freezegun import freeze_time
from graphene.test import Client
from api.schema import schema
from application.tickets import TicketsApplication


@freeze_time("2012-01-14")
def test_get_ticket(snapshot, ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket(
        name="My ticket", description="My ticket description"
    )
    ticket_app.rename_ticket(str(ticket.id), "Ticket renamed")
    ticket_app.update_ticket_description(str(ticket.id), "New ticket description")
    client = Client(schema, context={"ticket_app": ticket_app})
    get_ticket = """
        query ($id: ID!) {
            ticket(id: $id) {
                name
                description
                updatedAt
                history {
                    field
                    oldValue
                    newValue
                    timestamp
                }
            }
        }
    """

    executed = client.execute(get_ticket, variables={"id": str(ticket.id)})
    snapshot.assert_match(executed)


@freeze_time("2012-01-14")
def test_get_tickets_when_none_created(snapshot, ticket_app: TicketsApplication):
    client = Client(schema, context={"ticket_app": ticket_app})
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
def test_get_tickets_when_multiple_created(snapshot, ticket_app: TicketsApplication):
    ticket_app.create_ticket(name="My first ticket")
    ticket_app.create_ticket(name="My second ticket")
    client = Client(schema, context={"ticket_app": ticket_app})
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
