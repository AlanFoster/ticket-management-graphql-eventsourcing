import graphene

from api.tickets.mutations import Mutation
from api.tickets.queries import Query

schema = graphene.Schema(query=Query, mutation=Mutation, types=[])
