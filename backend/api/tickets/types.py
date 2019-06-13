from datetime import datetime

import graphene
import domain.ticket


class Ticket(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=False)
    updated_at = graphene.types.datetime.DateTime(required=True)

    @classmethod
    def from_model(cls, model: domain.ticket.Ticket):
        return cls(id=model.id, name=model.name, updated_at=datetime.now())
