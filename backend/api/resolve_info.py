from dataclasses import dataclass

import graphene
from application.tickets import TicketsApplication


@dataclass
class Context:
    """
    The GraphQL context object should be used for storing useful information/objects
    which each resolver will have access to. For instance, details about the current user,
    service clients, access to the database, etc.

    This context will be explicitly created by tests, or the flask entrypoint,
    and any of the required dependencies will be dependency injected.
    """

    ticket_app: TicketsApplication


class ResolveInfo(graphene.ResolveInfo):
    """
    Note, this class should not be instantiated directly, instead it is used purely for type
    checking.

    To correctly type check your code, your GraphQL resolvers should specify the type `info` to
    be an instance of this class, rather than the normal `info: graphene.ResolveInfo`
    """

    @property
    def context(self) -> Context:
        ...
