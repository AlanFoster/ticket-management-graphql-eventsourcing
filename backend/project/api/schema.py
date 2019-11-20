import graphene

import project.api.tickets.schema


class Query(project.api.tickets.schema.Query, graphene.ObjectType):
    pass


class Mutation(project.api.tickets.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query, mutation=Mutation, types=project.api.tickets.schema.schema.types
)
