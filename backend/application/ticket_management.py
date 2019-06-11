from typing import Optional

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication


class TicketApplication(SQLAlchemyApplication):
    pass


_application: Optional["TicketApplication"] = None


def construct_application(**kwargs) -> TicketApplication:
    return TicketApplication(**kwargs)


def init_application(**kwargs) -> None:
    """
    Constructs single global instance of application.
    To be called when initialising a worker process.
    """
    global _application
    if _application is not None:
        raise AssertionError("init_application() has already been called")
    _application = construct_application(**kwargs)


def get_application() -> TicketApplication:
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
