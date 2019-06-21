import graphene

from api.tickets.mutations import Mutation
from api.tickets.queries import Query
from api.tickets.types import TicketFieldUpdated, TicketCloned

schema = graphene.Schema(
    query=Query, mutation=Mutation, types=[TicketFieldUpdated, TicketCloned]
)
