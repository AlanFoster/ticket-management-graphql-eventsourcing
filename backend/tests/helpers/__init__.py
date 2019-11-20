from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attr import dataclass

from project.domain.ticket import HistoryItem, Ticket

RequiredInstanceT = TypeVar("RequiredInstanceT")


def any_instance_of(cls: Type[RequiredInstanceT]) -> RequiredInstanceT:
    class Any:
        def __eq__(self, other):
            return isinstance(other, cls)

        def __repr__(self):
            return f"[Any {cls.__name__}]"

        def __str__(self):
            return self.__repr__()

    return cast(RequiredInstanceT, Any())


@dataclass
class AssertableTicket:
    """
    AssertableTicket cherry-picks the attributes from the Ticket domain model that we
    wish to assert against in our tests. This is done to ignore unrelated attributes
    that the Ticket domain model inherits from the base AggregateRoot class, i.e. the
    third party library attributes that used to implement event sourcing in this application.
    """

    id: str
    name: Optional[str]
    description: Optional[str]
    updated_at: str
    history: List[HistoryItem]

    @classmethod
    def from_model(cls, ticket: Ticket):
        return cls(
            id=str(ticket.id),
            name=ticket.name,
            description=ticket.description,
            updated_at=ticket.updated_at.isoformat(),
            history=ticket.history,
        )
