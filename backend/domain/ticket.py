from datetime import datetime
from typing import Optional

from eventsourcing.domain.model.aggregate import AggregateRoot
from eventsourcing.utils.times import datetime_from_timestamp


class Ticket(AggregateRoot):
    def __init__(
        self, name: Optional[str] = None, description: Optional[str] = None, **kwargs
    ):
        super(Ticket, self).__init__(**kwargs)
        self.name = name
        self.description = description

    class Event(AggregateRoot.Event):
        pass

    class Created(AggregateRoot.Created):
        pass

    class Discarded(AggregateRoot.Discarded):
        pass

    def rename(self, name: str):
        self.__trigger_event__(Ticket.Renamed, name=name)

    def update_description(self, description: str):
        self.__trigger_event__(Ticket.DescriptionUpdated, description=description)

    @property
    def updated_at(self) -> datetime:
        return datetime_from_timestamp(self.___last_modified__)

    class Renamed(Event):
        @property
        def name(self) -> str:
            return self.__dict__["name"]

        def mutate(self, ticket: "Ticket"):
            ticket.name = self.name

    class DescriptionUpdated(Event):
        @property
        def description(self) -> str:
            return self.__dict__["description"]

        def mutate(self, ticket: "Ticket"):
            ticket.description = self.description
