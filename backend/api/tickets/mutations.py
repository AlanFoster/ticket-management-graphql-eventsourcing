import graphene
from typing import Any, Optional

from api.tickets.types import Ticket
from application.tickets import TicketsApplication


class CreateTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)
    ticket = graphene.Field(Ticket, required=True)

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    @classmethod
    def mutate(
        cls,
        root: Any,
        info: graphene.ResolveInfo,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ):
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket = ticket_app.create_ticket(name=name, description=description)
        return cls(ok=True, ticket=Ticket.from_model(ticket))


class RenameTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root: Any, info: graphene.ResolveInfo, id: str, name: str):
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket_app.rename_ticket(id, name=name)
        return cls(ok=True)


class UpdateTicketDescription(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)
        description = graphene.String(required=True)

    @classmethod
    def mutate(cls, root: Any, info: graphene.ResolveInfo, id: str, description: str):
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket_app.update_ticket_description(id, description)
        return cls(ok=True)


class DeleteTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root: Any, info: graphene.ResolveInfo, id: str):
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket_app.delete_ticket(id)
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_ticket = CreateTicket.Field()
    rename_ticket = RenameTicket.Field()
    delete_ticket = DeleteTicket.Field()
    update_ticket_description = UpdateTicketDescription.Field()
