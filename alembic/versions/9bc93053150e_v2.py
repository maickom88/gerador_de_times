"""v2

Revision ID: 9bc93053150e
Revises: 884e585c63c1
Create Date: 2022-01-16 20:10:24.220269

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9bc93053150e'
down_revision = '884e585c63c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_goals',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('guid', postgresql.UUID(), nullable=True),
    sa.Column('id_player', sa.BigInteger(), nullable=True),
    sa.Column('time_goals', sa.String(), nullable=True),
    sa.Column('id_match', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_match'], ['tb_matches.id'], ),
    sa.ForeignKeyConstraint(['id_player'], ['tb_players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_goals_guid'), 'tb_goals', ['guid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_goals_guid'), table_name='tb_goals')
    op.drop_table('tb_goals')
    # ### end Alembic commands ###
