import domain.ticket
import graphene


class HistoryItem(graphene.Interface):
    """
    The abstract base history item type. All history items must have an appropriate timestamp.
    Additional fields can be provided by the class that implements this interface.
    """

    timestamp = graphene.types.datetime.DateTime(required=True)

    @classmethod
    def from_model(cls, model: domain.ticket.HistoryItem):
        if isinstance(model, domain.ticket.TicketFieldUpdated):
            return TicketFieldUpdated.from_model(model)
        if isinstance(model, domain.ticket.TicketCloned):
            return TicketCloned.from_model(model)
        else:
            raise TypeError(f"Invalid model of type {model.__class__}")


class TicketFieldUpdated(graphene.ObjectType):
    class Meta:
        interfaces = (HistoryItem,)

    field = graphene.String(required=True)
    old_value = graphene.String(required=False)
    new_value = graphene.String(required=False)

    @classmethod
    def from_model(cls, model: domain.ticket.TicketFieldUpdated):
        return cls(
            field=model.field,
            old_value=model.old_value,
            new_value=model.new_value,
            timestamp=model.timestamp,
        )


class TicketCloned(graphene.ObjectType):
    class Meta:
        interfaces = (HistoryItem,)

    field = graphene.String(required=True)
    original_ticket_id = graphene.String(required=False)
    original_ticket_name = graphene.String(required=False)

    @classmethod
    def from_model(cls, model: domain.ticket.TicketCloned):
        return cls(
            original_ticket_id=model.original_ticket_id,
            original_ticket_name=model.original_ticket_name,
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
