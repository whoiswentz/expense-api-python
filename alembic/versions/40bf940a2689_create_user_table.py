"""create user table

Revision ID: 40bf940a2689
Revises: 3fb4e8cf87ce
Create Date: 2024-10-17 17:54:45.785432

"""
import uuid
from typing import Sequence, Union

import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '40bf940a2689'
down_revision: Union[str, None] = '3fb4e8cf87ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                  server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('username', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.Text, nullable=False)
    )


def downgrade():
    op.drop_table('users')
