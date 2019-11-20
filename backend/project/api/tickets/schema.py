import graphene
from project.api.tickets.mutations import Mutation
from project.api.tickets.queries import Query
from project.api.tickets.types import TicketCloned, TicketFieldUpdated

schema = graphene.Schema(
    query=Query, mutation=Mutation, types=[TicketFieldUpdated, TicketCloned]
)
