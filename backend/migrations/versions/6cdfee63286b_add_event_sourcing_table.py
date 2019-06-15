"""add event sourcing table

Revision ID: 6cdfee63286b
Revises:
Create Date: 2019-06-14 14:09:51.720373

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import BigInteger, Integer

# revision identifiers, used by Alembic.
revision = "6cdfee63286b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "stored_events",
        sa.Column("application_name", sa.String(length=32), nullable=False),
        sa.Column(
            "originator_id", sqlalchemy_utils.types.uuid.UUIDType(), nullable=False
        ),
        sa.Column(
            "originator_version",
            BigInteger().with_variant(Integer, "sqlite"),
            nullable=False,
        ),
        sa.Column("pipeline_id", sa.Integer(), nullable=True),
        sa.Column(
            "notification_id",
            BigInteger().with_variant(Integer, "sqlite"),
            nullable=True,
        ),
        sa.Column("topic", sa.Text(), nullable=False),
        sa.Column("state", sa.Text(), nullable=True),
        sa.Column("causal_dependencies", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint(
            "application_name", "originator_id", "originator_version"
        ),
    )
    op.create_index(
        "stored_events_notification_index",
        "stored_events",
        ["application_name", "pipeline_id", "notification_id"],
        unique=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("stored_events_notification_index", table_name="stored_events")
    op.drop_table("stored_events")
    # ### end Alembic commands ###