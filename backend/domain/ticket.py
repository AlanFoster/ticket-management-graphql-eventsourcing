from eventsourcing.domain.model.aggregate import AggregateRoot


class Ticket(AggregateRoot):
    def __init__(self, **kwargs):
        super(Ticket, self).__init__(**kwargs)
        self.name = None
        self.description = None

    class Event(AggregateRoot.Event):
        pass

    class Created(AggregateRoot.Created):
        pass

    class Discarded(AggregateRoot.Discarded):
        pass

    def rename(self, name: str):
        self.__trigger_event__(Ticket.Renamed, name=name)

    class Renamed(AggregateRoot.Event):
        @property
        def name(self):
            return self.__dict__["name"]

        def mutate(self, ticket: "Ticket"):
            ticket.name = self.name
