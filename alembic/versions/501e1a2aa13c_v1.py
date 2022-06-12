"""v1

Revision ID: 501e1a2aa13c
Revises: e98c2422f036
Create Date: 2021-12-21 19:48:03.354930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '501e1a2aa13c'
down_revision = 'e98c2422f036'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_index(op.f('ix_tb_relation_teams_players_guid'), table_name='tb_relation_teams_players')
    op.drop_table('tb_relation_teams_players')
    op.drop_index(op.f('ix_tb_relation_cups_teams_guid'), table_name='tb_relation_cups_teams')
    op.drop_table('tb_relation_cups_teams')
    op.drop_index(op.f('ix_tb_players_guid'), table_name='tb_players')
    op.drop_table('tb_players')
    op.drop_index(op.f('ix_tb_positions_guid'), table_name='tb_positions')
    op.drop_table('tb_positions')
    op.drop_index(op.f('ix_tb_cups_guid'), table_name='tb_cups')
    op.drop_table('tb_cups')
    op.drop_index(op.f('ix_tb_users_guid'), table_name='tb_users')
    op.drop_table('tb_users')
    op.drop_index(op.f('ix_tb_teams_guid'), table_name='tb_teams')
    op.drop_table('tb_teams')
    op.drop_index(op.f('ix_tb_sports_guid'), table_name='tb_sports')
    op.drop_table('tb_sports')
    op.drop_index(op.f('ix_tb_skills_guid'), table_name='tb_skills')
    op.drop_table('tb_skills')
    op.drop_index(op.f('ix_tb_goals_guid'), table_name='tb_goals')
    op.drop_table('tb_goals')


def downgrade():
    op.drop_index(op.f('ix_tb_relation_teams_players_guid'), table_name='tb_relation_teams_players')
    op.drop_table('tb_relation_teams_players')
    op.drop_index(op.f('ix_tb_relation_cups_teams_guid'), table_name='tb_relation_cups_teams')
    op.drop_table('tb_relation_cups_teams')
    op.drop_index(op.f('ix_tb_players_guid'), table_name='tb_players')
    op.drop_table('tb_players')
    op.drop_index(op.f('ix_tb_positions_guid'), table_name='tb_positions')
    op.drop_table('tb_positions')
    op.drop_index(op.f('ix_tb_cups_guid'), table_name='tb_cups')
    op.drop_table('tb_cups')
    op.drop_index(op.f('ix_tb_users_guid'), table_name='tb_users')
    op.drop_table('tb_users')
    op.drop_index(op.f('ix_tb_teams_guid'), table_name='tb_teams')
    op.drop_table('tb_teams')
    op.drop_index(op.f('ix_tb_sports_guid'), table_name='tb_sports')
    op.drop_table('tb_sports')
    op.drop_index(op.f('ix_tb_skills_guid'), table_name='tb_skills')
    op.drop_table('tb_skills')
    op.drop_index(op.f('ix_tb_goals_guid'), table_name='tb_goals')
    op.drop_table('tb_goals')
