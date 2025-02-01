"""Update models

Revision ID: 089325a7d1ce
Revises: 47aeab46f81f
Create Date: 2025-02-01 20:07:21.323657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '089325a7d1ce'
down_revision: Union[str, None] = '47aeab46f81f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'seller_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'seller_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
