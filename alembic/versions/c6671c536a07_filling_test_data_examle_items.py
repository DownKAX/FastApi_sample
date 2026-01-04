"""filling_test_data_examle_items

Revision ID: c6671c536a07
Revises: 7f44da9a635f
Create Date: 2025-12-28 15:51:16.844948

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column, Integer, String

# revision identifiers, used by Alembic.
revision: str = 'c6671c536a07'
down_revision: Union[str, None] = '7f44da9a635f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

example_items_table = table("example_items",
                  column("id", Integer),
                           column("description", String))


def upgrade() -> None:
    test_data = [{'description': 'test description1'}, {'description': 'test description2'}]
    op.bulk_insert(example_items_table, test_data)


def downgrade() -> None:
    op.execute('TRUNCATE TABLE example_items CASCADE')