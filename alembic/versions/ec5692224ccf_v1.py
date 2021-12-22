"""v1

Revision ID: ec5692224ccf
Revises: 3a5a6b3c2ee3
Create Date: 2021-12-19 21:03:20.795873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec5692224ccf'
down_revision = '3a5a6b3c2ee3'
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
