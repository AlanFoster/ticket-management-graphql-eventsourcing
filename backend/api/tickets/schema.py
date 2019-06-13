import graphene
from typing import Iterable, Any, Optional

import domain.ticket
from application.tickets import TicketsApplication


class Ticket(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=False)

    @classmethod
    def from_model(cls, model: domain.ticket.Ticket):
        return cls(id=model.id, name=model.name)


class Query(graphene.ObjectType):
    ticket = graphene.Field(Ticket, id=graphene.ID(required=True))
    tickets = graphene.List(graphene.NonNull(Ticket))

    def resolve_tickets(self, info: graphene.ResolveInfo) -> Iterable[Ticket]:
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        tickets = ticket_app.get_tickets()
        return [Ticket.from_model(ticket) for ticket in tickets]

    def resolve_ticket(self, info: graphene.ResolveInfo, id: str) -> Ticket:
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket = ticket_app.get_ticket(id)
        return Ticket.from_model(ticket)


class CreateTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)
    ticket = graphene.Field(Ticket, required=True)

    class Arguments:
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root: Any, info: graphene.ResolveInfo, name: Optional[str] = None):
        ticket_app: TicketsApplication = info.context.get("ticket_app")
        ticket = ticket_app.create_ticket(name=name)
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


class Mutation(graphene.ObjectType):
    create_ticket = CreateTicket.Field()
    rename_ticket = RenameTicket.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[])
