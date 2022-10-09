"""add table user

Revision ID: 15c64190440e
Revises: 73cb3f39efc8
Create Date: 2022-10-05 23:05:15.650281

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '15c64190440e'
down_revision = '73cb3f39efc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('authenticated', sa.Boolean(), nullable=True))
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'is_authenticated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_authenticated', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('user', 'authenticated')
    # ### end Alembic commands ###
