from collections import OrderedDict
from dataclasses import dataclass
from decimal import Decimal
from typing import List, Dict


@dataclass
class TicketListItem:
    ticket_id: str
    updated_at: Decimal


class TicketListProjection:
    """
    Used to keep track of currently created tickets so that they could be shown on a user's dashboard for instance.
    This projection is currently in memory, but should be persisted.
    """

    def __init__(self):
        self.tickets: Dict[str, TicketListItem] = OrderedDict()

    def create(self, projection: TicketListItem) -> None:
        self.tickets[projection.ticket_id] = projection

    def update(self, projection: TicketListItem) -> None:
        self.tickets[projection.ticket_id] = projection

    def delete(self, projection: TicketListItem) -> None:
        del self.tickets[projection.ticket_id]

    def all(self) -> List[TicketListItem]:
        return list(self.tickets.values())
