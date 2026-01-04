"""filling_test_data_examle

Revision ID: e11bccc6f971
Revises: c6671c536a07
Create Date: 2025-12-28 15:51:36.950398

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import Integer, String, DateTime

# revision identifiers, used by Alembic.
revision: str = 'e11bccc6f971'
down_revision: Union[str, None] = 'c6671c536a07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

example_table = table('example',
                      column('id', Integer),
                               column('username', String),
                               column('register_time', DateTime),
                               column("item_id", Integer))


def upgrade() -> None:
    time = datetime(2025, 3, 19, 15, 34, 59)
    test_data_example = [{'username': 'test', 'register_time': time, 'item_id': 1},
                         {'username': 'test2', 'register_time': time, 'item_id': 2}]
    op.bulk_insert(example_table, test_data_example)


def downgrade() -> None:
    op.execute('TRUNCATE TABLE example CASCADE')

