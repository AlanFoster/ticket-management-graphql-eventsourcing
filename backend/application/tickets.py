from typing import Optional

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from domain.ticket import Ticket


class TicketsApplication(SQLAlchemyApplication):
    def create_ticket(self) -> Ticket:
        ticket = Ticket.__create__()
        ticket.__save__()
        return ticket

    def get_ticket(self, id: str) -> Optional[Ticket]:
        if id in self.repository:
            return self.repository[id]
        else:
            return None

    def rename_ticket(self, id: str, name: str) -> None:
        ticket = self.get_ticket(id)
        ticket.rename(name=name)
        ticket.__save__()

    def delete_ticket(self, id: str) -> None:
        ticket = self.get_ticket(id)
        ticket.__discard__()
        ticket.__save__()


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
