"""add last few to columns to post table

Revision ID: 585ae0d9d61d
Revises: 0a755baccd6d
Create Date: 2022-02-06 18:30:39.591722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '585ae0d9d61d'
down_revision = '0a755baccd6d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
