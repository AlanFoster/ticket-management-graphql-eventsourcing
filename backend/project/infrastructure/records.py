from sqlalchemy import Column, Index, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BigInteger, Integer, Text
from sqlalchemy_utils.types.uuid import UUIDType

from project.app import db

Base = declarative_base()


class StoredEventRecord(db.Model):
    """
    Original definition of StoredEventRecord retrieved from:
    https://github.com/johnbywater/eventsourcing/blob/b50f1e6c89a6412da3013b5dbc720f159124e92d/eventsourcing/infrastructure/sqlalchemy/records.py#L149-L184

    But tweaked to work with Postgres
    """

    __tablename__ = "stored_events"

    # Application ID.
    application_name = Column(String(length=32), primary_key=True)

    # Originator ID (e.g. an entity or aggregate ID).
    originator_id = Column(UUIDType(), primary_key=True)

    # Originator version of item in sequence.
    originator_version = Column(
        BigInteger().with_variant(Integer, "sqlite"), primary_key=True
    )

    # Pipeline ID.
    pipeline_id = Column(Integer(), nullable=True)

    # Notification ID.
    notification_id = Column(
        BigInteger().with_variant(Integer, "sqlite"), nullable=True
    )

    # Topic of the item (e.g. path to domain event class).
    topic = Column(Text(), nullable=False)

    # State of the item (serialized dict, possibly encrypted).
    state = Column(Text())

    # Causal dependencies.
    causal_dependencies = Column(Text())

    __table_args__ = (
        Index(
            "stored_events_notification_index",
            "application_name",
            "pipeline_id",
            "notification_id",
            unique=True,
        ),
    )
