import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView

db = SQLAlchemy()


def create_app(**config_overrides):
    # create and configure the app
    app = Flask(__name__)
    db.init_app(app)
    CORS(app)

    app.config.from_pyfile("config.py")
    app.config.update(config_overrides)

    migrate = Migrate(app, db)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from application.tickets import init_application, get_application
    from infrastructure import records

    @app.before_first_request
    def before_first_request():
        init_application(session=db.session)

    from api.schema import schema

    app.add_url_rule("/health", view_func=lambda: "OK")
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=app.debug,
            get_context=lambda: {"ticket_app": get_application()},
        ),
    )

    return app
