from eventsourcing.domain.model.events import subscribe, unsubscribe
from project.domain.ticket import Ticket
from project.domain.tickets_projection import (TicketListItem,
                                               TicketListProjection)


class TicketListProjectionPolicy(object):
    def __init__(self):
        self.projection: TicketListProjection = TicketListProjection()
        subscribe(self.add_ticket, self.is_ticket_created)
        subscribe(self.update_ticket, self.is_ticket_updated)
        subscribe(self.delete_ticket, self.is_ticket_deleted)

    def close(self) -> None:
        unsubscribe(self.add_ticket, self.is_ticket_created)
        unsubscribe(self.update_ticket, self.is_ticket_updated)
        unsubscribe(self.delete_ticket, self.is_ticket_deleted)

    def get_tickets(self):
        return self.projection.all()

    # Adding tickets
    def is_ticket_created(self, event) -> bool:
        if isinstance(event, (list, tuple)):
            return all(map(self.is_ticket_created, event))
        return isinstance(event, Ticket.Created)

    def add_ticket(self, event: Ticket.Created) -> None:
        assert isinstance(event, list)
        event = event[0]
        assert isinstance(event, Ticket.Created)

        self.projection.create(
            TicketListItem(
                ticket_id=str(event.originator_id), updated_at=event.timestamp
            )
        )

    # Updating tickets
    def is_ticket_updated(self, event) -> bool:
        if isinstance(event, (list, tuple)):
            return all(map(self.is_ticket_updated, event))
        return isinstance(event, Ticket.Event)

    def update_ticket(self, event: Ticket.Event) -> None:
        assert isinstance(event, list)
        event = event[0]
        assert isinstance(event, Ticket.Event)

        self.projection.update(
            TicketListItem(
                ticket_id=str(event.originator_id), updated_at=event.timestamp
            )
        )

    # Deleting tickets

    def is_ticket_deleted(self, event) -> bool:
        if isinstance(event, (list, tuple)):
            return all(map(self.is_ticket_deleted, event))
        return isinstance(event, Ticket.Discarded)

    def delete_ticket(self, event: Ticket.Discarded) -> None:
        assert isinstance(event, list)
        event = event[0]
        assert isinstance(event, Ticket.Discarded)

        self.projection.delete(
            TicketListItem(
                ticket_id=str(event.originator_id), updated_at=event.timestamp
            )
        )
