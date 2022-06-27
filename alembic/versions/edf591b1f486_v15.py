"""v15

Revision ID: edf591b1f486
Revises: 35e0f0e8affd
Create Date: 2022-06-24 16:26:53.781654

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'edf591b1f486'
down_revision = '35e0f0e8affd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_devices',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('guid', postgresql.UUID(), nullable=True),
    sa.Column('id_user', sa.BigInteger(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('platform', sa.Enum('ANDROID', 'IOS', name='PlatformEnum'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_devices_guid'), 'tb_devices', ['guid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_devices_guid'), table_name='tb_devices')
    op.drop_table('tb_devices')
    # ### end Alembic commands ###
