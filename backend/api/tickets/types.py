import graphene
import domain.ticket


class HistoryItem(graphene.ObjectType):
    field = graphene.String(required=True)
    old_value = graphene.String(required=False)
    new_value = graphene.String(required=False)
    timestamp = graphene.types.datetime.DateTime(required=True)

    @classmethod
    def from_model(cls, model: domain.ticket.HistoryItem):
        return cls(
            field=model.field,
            old_value=model.old_value,
            new_value=model.new_value,
            timestamp=model.timestamp,
        )


class Ticket(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    updated_at = graphene.types.datetime.DateTime(required=True)
    history = graphene.NonNull(graphene.List(graphene.NonNull(HistoryItem)))

    @classmethod
    def from_model(cls, model: domain.ticket.Ticket):
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            updated_at=model.updated_at,
            history=[
                HistoryItem.from_model(history_item) for history_item in model.history
            ],
        )
