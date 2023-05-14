"""fix column scocre name

Revision ID: 3270830bf0ed
Revises: f483284f0c40
Create Date: 2023-05-14 14:00:57.863501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3270830bf0ed'
down_revision = 'f483284f0c40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('reviews', 'scocre', new_column_name="score")


def downgrade() -> None:
    op.alter_column('reviews', 'score', new_column_name="scocre")
