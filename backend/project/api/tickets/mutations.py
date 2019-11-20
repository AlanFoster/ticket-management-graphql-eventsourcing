from typing import Any, Optional

import graphene

from project.api.resolve_info import ResolveInfo
from project.api.tickets.types import Ticket


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
        info: ResolveInfo,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ):
        ticket_app = info.context.ticket_app
        ticket = ticket_app.create_ticket(name=name, description=description)
        return cls(ok=True, ticket=Ticket.from_model(ticket))


class RenameTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root: Any, info: ResolveInfo, id: str, name: str):
        ticket_app = info.context.ticket_app
        ticket_app.rename_ticket(id, name=name)
        return cls(ok=True)


class CloneTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)
    ticket = graphene.Field(Ticket, required=True)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root: Any, info: ResolveInfo, id: str):
        ticket_app = info.context.ticket_app
        new_ticket = ticket_app.clone_ticket(id)
        return cls(ok=True, ticket=Ticket.from_model(new_ticket))


class UpdateTicketDescription(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)
        description = graphene.String(required=True)

    @classmethod
    def mutate(cls, root: Any, info: ResolveInfo, id: str, description: str):
        ticket_app = info.context.ticket_app
        ticket_app.update_ticket_description(id, description)
        return cls(ok=True)


class DeleteTicket(graphene.Mutation):
    ok = graphene.Boolean(required=True)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root: Any, info: ResolveInfo, id: str):
        ticket_app = info.context.ticket_app
        ticket_app.delete_ticket(id)
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_ticket = CreateTicket.Field()
    rename_ticket = RenameTicket.Field()
    clone_ticket = CloneTicket.Field()
    delete_ticket = DeleteTicket.Field()
    update_ticket_description = UpdateTicketDescription.Field()
