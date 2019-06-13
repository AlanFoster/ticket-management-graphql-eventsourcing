from datetime import datetime
from typing import Optional

from eventsourcing.domain.model.aggregate import AggregateRoot
from eventsourcing.utils.times import datetime_from_timestamp


class Ticket(AggregateRoot):
    def __init__(self, name: Optional[str] = None, **kwargs):
        super(Ticket, self).__init__(**kwargs)
        self.name = name
        self.description = None

    class Event(AggregateRoot.Event):
        pass

    class Created(AggregateRoot.Created):
        pass

    class Discarded(AggregateRoot.Discarded):
        pass

    def rename(self, name: str):
        self.__trigger_event__(Ticket.Renamed, name=name)

    @property
    def updated_at(self) -> datetime:
        return datetime_from_timestamp(self.___last_modified__)

    class Renamed(Event):
        @property
        def name(self):
            return self.__dict__["name"]

        def mutate(self, ticket: "Ticket"):
            ticket.name = self.name
