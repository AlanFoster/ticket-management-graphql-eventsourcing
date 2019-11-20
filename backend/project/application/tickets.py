from typing import List, Optional

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from project.application.ticket_list_projection_policy import \
    TicketListProjectionPolicy
from project.domain.ticket import Ticket


class TicketsApplication(SQLAlchemyApplication):
    persist_event_type = (Ticket.Event, Ticket.Created, Ticket.Discarded)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ticket_list_projection_policy = TicketListProjectionPolicy()

    def create_ticket(
        self, name: Optional[str] = None, description: Optional[str] = None
    ) -> Ticket:
        ticket = Ticket.create(name=name, description=description)
        ticket.save()
        return ticket

    def get_ticket(self, id: str, at: int = None) -> Optional[Ticket]:
        if id in self.repository:
            return self.repository.get_entity(id, at=at)
        else:
            return None

    def clone_ticket(self, id: str) -> Ticket:
        old_ticket = self.repository[id]
        new_ticket = Ticket.create()
        new_ticket.clone(
            original_ticket_id=str(old_ticket.id),
            original_ticket_version=old_ticket.__version__,
        )
        new_ticket.save()
        return new_ticket

    def rename_ticket(self, id: str, name: str) -> None:
        ticket = self.get_ticket(id)
        assert ticket is not None

        ticket.rename(name=name)
        ticket.save()

    def update_ticket_description(self, id: str, description: str) -> None:
        ticket = self.get_ticket(id)
        assert ticket is not None

        ticket.update_description(description=description)
        ticket.save()

    def delete_ticket(self, id: str) -> None:
        ticket = self.get_ticket(id)
        assert ticket is not None

        ticket.discard()
        ticket.save()

    def get_tickets(self) -> List[Ticket]:
        projection_list = self.ticket_list_projection_policy.get_tickets()
        tickets = []
        for projection in projection_list:
            tickets.append(self.repository[projection.ticket_id])
        return tickets


_application: Optional["TicketsApplication"] = None


def construct_application(**kwargs) -> TicketsApplication:
    return TicketsApplication(**kwargs)


def init_application(**kwargs) -> None:
    """
    Constructs single global instance of application.
    To be called when initialising a worker process.
    """
    global _application
    if _application is not None:
        raise AssertionError("init_application() has already been called")
    _application = construct_application(**kwargs)


def get_application() -> TicketsApplication:
    """
    Returns single global instance of application.
    To be called when handling a worker request, if required.
    """
    if _application is None:
        raise AssertionError("get_application() must be called first")
    return _application


def close_application() -> None:
    """
    Shuts down single global instance of application.
    To be called when tearing down, perhaps between tests, in order to allow a
    subsequent call to init_application().
    """
    global _application
    if _application is not None:
        _application.close()
    _application = None
