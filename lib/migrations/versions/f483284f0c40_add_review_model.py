"""Add Review Model

Revision ID: f483284f0c40
Revises: 24cb34244fd0
Create Date: 2023-05-14 13:54:59.558467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f483284f0c40'
down_revision = '24cb34244fd0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scocre', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_reviews_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
