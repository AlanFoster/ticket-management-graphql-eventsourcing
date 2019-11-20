import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_overrides=None):
    # create and configure the app
    app = Flask(__name__)
    db.init_app(app)
    CORS(app)

    app.config.from_pyfile("config.py")
    if config_overrides:
        app.config.update(config_overrides)

    migrate = Migrate(app, db)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from project.application.tickets import init_application, get_application

    @app.before_first_request
    def before_first_request():
        init_application(session=db.session)

    from project.api.schema import schema
    from project.api.resolve_info import Context

    app.add_url_rule("/health", view_func=lambda: "OK")
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view(
            "graphql",
            schema=schema,
            graphiql=app.debug,
            get_context=lambda: Context(ticket_app=get_application()),
        ),
    )

    return app
