from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from eventsourcing.domain.model.aggregate import AggregateRoot
from eventsourcing.utils.times import datetime_from_timestamp


@dataclass
class HistoryItem:
    """
    The base value object representing important historical events that may be useful
    to show to a user. All history items must have an appropriate timestamp. Additional
    fields can be provided by the class that extends this value object.
    """

    timestamp: datetime


@dataclass
class TicketFieldUpdated(HistoryItem):
    field: str
    old_value: Optional[str]
    new_value: str


@dataclass
class TicketCloned(HistoryItem):
    original_ticket_id: str
    original_ticket_name: str


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

    @classmethod
    def create(
        cls, name: Optional[str] = None, description: Optional[str] = None, **kwargs
    ) -> "Play":
        return super().__create__(name=name, description=description, **kwargs)

    def save(self) -> None:
        self.__save__()

    def discard(self) -> None:
        self.__discard__()

    def rename(self, name: str):
        self.__trigger_event__(Ticket.Renamed, name=name)

    def update_description(self, description: str):
        self.__trigger_event__(Ticket.DescriptionUpdated, description=description)

    def clone(self, original_ticket_id: str, original_ticket_version: int):
        self.__trigger_event__(
            Ticket.Cloned,
            original_ticket_id=original_ticket_id,
            original_ticket_version=original_ticket_version,
        )

    @property
    def updated_at(self) -> datetime:
        return datetime_from_timestamp(self.___last_modified__)

    class Renamed(Event):
        @property
        def name(self) -> str:
            return self.__dict__["name"]

        def mutate(self, ticket: "Ticket"):
            ticket.history.append(
                TicketFieldUpdated(
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
                TicketFieldUpdated(
                    field="description",
                    old_value=ticket.description,
                    new_value=self.description,
                    timestamp=datetime_from_timestamp(self.timestamp),
                )
            )

            ticket.description = self.description

    class Cloned(Event):
        @property
        def original_ticket_id(self) -> str:
            return self.__dict__["original_ticket_id"]

        @property
        def original_ticket_version(self) -> int:
            return self.__dict__["original_ticket_version"]

        def mutate(self, ticket: "Ticket"):
            # TODO: Investigate if there's a way to dependency inject this rather than reaching for the global app
            from application.tickets import get_application

            tickets_app = get_application()
            original_ticket = tickets_app.get_ticket(
                id=self.original_ticket_id, at=self.original_ticket_version
            )
            ticket.name = f"CLONED - {original_ticket.name}"
            ticket.description = original_ticket.description
            # When cloning a ticket, we decide not to copy the previous history but instead start fresh
            ticket.history = [
                TicketCloned(
                    original_ticket_id=self.original_ticket_id,
                    original_ticket_name=original_ticket.name,
                    timestamp=datetime_from_timestamp(self.timestamp),
                )
            ]
