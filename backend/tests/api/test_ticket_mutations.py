from graphene.test import Client
from api.schema import schema
from application.tickets import TicketsApplication
from domain.ticket import Ticket


def get_latest_ticket_as_dict(tickets_apps: TicketsApplication, ticket: Ticket):
    latest_ticket = tickets_apps.get_ticket(str(ticket.id))
    if latest_ticket is None:
        return None
    return {"name": latest_ticket.name}


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
    assert executed["data"]["createTicket"]["ok"]
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
    snapshot.assert_match(get_latest_ticket_as_dict(ticket_app, ticket))


def test_delete_ticket(snapshot, ticket_app: TicketsApplication):
    client = Client(schema, context={"ticket_app": ticket_app})
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
