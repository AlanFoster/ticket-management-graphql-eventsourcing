import json
import os

import pytest
from flask.testing import FlaskClient

from project.app import create_app
from project.application.tickets import close_application


@pytest.fixture(scope="function")
def client():
    config_overrides = {"DATABASE_URL": os.getenv("TEST_DATABASE_URL")}
    app = create_app(config_overrides)
    app.app_context().push()
    client = app.test_client()
    with app.test_request_context():
        yield client

    # Somewhat leaky: Cleaning up global tickets application manually
    close_application()


def test_healthcheck(client: FlaskClient):
    assert client.get("/health").data == b"OK"


def test_api(snapshot, client: FlaskClient):
    query = """
    {
      __schema {
        types {
          name
        }
      }
    }
    """

    assert json.loads(client.post(f"/graphql", json={"query": query}).data)
