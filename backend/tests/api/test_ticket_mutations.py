from graphene.test import Client
from api.schema import schema
from application.tickets import TicketsApplication
from domain.ticket import Ticket


def get_ticket_as_dict(ticket: Ticket):
    return {"name": ticket.name}


def test_create_ticket(snapshot, ticket_app: TicketsApplication):
    client = Client(schema, context={"ticket_app": ticket_app})
    create_ticket = """
        mutation ($name: String!) {
            createTicket(name: $name) {
                ok
                ticket {
                    name
                }
            }
        }
    """

    executed = client.execute(create_ticket, variables={"name": "testing ticket"})
    snapshot.assert_match(executed)


def test_rename_ticket(snapshot, ticket_app: TicketsApplication):
    client = Client(schema, context={"ticket_app": ticket_app})
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
    snapshot.assert_match(get_ticket_as_dict(ticket))
