from typing import Iterable

import graphene
from api.resolve_info import ResolveInfo
from api.tickets.types import Ticket
from application.tickets import TicketsApplication


class Query(graphene.ObjectType):
    ticket = graphene.Field(Ticket, id=graphene.ID(required=True))
    tickets = graphene.NonNull(graphene.List(graphene.NonNull(Ticket)))

    def resolve_tickets(self, info: ResolveInfo) -> Iterable[Ticket]:
        ticket_app: TicketsApplication = info.context.ticket_app
        tickets = ticket_app.get_tickets()
        return [Ticket.from_model(ticket) for ticket in tickets]

    def resolve_ticket(self, info: ResolveInfo, id: str) -> Ticket:
        ticket_app: TicketsApplication = info.context.ticket_app
        ticket = ticket_app.get_ticket(id)
        return Ticket.from_model(ticket)
