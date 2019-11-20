from graphql.error import GraphQLLocatedError


def raise_original_error(e: GraphQLLocatedError):
    """
    Raises the original error that has been wrapped within a GraphQLocatedError class.
    This is useful to ensure that the original stacktrace is printed to pytest, or
    when running with `pytest --pdb` a breakpoint will trigger as expected.
    If error formatter isn't used, Graphene will format the exception as a
    string within the returned GraphQL payload as normal.
    """
    if hasattr(e, "original_error"):
        raise e.original_error
    raise e
