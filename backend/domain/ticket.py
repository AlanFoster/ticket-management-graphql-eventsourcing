from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from eventsourcing.domain.model.aggregate import AggregateRoot
from eventsourcing.utils.times import datetime_from_timestamp


@dataclass
class HistoryItem:
    field: str
    old_value: str
    new_value: str
    timestamp: datetime


class Ticket(AggregateRoot):
    def __init__(
        self, name: Optional[str] = None, description: Optional[str] = None, **kwargs
    ):
        super(Ticket, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.history: List[HistoryItem] = []

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
            ticket.history.append(
                HistoryItem(
                    field="name",
                    old_value=ticket.name,
                    new_value=self.name,
                    timestamp=datetime_from_timestamp(self.timestamp),
                )
            )
            ticket.name = self.name

    class DescriptionUpdated(Event):
        @property
        def description(self) -> str:
            return self.__dict__["description"]

        def mutate(self, ticket: "Ticket"):
            ticket.history.append(
                HistoryItem(
                    field="description",
                    old_value=ticket.description,
                    new_value=self.description,
                    timestamp=datetime_from_timestamp(self.timestamp),
                )
            )

            ticket.description = self.description
