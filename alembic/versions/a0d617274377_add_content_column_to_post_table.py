"""add content column to post table

Revision ID: a0d617274377
Revises: cea84f9816d2
Create Date: 2022-02-06 17:39:01.048832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0d617274377'
down_revision = 'cea84f9816d2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
