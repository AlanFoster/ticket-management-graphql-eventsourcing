import api.tickets.schema
import graphene


class Query(api.tickets.schema.Query, graphene.ObjectType):
    pass


class Mutation(api.tickets.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query, mutation=Mutation, types=api.tickets.schema.schema.types
)
