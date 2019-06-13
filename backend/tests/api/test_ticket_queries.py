from graphene.test import Client
from api.schema import schema
from application.tickets import TicketsApplication


def test_get_ticket(snapshot, ticket_app: TicketsApplication):
    ticket = ticket_app.create_ticket(name="My ticket")
    client = Client(schema, context={"ticket_app": ticket_app})
    get_ticket = """
        query ($id: ID!) {
            ticket(id: $id) {
                name
            }
        }
    """

    executed = client.execute(get_ticket, variables={"id": str(ticket.id)})
    snapshot.assert_match(executed)


def test_get_tickets_when_none_created(snapshot, ticket_app: TicketsApplication):
    client = Client(schema, context={"ticket_app": ticket_app})
    get_tickets = """
        query {
            tickets {
                name
            }
        }
    """

    executed = client.execute(get_tickets, variables={})
    snapshot.assert_match(executed)


def test_get_tickets_when_multiple_created(snapshot, ticket_app: TicketsApplication):
    ticket_app.create_ticket(name="My first ticket")
    ticket_app.create_ticket(name="My second ticket")
    client = Client(schema, context={"ticket_app": ticket_app})
    get_tickets = """
        query {
            tickets {
                name
            }
        }
    """

    executed = client.execute(get_tickets, variables={})
    snapshot.assert_match(executed)
