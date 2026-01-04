"""create_example_table

Revision ID: 7f44da9a635f
Revises: 83c103c4e2bf
Create Date: 2025-12-28 15:49:17.919225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f44da9a635f'
down_revision: Union[str, None] = '83c103c4e2bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('example',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('register_time', sa.DateTime(), nullable=False),
                    sa.Column('item_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['item_id'], ['example_items.id'], onupdate='CASCADE', ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('username')
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('example', if_exists=True)

