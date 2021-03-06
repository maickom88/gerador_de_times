"""v2

Revision ID: 99a311f5129d
Revises: d34453479fcd
Create Date: 2022-01-16 19:51:45.400074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a311f5129d'
down_revision = 'd34453479fcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tb_goals_id_match_fkey', 'tb_goals', type_='foreignkey')
    op.create_foreign_key(None, 'tb_goals', 'tb_matches', ['id_match'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tb_goals', type_='foreignkey')
    op.create_foreign_key('tb_goals_id_match_fkey', 'tb_goals', 'tb_players', ['id_match'], ['id'])
    # ### end Alembic commands ###
