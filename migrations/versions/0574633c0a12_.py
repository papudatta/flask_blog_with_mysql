"""empty message

Revision ID: 0574633c0a12
Revises: d48e2d305f6e
Create Date: 2018-07-21 17:59:40.536949

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0574633c0a12'
down_revision = 'd48e2d305f6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('author', 'password',
               existing_type=mysql.VARCHAR(length=15),
               type_=sa.String(length=60),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'password',
               existing_type=sa.String(length=60),
               type_=mysql.VARCHAR(length=15),
               existing_nullable=True)
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
