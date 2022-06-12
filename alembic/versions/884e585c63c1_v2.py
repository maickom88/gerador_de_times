"""v2

Revision ID: 884e585c63c1
Revises: 99a311f5129d
Create Date: 2022-01-16 19:59:09.596306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884e585c63c1'
down_revision = '99a311f5129d'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_index(op.f('ix_tb_goals_guid'), table_name='tb_goals')
    op.drop_table('tb_goals')


def downgrade():
    op.drop_index(op.f('ix_tb_goals_guid'), table_name='tb_goals')
    op.drop_table('tb_goals')